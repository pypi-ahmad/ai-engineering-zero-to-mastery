# Solutions: 6.1 MLOps Fundamentals & Lifecycle

## Exercise 1: Run Metadata (Reproducibility)

```python
from __future__ import annotations

import json
import platform
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _git_sha() -> str | None:
    try:
        out = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
        return out
    except Exception:
        return None


def make_run_metadata(dataset_id: str, model_type: str, hyperparams: dict[str, Any]) -> dict[str, Any]:
    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),
        "git_sha": _git_sha(),
        "dataset_id": dataset_id,
        "model_type": model_type,
        "hyperparams": hyperparams,
    }


meta = make_run_metadata(
    dataset_id="sklearn:breast_cancer:v1",
    model_type="LogisticRegression",
    hyperparams={"max_iter": 2000, "C": 1.0},
)
artifact_dir = Path("artifacts/lesson6_1")
artifact_dir.mkdir(parents=True, exist_ok=True)
(artifact_dir / "run_metadata.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
```

## Exercise 2: “Pipeline as Functions” (Idempotent)

```python
from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split


@dataclass(frozen=True)
class Result:
    model: LogisticRegression
    metrics: dict[str, float]


def ingest() -> pd.DataFrame:
    data = load_breast_cancer(as_frame=True)
    df = data.frame.copy()
    return df


def train(df: pd.DataFrame, seed: int = 42) -> LogisticRegression:
    X = df.drop(columns=["target"])
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=seed, stratify=y
    )
    m = LogisticRegression(max_iter=2000)
    m.fit(X_train, y_train)
    return m


def evaluate(model: LogisticRegression, df: pd.DataFrame, seed: int = 42) -> dict[str, float]:
    X = df.drop(columns=["target"])
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=seed, stratify=y
    )
    proba = model.predict_proba(X_test)[:, 1]
    return {"roc_auc": float(roc_auc_score(y_test, proba))}


def main() -> Result:
    df = ingest()
    model = train(df)
    metrics = evaluate(model, df)
    return Result(model=model, metrics=metrics)


print(main().metrics)
```

## Exercise 3: Model Card (Minimal)

Suggested structure (copy into your project docs):

```text
Intended use:
Data:
Model:
Metrics:
Limitations:
Monitoring plan:
```

## Exercise 4: Baseline + Regression Gate

Example gate:
- ship only if ROC AUC >= 0.97 on a fixed heldout split.

## Exercise 5: Maturity Mapping

Example mapping:
- Level 0: ad-hoc notebook runs, no saved metadata.
- Next: add run metadata + fixed splits + regression gate (Level 1).

