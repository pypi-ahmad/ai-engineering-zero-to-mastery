#!/usr/bin/env python3
from __future__ import annotations

import argparse
import logging
from pathlib import Path
from typing import Any

import pandas as pd
import yaml
from sklearn.datasets import load_breast_cancer


logger = logging.getLogger(__name__)


def _project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _load_config(config_path: Path) -> dict[str, Any]:
    data = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("config must be a YAML mapping")
    return data


def ingest(*, config_path: Path, root: Path, force: bool = False) -> Path:
    """Create an offline-friendly raw dataset CSV.

    Uses `sklearn.datasets.load_breast_cancer` to avoid network/download friction.
    """
    cfg = _load_config(config_path)
    raw_csv = root / str(cfg["paths"]["raw_csv"])
    raw_csv.parent.mkdir(parents=True, exist_ok=True)

    if raw_csv.exists() and not force:
        logger.info("Raw dataset already exists (skipping). path=%s", raw_csv)
        return raw_csv

    ds = load_breast_cancer(as_frame=True)
    df: pd.DataFrame = ds.frame.copy()
    # Ensure a stable row id for downstream reproducibility.
    df.insert(0, "row_id", range(len(df)))

    # Normalize column names to snake_case for easier serving contracts.
    df.columns = [
        str(c).strip().lower().replace(" ", "_").replace("-", "_") for c in df.columns
    ]

    df.to_csv(raw_csv, index=False)
    logger.info("Wrote raw dataset. rows=%d path=%s", len(df), raw_csv)
    return raw_csv


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    parser = argparse.ArgumentParser(description="Ingest raw dataset for the capstone template.")
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
    parser.add_argument("--force", action="store_true", help="Overwrite existing raw dataset.")
    args = parser.parse_args()

    ingest(config_path=args.config, root=args.root, force=args.force)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
