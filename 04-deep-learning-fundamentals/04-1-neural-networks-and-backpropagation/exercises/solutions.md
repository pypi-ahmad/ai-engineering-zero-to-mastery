# Solutions: 4.1 Neural Networks & Backpropagation

## Exercise 1: MLP Forward Pass (Shapes)

```python
from __future__ import annotations

import torch
from torch import nn


class MLP(nn.Module):
    def __init__(self, in_dim: int = 64, hidden: int = 128, out_dim: int = 10) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden),
            nn.ReLU(),
            nn.Linear(hidden, out_dim),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


B = 32
x = torch.randn(B, 64)
model = MLP()
logits = model(x)
print(x.shape, logits.shape)  # torch.Size([32, 64]) torch.Size([32, 10])
```

## Exercise 2: Gradient Check (Scalar)

```python
from __future__ import annotations

import torch


def f(w: torch.Tensor) -> torch.Tensor:
    return w**3 + 2 * w


def analytic_grad(w: float) -> float:
    return 3 * (w**2) + 2


def numerical_grad(w: float, eps: float = 1e-6) -> float:
    return ((w + eps) ** 3 + 2 * (w + eps) - ((w - eps) ** 3 + 2 * (w - eps))) / (2 * eps)


for w0 in [-2.0, -0.5, 0.0, 1.5, 3.0]:
    w = torch.tensor(w0, requires_grad=True)
    y = f(w)
    y.backward()
    print(
        w0,
        "analytic", analytic_grad(w0),
        "autograd", float(w.grad),
        "numeric", numerical_grad(w0),
    )
```

## Exercise 3: Train a Small MLP (Digits)

```python
from __future__ import annotations

import numpy as np
import torch
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


SEED = 42
rng = np.random.default_rng(SEED)
torch.manual_seed(SEED)

digits = load_digits()
X = digits.data.astype("float32") / 16.0  # [N, 64]
y = digits.target.astype("int64")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=SEED, stratify=y
)

train_ds = TensorDataset(torch.from_numpy(X_train), torch.from_numpy(y_train))
test_ds = TensorDataset(torch.from_numpy(X_test), torch.from_numpy(y_test))
train_loader = DataLoader(train_ds, batch_size=128, shuffle=True)
test_loader = DataLoader(test_ds, batch_size=256, shuffle=False)

model = nn.Sequential(nn.Linear(64, 128), nn.ReLU(), nn.Linear(128, 10))
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.CrossEntropyLoss()

for _epoch in range(10):
    model.train()
    for xb, yb in train_loader:
        logits = model(xb)
        loss = loss_fn(logits, yb)
        opt.zero_grad()
        loss.backward()
        opt.step()

model.eval()
correct = 0
total = 0
with torch.no_grad():
    for xb, yb in test_loader:
        pred = model(xb).argmax(dim=1)
        correct += int((pred == yb).sum())
        total += int(yb.numel())

acc = correct / total
print("test_acc", acc)
```

## Exercise 4: Loss Function Sanity

```python
import torch
from torch import nn

loss_fn = nn.CrossEntropyLoss()

logits = torch.tensor([[2.0, 0.0], [0.0, 2.0]])  # 2 examples, 2 classes
y = torch.tensor([0, 1])

# Correct: logits directly
loss_logits = float(loss_fn(logits, y))

# Wrong: softmax then CE (double-softmax effect; not equivalent)
probs = torch.softmax(logits, dim=1)
loss_probs = float(loss_fn(probs, y))

print(loss_logits, loss_probs)
```

## Exercise 5: Backprop Failure Modes Note

Key points:
- Exploding: gradients become huge, loss spikes/NaNs; mitigate with clipping, smaller LR, better init/normalization.
- Vanishing: gradients near zero, training stalls; mitigate with ReLU-like activations, residual connections, normalization, careful init.

