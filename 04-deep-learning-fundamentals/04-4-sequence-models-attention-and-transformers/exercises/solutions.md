# Solutions: 4.4 Sequence Models, Attention & Transformers

## Exercise 1: Scaled Dot-Product Attention (Shapes)

```python
from __future__ import annotations

import torch


def attention(q: torch.Tensor, k: torch.Tensor, v: torch.Tensor) -> torch.Tensor:
    # q,k,v: [B, T, D]
    d = q.size(-1)
    scores = (q @ k.transpose(-2, -1)) / (d**0.5)  # [B, T, T]
    w = torch.softmax(scores, dim=-1)
    return w @ v  # [B, T, D]


B, T, D = 2, 5, 8
q = torch.randn(B, T, D)
k = torch.randn(B, T, D)
v = torch.randn(B, T, D)
out = attention(q, k, v)
print(out.shape)
```

## Exercise 2: Causal Mask (No Looking Ahead)

```python
from __future__ import annotations

import torch


def causal_attention(q: torch.Tensor, k: torch.Tensor, v: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
    d = q.size(-1)
    scores = (q @ k.transpose(-2, -1)) / (d**0.5)  # [B, T, T]
    T = scores.size(-1)
    mask = torch.triu(torch.ones(T, T, dtype=torch.bool), diagonal=1)  # True above diagonal
    scores = scores.masked_fill(mask, float("-inf"))
    w = torch.softmax(scores, dim=-1)
    return w @ v, w


B, T, D = 1, 6, 8
q = torch.randn(B, T, D)
k = torch.randn(B, T, D)
v = torch.randn(B, T, D)
out, w = causal_attention(q, k, v)
print(out.shape)
print("upper triangle max weight:", float(w[0].triu(diagonal=1).max()))
```

## Exercise 3: Positional Encoding (Sinusoidal)

```python
from __future__ import annotations

import math
import torch


def sinusoidal_positional_encoding(T: int, D: int) -> torch.Tensor:
    pe = torch.zeros(T, D)
    position = torch.arange(T, dtype=torch.float32).unsqueeze(1)
    div_term = torch.exp(torch.arange(0, D, 2, dtype=torch.float32) * (-math.log(10000.0) / D))
    pe[:, 0::2] = torch.sin(position * div_term)
    pe[:, 1::2] = torch.cos(position * div_term)
    return pe


pe = sinusoidal_positional_encoding(T=10, D=16)
print(pe.shape)
print(float(pe.min()), float(pe.max()))
print("pos0==pos1?", bool(torch.allclose(pe[0], pe[1])))
```

## Exercise 4: Multi-Head Attention (Minimal)

```python
from __future__ import annotations

import torch
from torch import nn


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model: int, n_heads: int) -> None:
        super().__init__()
        if d_model % n_heads != 0:
            raise ValueError("d_model must be divisible by n_heads")
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_head = d_model // n_heads
        self.qkv = nn.Linear(d_model, 3 * d_model)
        self.proj = nn.Linear(d_model, d_model)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        B, T, D = x.shape
        qkv = self.qkv(x)  # [B, T, 3D]
        q, k, v = qkv.split(D, dim=-1)

        def split_heads(t: torch.Tensor) -> torch.Tensor:
            return t.view(B, T, self.n_heads, self.d_head).transpose(1, 2)  # [B, H, T, Dh]

        qh = split_heads(q)
        kh = split_heads(k)
        vh = split_heads(v)

        scores = (qh @ kh.transpose(-2, -1)) / (self.d_head**0.5)  # [B, H, T, T]
        w = torch.softmax(scores, dim=-1)
        out = w @ vh  # [B, H, T, Dh]
        out = out.transpose(1, 2).contiguous().view(B, T, D)  # [B, T, D]
        return self.proj(out)


x = torch.randn(2, 5, 32)
mha = MultiHeadAttention(d_model=32, n_heads=4)
y = mha(x)
print(y.shape)
```

## Exercise 5: Parameter Count Spot Check

Approximate counts:

- QKV + output projections: `4 * D * D` (ignoring biases)
- MLP: `D*(4D) + (4D)*D = 8*D*D`

So a block is roughly `12*D*D` parameters (plus layer norms and biases).

