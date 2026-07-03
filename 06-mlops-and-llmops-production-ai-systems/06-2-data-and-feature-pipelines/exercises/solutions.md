# Solutions: 6.2 Data & Feature Pipelines

## Exercise 1: Schema + Range Validation

```python
from __future__ import annotations

import pandas as pd


def validate_table(df: pd.DataFrame) -> None:
    required = {"user_id": "int64", "age": "float64", "country": "object"}
    missing = set(required) - set(df.columns)
    if missing:
        raise ValueError(f"missing columns: {sorted(missing)}")
    for col, dtype in required.items():
        if str(df[col].dtype) != dtype:
            raise ValueError(f"bad dtype for {col}: expected {dtype}, got {df[col].dtype}")
    if (df["age"] < 0).any():
        raise ValueError("age must be non-negative")
```

## Exercise 2: Dataset Fingerprint (Hash)

```python
from __future__ import annotations

import hashlib
import pandas as pd


def df_fingerprint(df: pd.DataFrame) -> str:
    df2 = df.copy()
    df2 = df2.reindex(sorted(df2.columns), axis=1)
    data = df2.to_csv(index=False).encode("utf-8")
    return hashlib.sha256(data).hexdigest()
```

## Exercise 3: Point-in-Time Join (Toy)

```python
from __future__ import annotations

import pandas as pd


def point_in_time_join(events: pd.DataFrame, feats: pd.DataFrame) -> pd.DataFrame:
    # events: entity_id, event_time
    # feats: entity_id, feature_time, value
    e = events.sort_values(["entity_id", "event_time"]).copy()
    f = feats.sort_values(["entity_id", "feature_time"]).copy()
    out = pd.merge_asof(
        e,
        f,
        left_on="event_time",
        right_on="feature_time",
        by="entity_id",
        direction="backward",
        allow_exact_matches=True,
    )
    return out
```

## Exercise 4: Offline/Online Feature Consistency Check

```python
from __future__ import annotations

import pandas as pd


def offline_feature(df: pd.DataFrame) -> pd.Series:
    return df["x"].fillna(0).astype(float) * 2.0


def online_feature(x: float | None) -> float:
    return float(0 if x is None else x) * 2.0


df = pd.DataFrame({"x": [1.0, None, 2.5]})
off = offline_feature(df).tolist()
on = [online_feature(v) for v in df["x"].tolist()]
assert off == on
```

## Exercise 5: Pipeline Metadata Record

```python
from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def git_sha() -> str | None:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return None


def write_metadata(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, indent=2), encoding="utf-8")


record = {
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "input_hash": "abc",
    "output_hash": "def",
    "features": ["age_bucket", "is_us"],
    "git_sha": git_sha(),
}
write_metadata(Path("artifacts/pipeline_metadata.json"), record)
```

