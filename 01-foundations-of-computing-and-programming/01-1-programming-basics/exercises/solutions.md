# Solutions: 1.1 Programming Basics

Use these to check your thinking after you attempt the exercises.

## Exercise 1: Input Validation Gate

```python
from __future__ import annotations

from typing import Iterable


def validate_scores(scores: list[float], min_score: float, max_score: float) -> list[float]:
    if min_score > max_score:
        raise ValueError("min_score must be <= max_score")
    out: list[float] = []
    for s in scores:
        if not isinstance(s, (int, float)):
            raise TypeError(f"score must be numeric, got {type(s).__name__}")
        if min_score <= float(s) <= max_score:
            out.append(float(s))
    return out
```

## Exercise 2: Deterministic Split

```python
from __future__ import annotations

import random


def train_test_split_indices(n: int, test_size: float, seed: int) -> tuple[list[int], list[int]]:
    if n <= 1:
        raise ValueError("n must be > 1")
    if not (0.0 < test_size < 1.0):
        raise ValueError("test_size must be between 0 and 1 (exclusive)")

    idx = list(range(n))
    rng = random.Random(seed)
    rng.shuffle(idx)

    n_test = max(1, int(round(n * test_size)))
    test_idx = idx[:n_test]
    train_idx = idx[n_test:]
    return train_idx, test_idx
```

## Exercise 3: Safe File Read Wrapper

```python
from __future__ import annotations

from pathlib import Path


def read_text_file(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"file not found: {path}")
    lines = path.read_text(encoding="utf-8").splitlines()
    lines = [ln.rstrip() for ln in lines]
    return "\n".join(lines)
```

## Exercise 4: Retry With Backoff (Bounded)

```python
from __future__ import annotations

import time
from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def retry(fn: Callable[[], T], max_attempts: int, base_sleep_s: float) -> T:
    if max_attempts < 1:
        raise ValueError("max_attempts must be >= 1")
    if base_sleep_s < 0:
        raise ValueError("base_sleep_s must be >= 0")

    last_exc: Exception | None = None
    for attempt in range(max_attempts):
        try:
            return fn()
        except Exception as exc:  # noqa: BLE001 - exercise: re-raise last failure
            last_exc = exc
            if attempt == max_attempts - 1:
                raise
            time.sleep(base_sleep_s * (2**attempt))

    # Unreachable, but keeps type-checkers happy.
    assert last_exc is not None
    raise last_exc
```

## Exercise 5: “No Hidden State” Refactor

One simple approach: represent state explicitly.

```python
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Accumulator:
    total: int = 0

    def add_and_report(self, x: int) -> int:
        self.total += x
        return self.total
```

