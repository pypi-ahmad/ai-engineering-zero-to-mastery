# Solutions: 5.2 Autoregressive & Diffusion Models

## Exercise 1: Decoding Strategies (Toy Distribution)

```python
from __future__ import annotations

import numpy as np


def greedy(probs: np.ndarray) -> int:
    return int(np.argmax(probs))


def sample_top_k(probs: np.ndarray, k: int, rng: np.random.Generator) -> int:
    if k < 1:
        raise ValueError("k must be >= 1")
    idx = np.argsort(probs)[::-1][:k]
    p = probs[idx].astype("float64")
    p = p / p.sum()
    return int(rng.choice(idx, p=p))


def sample_top_p(probs: np.ndarray, p: float, rng: np.random.Generator) -> int:
    if not (0.0 < p <= 1.0):
        raise ValueError("p must be in (0,1]")
    order = np.argsort(probs)[::-1]
    cum = np.cumsum(probs[order])
    cut = int(np.searchsorted(cum, p, side="left")) + 1
    idx = order[:cut]
    pp = probs[idx].astype("float64")
    pp = pp / pp.sum()
    return int(rng.choice(idx, p=pp))


rng = np.random.default_rng(42)
probs = np.array([0.22, 0.18, 0.12, 0.10, 0.09, 0.07, 0.07, 0.06, 0.05, 0.04], dtype="float64")

print("greedy", greedy(probs))
print("topk", [sample_top_k(probs, k=3, rng=rng) for _ in range(10)])
print("topp", [sample_top_p(probs, p=0.8, rng=rng) for _ in range(10)])
```

## Exercise 2: Temperature Scaling

```python
from __future__ import annotations

import numpy as np


def softmax(logits: np.ndarray) -> np.ndarray:
    z = logits - logits.max()
    e = np.exp(z)
    return e / e.sum()


def apply_temperature(logits: np.ndarray, temperature: float) -> np.ndarray:
    if temperature <= 0:
        raise ValueError("temperature must be > 0")
    return logits / temperature


def entropy(p: np.ndarray) -> float:
    p = p[p > 0]
    return float(-(p * np.log(p)).sum())


logits = np.array([3.0, 2.0, 1.0, 0.0])
for t in [0.5, 1.0, 2.0]:
    p = softmax(apply_temperature(logits, t))
    print(t, p.round(3), "H", round(entropy(p), 4))
```

## Exercise 3: Bigram Language Model (Character-Level)

```python
from __future__ import annotations

import numpy as np

text = "hello world. hello ai. hello engineering."
chars = sorted(set(text))
stoi = {c: i for i, c in enumerate(chars)}
itos = {i: c for c, i in stoi.items()}
V = len(chars)

counts = np.ones((V, V), dtype="float64")  # add-1 smoothing
for a, b in zip(text[:-1], text[1:]):
    counts[stoi[a], stoi[b]] += 1

probs = counts / counts.sum(axis=1, keepdims=True)

rng = np.random.default_rng(42)
out = []
ch = text[0]
for _ in range(200):
    out.append(ch)
    p = probs[stoi[ch]]
    ch = itos[int(rng.choice(np.arange(V), p=p))]
print("".join(out))
```

## Exercise 4: Diffusion Forward Process (1D)

```python
from __future__ import annotations

import numpy as np

rng = np.random.default_rng(42)

T = 50
betas = np.linspace(1e-4, 2e-2, T, dtype="float64")
alphas = 1.0 - betas
alpha_bar = np.cumprod(alphas)

x0 = np.sin(np.linspace(0, 2 * np.pi, 128)).astype("float64")

def q_sample(x0: np.ndarray, t: int) -> np.ndarray:
    eps = rng.normal(size=x0.shape)
    return np.sqrt(alpha_bar[t]) * x0 + np.sqrt(1 - alpha_bar[t]) * eps


for t in [0, 5, 20, 49]:
    xt = q_sample(x0, t)
    print(t, "var", float(xt.var()))
```

## Exercise 5 (Optional): Diffusers Sanity Run

Keep this optional; it requires model downloads and network access.

