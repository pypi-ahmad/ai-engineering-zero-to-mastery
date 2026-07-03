# Solutions: 4.3 CNNs & Computer Vision

## Exercise 1: Convolution Output Shapes

For conv:

$$
H_{out} = \\left\\lfloor \\frac{H + 2p - k}{s} \\right\\rfloor + 1
$$

With `H=8, k=3, s=1, p=1`, output is `8`. Same for `W`.

After `2x2` max-pool with stride 2: `8 -> 4`.

## Exercise 2: Train a Tiny CNN on Digits

```python
from __future__ import annotations

import numpy as np
import torch
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

SEED = 42
torch.manual_seed(SEED)

digits = load_digits()
X = (digits.images.astype("float32") / 16.0)  # [N, 8, 8]
y = digits.target.astype("int64")

idx_train, idx_test = train_test_split(
    np.arange(len(X)), test_size=0.2, random_state=SEED, stratify=y
)
X_train = torch.from_numpy(X[idx_train]).unsqueeze(1)
X_test = torch.from_numpy(X[idx_test]).unsqueeze(1)
y_train = torch.from_numpy(y[idx_train])
y_test = torch.from_numpy(y[idx_test])

train_loader = DataLoader(TensorDataset(X_train, y_train), batch_size=128, shuffle=True)
test_loader = DataLoader(TensorDataset(X_test, y_test), batch_size=256, shuffle=False)


class TinyCNN(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 16, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(16, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.head = nn.Linear(32 * 2 * 2, 10)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        h = self.features(x)
        h = h.view(h.size(0), -1)
        return self.head(h)


model = TinyCNN()
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.CrossEntropyLoss()

for _epoch in range(12):
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

print("test_acc", correct / total)
```

## Exercise 3: “Freeze Layers” Sanity Check

```python
for p in model.features.parameters():
    p.requires_grad = False

opt = torch.optim.Adam(model.head.parameters(), lr=1e-3)

xb, yb = next(iter(train_loader))
loss = loss_fn(model(xb), yb)
opt.zero_grad()
loss.backward()

any_feature_grads = any(p.grad is not None for p in model.features.parameters())
any_head_grads = any(p.grad is not None for p in model.head.parameters())
print("feature_grads?", any_feature_grads, "head_grads?", any_head_grads)
```

## Exercise 4: Robust Inference Function

```python
from __future__ import annotations

import torch


@torch.no_grad()
def predict_topk(model: torch.nn.Module, x: torch.Tensor, k: int = 3) -> tuple[torch.Tensor, torch.Tensor]:
    model.eval()
    if x.ndim == 3:
        x = x.unsqueeze(0)  # [1, 1, H, W]
    logits = model(x)
    probs = torch.softmax(logits, dim=1)
    top_p, top_i = torch.topk(probs, k=k, dim=1)
    return top_i, top_p
```

## Exercise 5: CV Failure Modes Note

Typical points:
- Leakage: near-duplicates across splits, same subject appears in train and test, augmentations applied before splitting.
- Bad augmentation: label-changing transforms (e.g., heavy rotation when orientation matters).
- Deployment pitfall: camera/lighting changes shift pixel statistics; add monitoring and recalibration strategy.

