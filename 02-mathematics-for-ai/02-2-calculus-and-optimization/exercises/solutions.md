# Solutions: 2.2 Calculus & Optimization

## Exercise 1: Numerical Derivative

```python
from __future__ import annotations\n\nfrom collections.abc import Callable\n\n\ndef numerical_derivative(f: Callable[[float], float], x: float, eps: float = 1e-5) -> float:\n    return (f(x + eps) - f(x - eps)) / (2 * eps)\n\n\nprint(numerical_derivative(lambda t: t**3, 2.0))\n```

## Exercise 2: Gradient Descent on a Quadratic

```python
from __future__ import annotations\n\n\ndef gd(lr: float, steps: int = 30, w0: float = 0.0) -> float:\n    w = w0\n    for _ in range(steps):\n        grad = 2 * (w - 3.0)\n        w = w - lr * grad\n    return w\n\n\nfor lr in [0.01, 0.1, 1.1]:\n    print(lr, gd(lr))\n```

For `f(w)=(w-3)^2`, GD converges for `0 < lr < 1` (because the curvature is 2).

## Exercise 3: Vector Gradient Check

```python
from __future__ import annotations\n\nimport numpy as np\n\nrng = np.random.default_rng(42)\nA = rng.normal(size=(10, 3))\nb = rng.normal(size=(10,))\n\n\ndef f(w: np.ndarray) -> float:\n    r = A @ w - b\n    return float(r @ r)\n\n\ndef grad(w: np.ndarray) -> np.ndarray:\n    # f(w) = ||Aw-b||^2 => grad = 2 A^T(Aw-b)\n    return 2 * (A.T @ (A @ w - b))\n\n\ndef num_grad(w: np.ndarray, eps: float = 1e-6) -> np.ndarray:\n    g = np.zeros_like(w)\n    for i in range(len(w)):\n        e = np.zeros_like(w)\n        e[i] = eps\n        g[i] = (f(w + e) - f(w - e)) / (2 * eps)\n    return g\n\n\nw = rng.normal(size=(3,))\nprint(\"analytic:\", grad(w))\nprint(\"numeric :\", num_grad(w))\nprint(\"max abs diff:\", float(np.max(np.abs(grad(w) - num_grad(w)))))\n```

## Exercise 4: Autograd Sanity Check (PyTorch)

```python
import torch\n\nw = torch.tensor([1.0, -2.0, 3.0], requires_grad=True)\nloss = (w**2).sum()\nloss.backward()\nprint(w.grad)  # tensor([ 2., -4.,  6.])\n```

## Exercise 5: “Bad Learning Rate” Diagnosis Note

One reasonable answer:

- Too high: loss oscillates or explodes; gradients become unstable; metrics jump wildly.
- Too low: loss decreases extremely slowly; training takes too long; model underfits given time budget.
- Mitigate too high: reduce LR; use warmup; add gradient clipping.
- Mitigate too low: increase LR; use LR schedules; normalize inputs; use an adaptive optimizer.

