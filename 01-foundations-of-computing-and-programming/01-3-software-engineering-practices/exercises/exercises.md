# Exercises: 1.3 Software Engineering Practices

These exercises aim to turn “notebook code” into “team code”: testable, reviewable, and reproducible.

## Exercise 1: Pure Function + Unit Tests

Write a pure function:

`safe_divide(a: float, b: float) -> float`

Rules:
- raise `ValueError` if `b == 0`,
- handle ints and floats,
- no global state.

Then write 3 pytest tests:
- normal case,
- division by zero,
- negative numbers.

Expected outcome:
- `pytest` passes.

## Exercise 2: Make It a Small Module

Create a small module layout in a temp folder:

```text
mini_pkg/
  __init__.py
  metrics.py
```

In `metrics.py`, implement:
- `accuracy(y_true: list[int], y_pred: list[int]) -> float`
- input validation (length match, non-empty)

Expected outcome:
- you can `import mini_pkg.metrics` and call `accuracy`.

## Exercise 3: Logging (No Prints)

Write a script that:
- logs at `INFO` when it starts and ends,
- logs at `WARNING` when it sees invalid input,
- logs at `ERROR` when it catches an exception and re-raises.

Expected outcome:
- output is readable and includes level names.

## Exercise 4: Reproducible Randomness

Write a function:

`sample_batch(items: list[str], k: int, seed: int) -> list[str]`

Rules:
- deterministic for same seed,
- validate `0 <= k <= len(items)`.

Expected outcome:
- two calls with same inputs return identical results.

## Exercise 5: Minimal CLI Contract (argparse)

Write a small CLI entrypoint:

`python app.py --n 100 --seed 42`

Behavior:
- creates numbers `0..n-1`,
- shuffles deterministically with `seed`,
- prints the first 5 values.

Expected outcome:
- invalid args produce a helpful error message.

