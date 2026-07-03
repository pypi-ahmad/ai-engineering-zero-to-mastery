# Solutions: 1.3 Software Engineering Practices

## Exercise 1: Pure Function + Unit Tests

```python
from __future__ import annotations


def safe_divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError(\"b must be non-zero\")\n    return float(a) / float(b)\n```

Example pytest tests:

```python
import pytest\n\nfrom your_module import safe_divide\n\n\ndef test_safe_divide_normal() -> None:\n    assert safe_divide(10, 2) == 5.0\n\n\ndef test_safe_divide_zero() -> None:\n    with pytest.raises(ValueError):\n        safe_divide(1, 0)\n\n\ndef test_safe_divide_negative() -> None:\n    assert safe_divide(-6, 2) == -3.0\n```

## Exercise 2: Make It a Small Module

```python
from __future__ import annotations

\n\ndef accuracy(y_true: list[int], y_pred: list[int]) -> float:\n    if not y_true:\n        raise ValueError(\"y_true must be non-empty\")\n    if len(y_true) != len(y_pred):\n        raise ValueError(\"y_true and y_pred must have the same length\")\n    correct = sum(1 for a, b in zip(y_true, y_pred) if a == b)\n    return correct / len(y_true)\n```

## Exercise 3: Logging (No Prints)

```python
from __future__ import annotations\n\nimport logging\n\nlogger = logging.getLogger(__name__)\n\n\ndef main() -> None:\n    logging.basicConfig(level=logging.INFO, format=\"%(levelname)s %(message)s\")\n    logger.info(\"start\")\n    try:\n        value = \"\"  # pretend input\n        if not value:\n            logger.warning(\"invalid input: empty\")\n        raise RuntimeError(\"boom\")\n    except Exception:\n        logger.exception(\"failed\")\n        raise\n    finally:\n        logger.info(\"end\")\n\n\nif __name__ == \"__main__\":\n    main()\n```

## Exercise 4: Reproducible Randomness

```python
from __future__ import annotations\n\nimport random\n\n\ndef sample_batch(items: list[str], k: int, seed: int) -> list[str]:\n    if k < 0 or k > len(items):\n        raise ValueError(\"k out of range\")\n    rng = random.Random(seed)\n    return rng.sample(items, k)\n```

## Exercise 5: Minimal CLI Contract (argparse)

```python
from __future__ import annotations\n\nimport argparse\nimport random\n\n\ndef parse_args() -> argparse.Namespace:\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--n\", type=int, required=True)\n    p.add_argument(\"--seed\", type=int, required=True)\n    return p.parse_args()\n\n\ndef main() -> None:\n    args = parse_args()\n    if args.n < 0:\n        raise SystemExit(\"--n must be >= 0\")\n\n    nums = list(range(args.n))\n    rng = random.Random(args.seed)\n    rng.shuffle(nums)\n    print(nums[:5])\n\n\nif __name__ == \"__main__\":\n    main()\n```

