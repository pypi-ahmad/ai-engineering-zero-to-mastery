# Solutions: 5.1 Classical Deep Generative Models

## Exercise 1: VAE Loss Terms (Correctness)

```python
from __future__ import annotations

import torch
import torch.nn.functional as F


def vae_loss(
    logits: torch.Tensor,
    x: torch.Tensor,
    mu: torch.Tensor,
    logvar: torch.Tensor,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    recon = F.binary_cross_entropy_with_logits(logits, x, reduction="sum")
    kl = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
    total = recon + kl
    return total, recon, kl
```

## Exercise 2: Train VAE on Digits (Small)

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

idx_train, _idx_test = train_test_split(
    np.arange(len(X)), test_size=0.2, random_state=SEED, stratify=y
)
X_train = torch.from_numpy(X[idx_train]).unsqueeze(1)  # [N, 1, 8, 8]

ds = TensorDataset(X_train, torch.from_numpy(y[idx_train]))
loader = DataLoader(ds, batch_size=128, shuffle=True)

INPUT_DIM = 8 * 8
LATENT = 16


class VAE(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.enc = nn.Sequential(nn.Linear(INPUT_DIM, 128), nn.ReLU(), nn.Linear(128, 128), nn.ReLU())
        self.mu = nn.Linear(128, LATENT)
        self.logvar = nn.Linear(128, LATENT)
        self.dec = nn.Sequential(nn.Linear(LATENT, 128), nn.ReLU(), nn.Linear(128, 128), nn.ReLU(), nn.Linear(128, INPUT_DIM))

    def forward(self, x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        h = self.enc(x)
        mu = self.mu(h)
        logvar = self.logvar(h)
        std = torch.exp(0.5 * logvar)
        z = mu + std * torch.randn_like(std)
        logits = self.dec(z)
        return logits, mu, logvar


model = VAE()
opt = torch.optim.Adam(model.parameters(), lr=1e-3)

for _epoch in range(8):
    model.train()
    for xb, _ in loader:
        x_flat = xb.view(xb.size(0), -1)
        logits, mu, logvar = model(x_flat)
        loss, _recon, _kl = vae_loss(logits, x_flat, mu, logvar)
        opt.zero_grad()
        loss.backward()
        opt.step()

with torch.no_grad():
    z = torch.randn(32, LATENT)
    samples = torch.sigmoid(model.dec(z)).view(-1, 1, 8, 8)
print(samples.shape)
```

## Exercise 3: GAN One-Step Sanity

```python
from __future__ import annotations

import torch
from torch import nn

LATENT = 32
INPUT_DIM = 64


class G(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.net = nn.Sequential(nn.Linear(LATENT, 128), nn.ReLU(), nn.Linear(128, INPUT_DIM), nn.Tanh())

    def forward(self, z: torch.Tensor) -> torch.Tensor:
        return self.net(z)


class D(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.net = nn.Sequential(nn.Linear(INPUT_DIM, 128), nn.LeakyReLU(0.2), nn.Linear(128, 1))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


g = G()
d = D()
opt_g = torch.optim.Adam(g.parameters(), lr=1e-3)
opt_d = torch.optim.Adam(d.parameters(), lr=1e-3)
bce = nn.BCEWithLogitsLoss()

real = torch.randn(64, INPUT_DIM)  # toy "real" data
z = torch.randn(64, LATENT)
fake = g(z).detach()

# D step
opt_d.zero_grad()
loss_d = bce(d(real), torch.ones(64, 1)) + bce(d(fake), torch.zeros(64, 1))
loss_d.backward()
opt_d.step()

# G step
opt_g.zero_grad()
z = torch.randn(64, LATENT)
fake2 = g(z)
loss_g = bce(d(fake2), torch.ones(64, 1))
loss_g.backward()
opt_g.step()

print(float(loss_d), float(loss_g))
```

## Exercise 4: Diversity Metric (Mode Collapse Hint)

```python
import torch


def batch_diversity(x: torch.Tensor) -> float:
    # x: [B, D]
    return float(x.var(dim=0).mean())


samples = torch.randn(64, 64)
print(batch_diversity(samples))
```

## Exercise 5: Synthetic Data Risk Note

Minimum points:
- validate utility on a heldout real dataset,
- check privacy leakage (membership inference style thinking),
- check bias amplification and coverage gaps,
- require monitoring once deployed.

