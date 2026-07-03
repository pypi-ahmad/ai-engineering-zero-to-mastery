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
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score


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


def evaluate(*, config_path: Path, root: Path) -> Path:
    """Evaluate the trained artifact on the test split and write metrics."""
    cfg = _load_config(config_path)

    artifact_dir = root / str(cfg["paths"]["artifact_dir"])
    model_path = artifact_dir / "model.joblib"
    if not model_path.exists():
        raise FileNotFoundError(f"model artifact not found: {model_path}. Run train.py first.")

    test_csv = root / str(cfg["paths"]["processed_test_csv"])
    if not test_csv.exists():
        raise FileNotFoundError(f"processed test split not found: {test_csv}. Run prepare.py first.")

    test_df = pd.read_csv(test_csv)
    if "target" not in test_df.columns:
        raise ValueError("expected a 'target' column in test data")

    configured_features = cfg.get("features")
    if configured_features is None:
        feature_cols = [c for c in test_df.columns if c not in {"target", "row_id"}]
    else:
        if not isinstance(configured_features, list) or not all(
            isinstance(x, str) for x in configured_features
        ):
            raise ValueError("config.features must be a list[str]")
        feature_cols = configured_features

    missing = sorted(set(feature_cols) - set(test_df.columns))
    if missing:
        raise ValueError(f"test data missing required feature columns: {missing}")

    X_test = test_df[feature_cols]
    y_test = test_df["target"]

    pipe = joblib.load(model_path)
    pred = pipe.predict(X_test)
    proba = pipe.predict_proba(X_test)[:, 1]
    metrics = _metrics(y_test, pred, proba)

    metrics_path = artifact_dir / "metrics_eval.json"
    metrics_path.write_text(
        json.dumps({"split": "test", "metrics": metrics}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    logger.info("Wrote evaluation metrics. path=%s", metrics_path)
    return metrics_path


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    parser = argparse.ArgumentParser(description="Evaluate the baseline model for the capstone template.")
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
    args = parser.parse_args()

    evaluate(config_path=args.config, root=args.root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
