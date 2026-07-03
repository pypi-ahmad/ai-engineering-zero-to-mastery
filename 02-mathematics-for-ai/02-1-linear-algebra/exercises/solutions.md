# Solutions: 2.1 Linear Algebra

## Exercise 1: Cosine Similarity (Correctness)

```python
from __future__ import annotations

import numpy as np


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    a = np.asarray(a)
    b = np.asarray(b)
    if a.ndim != 1 or b.ndim != 1:
        raise ValueError(\"a and b must be 1D\")\n    if a.shape != b.shape:\n        raise ValueError(\"a and b must have the same shape\")\n\n    na = float(np.linalg.norm(a))\n    nb = float(np.linalg.norm(b))\n    if na == 0.0 or nb == 0.0:\n        raise ValueError(\"cosine similarity is undefined for zero vectors\")\n\n    return float(a @ b) / (na * nb)\n```

## Exercise 2: Shape Reasoning

1. valid -> `(3, 2)`
2. valid -> scalar
3. valid -> `(4,)`
4. valid -> `(4,)`

## Exercise 3: Least Squares From Scratch

```python
from __future__ import annotations\n\nimport numpy as np\n\nrng = np.random.default_rng(42)\n\nn, d = 200, 3\nX = rng.normal(size=(n, d))\nw_true = rng.normal(size=(d,))\nnoise = 0.1 * rng.normal(size=(n,))\n\ny = X @ w_true + noise\n\n# Normal equation: (X^T X)^{-1} X^T y\nw_hat = np.linalg.solve(X.T @ X, X.T @ y)\nprint(\"w_true:\", w_true)\nprint(\"w_hat:\", w_hat)\n```

## Exercise 4: Projection Error

```python
from __future__ import annotations\n\nimport numpy as np\n\nu = np.array([1.0, 2.0, 3.0])\nv = np.array([2.0, -1.0, 0.5])\n\nproj = (v @ u) / (u @ u) * u\nr = v - proj\nprint(\"u·r:\", float(u @ r))\n```

## Exercise 5: Nearest Neighbor by Dot Product

```python
from __future__ import annotations\n\nimport numpy as np\n\n\ndef nn_dot(E: np.ndarray, q: np.ndarray) -> int:\n    scores = E @ q\n    return int(np.argmax(scores))\n\n\ndef nn_cos(E: np.ndarray, q: np.ndarray) -> int:\n    E = np.asarray(E)\n    q = np.asarray(q)\n    qn = np.linalg.norm(q)\n    En = np.linalg.norm(E, axis=1)\n    scores = (E @ q) / (En * qn)\n    return int(np.argmax(scores))\n```

Dot-product and cosine rankings are identical when all embedding vectors are already normalized to the same norm (commonly unit norm).

