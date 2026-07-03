#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Any

import joblib
import pandas as pd
import yaml
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


logger = logging.getLogger(__name__)


def _project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _load_config(config_path: Path) -> dict[str, Any]:
    data = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("config must be a YAML mapping")
    return data


def _metrics(y_true, y_pred, y_proba) -> dict[str, float]:
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "precision": float(precision_score(y_true, y_pred)),
        "recall": float(recall_score(y_true, y_pred)),
        "f1": float(f1_score(y_true, y_pred)),
        "roc_auc": float(roc_auc_score(y_true, y_proba)),
    }


def train(*, config_path: Path, root: Path, force: bool = False) -> Path:
    """Train a baseline model and persist artifacts.

    Teaches:
    - fit preprocessing on train only (pipeline)
    - artifact persistence (model + metrics)
    - deterministic config-driven runs
    """
    cfg = _load_config(config_path)

    train_csv = root / str(cfg["paths"]["processed_train_csv"])
    test_csv = root / str(cfg["paths"]["processed_test_csv"])
    raw_csv = root / str(cfg["paths"]["raw_csv"])

    if train_csv.exists() and test_csv.exists():
        logger.info("Using processed splits: %s %s", train_csv, test_csv)
        train_df = pd.read_csv(train_csv)
        test_df = pd.read_csv(test_csv)
    else:
        if not raw_csv.exists():
            raise FileNotFoundError(f"raw dataset not found: {raw_csv}. Run ingest.py first.")
        logger.info("Processed splits missing; training directly from raw (recommended: run prepare.py).")
        df = pd.read_csv(raw_csv)
        # Minimal fallback: take the first 75% as train to avoid additional deps.
        cut = int(len(df) * 0.75)
        train_df = df.iloc[:cut].copy()
        test_df = df.iloc[cut:].copy()

    if "target" not in train_df.columns:
        raise ValueError("expected a 'target' column in training data")

    artifact_dir = root / str(cfg["paths"]["artifact_dir"])
    artifact_dir.mkdir(parents=True, exist_ok=True)
    model_path = artifact_dir / "model.joblib"
    metrics_path = artifact_dir / "metrics_train.json"

    if model_path.exists() and metrics_path.exists() and not force:
        logger.info("Model artifacts already exist (skipping). model=%s metrics=%s", model_path, metrics_path)
        return model_path

    configured_features = cfg.get("features")
    if configured_features is None:
        feature_cols = [c for c in train_df.columns if c not in {"target", "row_id"}]
    else:
        if not isinstance(configured_features, list) or not all(
            isinstance(x, str) for x in configured_features
        ):
            raise ValueError("config.features must be a list[str]")
        feature_cols = configured_features

    missing = sorted(set(feature_cols) - set(train_df.columns))
    if missing:
        raise ValueError(f"training data missing required feature columns: {missing}")

    X_train = train_df[feature_cols]
    y_train = train_df["target"]
    X_test = test_df[feature_cols]
    y_test = test_df["target"]

    model_cfg = cfg.get("model", {})
    params = dict(model_cfg.get("params", {}))

    pipe = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("clf", LogisticRegression(**params)),
        ]
    )
    pipe.fit(X_train, y_train)

    pred = pipe.predict(X_test)
    proba = pipe.predict_proba(X_test)[:, 1]
    metrics = _metrics(y_test, pred, proba)
    metrics_out = {"split": "test", "metrics": metrics}

    joblib.dump(pipe, model_path)
    metrics_path.write_text(json.dumps(metrics_out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    logger.info("Saved model + metrics. model=%s metrics=%s", model_path, metrics_path)
    return model_path


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    parser = argparse.ArgumentParser(description="Train a baseline model for the capstone template.")
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
    parser.add_argument("--force", action="store_true", help="Overwrite existing artifacts.")
    args = parser.parse_args()

    train(config_path=args.config, root=args.root, force=args.force)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
