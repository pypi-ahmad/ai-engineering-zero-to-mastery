#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd
import yaml
from sklearn.model_selection import train_test_split


logger = logging.getLogger(__name__)


def _project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _load_config(config_path: Path) -> dict[str, Any]:
    data = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("config must be a YAML mapping")
    return data


@dataclass(frozen=True)
class SplitArtifacts:
    train_path: Path
    test_path: Path
    split_meta_path: Path


def prepare(*, config_path: Path, root: Path, force: bool = False) -> SplitArtifacts:
    """Split raw data into train/test CSVs (no modeling here).

    This is a deliberately simple "data engineering" step to teach:
    - deterministic splits
    - preserving ids for reproducibility
    """
    cfg = _load_config(config_path)
    seed = int(cfg.get("seed", 42))

    raw_csv = root / str(cfg["paths"]["raw_csv"])
    train_csv = root / str(cfg["paths"]["processed_train_csv"])
    test_csv = root / str(cfg["paths"]["processed_test_csv"])

    train_csv.parent.mkdir(parents=True, exist_ok=True)
    test_csv.parent.mkdir(parents=True, exist_ok=True)

    split_meta_path = root / str(cfg["paths"].get("split_meta_json", "artifacts/split_meta.json"))
    split_meta_path.parent.mkdir(parents=True, exist_ok=True)

    if train_csv.exists() and test_csv.exists() and split_meta_path.exists() and not force:
        logger.info("Processed train/test already exist (skipping).")
        return SplitArtifacts(train_path=train_csv, test_path=test_csv, split_meta_path=split_meta_path)

    if not raw_csv.exists():
        raise FileNotFoundError(f"raw dataset not found: {raw_csv}. Run ingest.py first.")

    df = pd.read_csv(raw_csv)
    if "target" not in df.columns:
        raise ValueError("expected a 'target' column in raw dataset")
    if "row_id" not in df.columns:
        raise ValueError("expected a 'row_id' column in raw dataset")

    y = df["target"]
    stratify = y if bool(cfg["split"].get("stratify", True)) else None

    train_df, test_df = train_test_split(
        df,
        test_size=float(cfg["split"]["test_size"]),
        random_state=seed,
        stratify=stratify,
    )

    train_df.to_csv(train_csv, index=False)
    test_df.to_csv(test_csv, index=False)

    meta = {
        "seed": seed,
        "test_size": float(cfg["split"]["test_size"]),
        "n_train": int(len(train_df)),
        "n_test": int(len(test_df)),
        "train_row_ids": train_df["row_id"].astype(int).tolist(),
        "test_row_ids": test_df["row_id"].astype(int).tolist(),
    }
    split_meta_path.write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    logger.info("Wrote processed splits. train=%s test=%s meta=%s", train_csv, test_csv, split_meta_path)
    return SplitArtifacts(train_path=train_csv, test_path=test_csv, split_meta_path=split_meta_path)


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    parser = argparse.ArgumentParser(description="Prepare train/test splits for the capstone template.")
    parser.add_argument(
        "--config",
        type=Path,
        default=_project_root() / "configs" / "config.yaml",
        help="Path to config YAML.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=_project_root(),
        help="Project root for resolving relative paths.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing processed outputs.")
    args = parser.parse_args()

    prepare(config_path=args.config, root=args.root, force=args.force)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

