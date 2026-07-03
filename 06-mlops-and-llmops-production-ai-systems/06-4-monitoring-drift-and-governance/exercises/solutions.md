# Solutions: 6.4 Monitoring, Drift & Governance

## Exercise 1: Drift Detection (KS Test)

```python
from __future__ import annotations

import numpy as np
from scipy.stats import ks_2samp

rng = np.random.default_rng(42)

train = rng.normal(loc=0.0, scale=1.0, size=5000)
serve_ok = rng.normal(loc=0.05, scale=1.0, size=5000)
serve_drift = rng.normal(loc=0.6, scale=1.2, size=5000)

for name, s in [("ok", serve_ok), ("drift", serve_drift)]:
    stat, p = ks_2samp(train, s)
    print(name, "KS", float(stat), "p", float(p))
```

Policy example:
- alert if `p < 1e-5` **and** effect size (`KS stat`) > 0.1.

## Exercise 2: Rolling Performance Monitor

```python
from __future__ import annotations

import numpy as np

rng = np.random.default_rng(42)
T = 5000

# Simulate accuracy drop after t=3000
correct = np.concatenate(
    [rng.binomial(1, 0.95, size=3000), rng.binomial(1, 0.82, size=2000)]
)

win = 200
roll = np.convolve(correct, np.ones(win) / win, mode="valid")
threshold = 0.90
alerts = np.where(roll < threshold)[0]
print("first alert index", int(alerts[0]) if len(alerts) else None)
```

## Exercise 3: Data Quality Gates for Inference

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class GateResult:
    ok: bool
    reason: str | None = None


def validate_payload(payload: dict[str, Any]) -> GateResult:
    required = {"age", "income", "country"}
    missing = required - set(payload)
    if missing:
        return GateResult(False, f"missing: {sorted(missing)}")
    age = payload["age"]
    if not isinstance(age, (int, float)) or age < 0 or age > 120:
        return GateResult(False, "bad age")
    if payload["country"] not in {"US", "CA", "IN"}:
        return GateResult(False, "unknown country")
    return GateResult(True)
```

## Exercise 4: Governance Checklist (Release Gate)

Example checklist items:
- metrics on fixed eval set meet thresholds
- model card updated
- monitoring dashboard + alerts configured
- rollback runbook exists
- privacy/security review complete

## Exercise 5: Retraining Trigger Policy

Example policy:
- trigger retrain if drift alert persists for 3 consecutive windows OR rolling accuracy < 0.88 for 5 windows.

