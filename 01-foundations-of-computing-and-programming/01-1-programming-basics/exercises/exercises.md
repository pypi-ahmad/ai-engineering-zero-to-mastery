# Exercises: 1.1 Programming Basics

Do these after you read the theory and run the notebook once from a clean kernel.

## How to Use

- Try each exercise without looking at solutions.
- Use a scratch notebook cell or a small `.py` file.
- For each exercise, write down:
  - your assumption,
  - what can fail,
  - how you would debug it.

## Exercise 1: Input Validation Gate

Write a function `validate_scores(scores: list[float], min_score: float, max_score: float) -> list[float]` that:

- returns only the scores inside `[min_score, max_score]`,
- raises `ValueError` if `min_score > max_score`,
- raises `TypeError` if any score is not `int` or `float`.

Expected outcome:
- given `[0.2, -1.0, 0.7, 2.0]` and range `[0.0, 1.0]` returns `[0.2, 0.7]`.

## Exercise 2: Deterministic Split

Write `train_test_split_indices(n: int, test_size: float, seed: int) -> tuple[list[int], list[int]]` that:

- returns two disjoint index lists,
- is deterministic for the same inputs,
- validates that `0 < test_size < 1` and `n > 1`.

Expected outcome:
- calling it twice with the same args yields the same two lists.

## Exercise 3: Safe File Read Wrapper

Write `read_text_file(path: Path) -> str` that:

- raises a clear error if the file does not exist,
- reads using UTF-8,
- strips trailing whitespace on each line,
- returns the final joined string.

Expected outcome:
- error message includes the missing path.

## Exercise 4: Retry With Backoff (Bounded)

Write `retry(fn, max_attempts: int, base_sleep_s: float)` that:

- calls `fn()` until it succeeds,
- sleeps `base_sleep_s * 2**k` between failures,
- stops after `max_attempts` and re-raises the last exception.

Expected outcome:
- the function never retries forever.

## Exercise 5: “No Hidden State” Refactor

Given this code:

```python
TOTAL = 0

def add_and_report(x: int) -> int:
    global TOTAL
    TOTAL += x
    return TOTAL
```

Refactor it into a version with no global state.

Expected outcome:
- you can compute totals for two independent “sessions” without interference.

