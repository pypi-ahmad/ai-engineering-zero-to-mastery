# Solutions: 4.2 Training Deep Neural Networks

Below is a compact training loop you can reuse for Exercises 1–5.

```python
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import torch
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


@dataclass(frozen=True)
class Split:
    train: TensorDataset
    val: TensorDataset
    test: TensorDataset


def make_splits(seed: int = 42) -> Split:
    digits = load_digits()
    X = digits.data.astype("float32") / 16.0
    y = digits.target.astype("int64")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=seed, stratify=y
    )
    X_tr, X_val, y_tr, y_val = train_test_split(
        X_train, y_train, test_size=0.2, random_state=seed, stratify=y_train
    )
    return Split(
        train=TensorDataset(torch.from_numpy(X_tr), torch.from_numpy(y_tr)),
        val=TensorDataset(torch.from_numpy(X_val), torch.from_numpy(y_val)),
        test=TensorDataset(torch.from_numpy(X_test), torch.from_numpy(y_test)),
    )


def accuracy(model: nn.Module, loader: DataLoader) -> float:
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for xb, yb in loader:
            pred = model(xb).argmax(dim=1)
            correct += int((pred == yb).sum())
            total += int(yb.numel())
    return correct / total


def train(
    model: nn.Module,
    train_loader: DataLoader,
    val_loader: DataLoader,
    lr: float,
    weight_decay: float = 0.0,
    epochs: int = 10,
    patience: int | None = None,
    seed: int = 42,
) -> tuple[list[float], float]:
    torch.manual_seed(seed)
    opt = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=weight_decay)
    loss_fn = nn.CrossEntropyLoss()

    best_acc = -1.0
    best_state: dict[str, torch.Tensor] | None = None
    bad_epochs = 0
    losses: list[float] = []

    for _epoch in range(epochs):
        model.train()
        running = 0.0
        n = 0
        for xb, yb in train_loader:
            logits = model(xb)
            loss = loss_fn(logits, yb)
            opt.zero_grad()
            loss.backward()
            opt.step()
            running += float(loss) * xb.size(0)
            n += xb.size(0)
        losses.append(running / n)

        val_acc = accuracy(model, val_loader)
        if val_acc > best_acc:
            best_acc = val_acc
            best_state = {k: v.detach().clone() for k, v in model.state_dict().items()}
            bad_epochs = 0
        else:
            bad_epochs += 1

        if patience is not None and bad_epochs >= patience:
            break

    if best_state is not None:
        model.load_state_dict(best_state)
    return losses, best_acc
```

## Exercise 1: Learning Rate Sweep

```python
splits = make_splits(seed=42)
train_loader = DataLoader(splits.train, batch_size=128, shuffle=True)
val_loader = DataLoader(splits.val, batch_size=256, shuffle=False)
test_loader = DataLoader(splits.test, batch_size=256, shuffle=False)

for lr in [1e-4, 1e-3, 1e-2]:
    model = nn.Sequential(nn.Linear(64, 128), nn.ReLU(), nn.Linear(128, 10))
    losses, best_val = train(model, train_loader, val_loader, lr=lr, epochs=5, seed=42)
    print(lr, "losses", [round(x, 4) for x in losses], "best_val", round(best_val, 4), "test", round(accuracy(model, test_loader), 4))
```

## Exercise 2: Weight Decay vs No Weight Decay

```python
for wd in [0.0, 1e-2]:
    model = nn.Sequential(nn.Linear(64, 128), nn.ReLU(), nn.Linear(128, 10))
    _, best_val = train(model, train_loader, val_loader, lr=1e-3, weight_decay=wd, epochs=10, seed=42)
    print("wd", wd, "best_val", best_val, "test", accuracy(model, test_loader))
```

## Exercise 3: Dropout Overfitting Check

```python
no_dropout = nn.Sequential(
    nn.Linear(64, 256), nn.ReLU(),
    nn.Linear(256, 128), nn.ReLU(),
    nn.Linear(128, 10),
)

with_dropout = nn.Sequential(
    nn.Linear(64, 256), nn.ReLU(), nn.Dropout(p=0.2),
    nn.Linear(256, 128), nn.ReLU(), nn.Dropout(p=0.2),
    nn.Linear(128, 10),
)

for name, m in [("no_dropout", no_dropout), ("with_dropout", with_dropout)]:
    _, best_val = train(m, train_loader, val_loader, lr=1e-3, epochs=12, seed=42)
    print(name, "best_val", best_val, "test", accuracy(m, test_loader))
```

## Exercise 4: Early Stopping (Patience)

```python
model = nn.Sequential(nn.Linear(64, 256), nn.ReLU(), nn.Linear(256, 10))
losses, best_val = train(model, train_loader, val_loader, lr=1e-3, epochs=50, patience=3, seed=42)
print("epochs_ran", len(losses), "best_val", best_val, "test", accuracy(model, test_loader))
```

## Exercise 5: Reproducibility Spot Check

```python
def run_once(seed: int) -> float:
    splits = make_splits(seed=seed)
    train_loader = DataLoader(splits.train, batch_size=128, shuffle=True)
    val_loader = DataLoader(splits.val, batch_size=256, shuffle=False)
    test_loader = DataLoader(splits.test, batch_size=256, shuffle=False)
    model = nn.Sequential(nn.Linear(64, 128), nn.ReLU(), nn.Linear(128, 10))
    train(model, train_loader, val_loader, lr=1e-3, epochs=8, seed=seed)
    return accuracy(model, test_loader)


print(run_once(42), run_once(42))
```

