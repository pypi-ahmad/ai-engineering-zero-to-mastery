# Solutions: 5.5 LLM Post-Training & Fine-Tuning

## Exercise 1: Decision Checklist (Prompt vs RAG vs Fine-Tune)

Minimum points:
- Prompting: best for instruction/control; fails with factuality/grounding and long-tail formats; eval with format + task accuracy.
- RAG: best when you need up-to-date/grounded info; fails with retrieval quality; eval with recall@k + answer groundedness.
- Fine-tune: best when behavior must be consistent; fails with overfitting/catastrophic forgetting; eval before/after on a fixed set.

## Exercise 2–5: Toy LoRA Implementation + Training + Save/Load

```python
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


class LoRALinear(nn.Module):
    def __init__(self, base: nn.Linear, r: int = 4, alpha: float = 8.0) -> None:
        super().__init__()
        self.base = base
        for p in self.base.parameters():
            p.requires_grad = False

        in_dim = base.in_features
        out_dim = base.out_features
        self.r = r
        self.alpha = alpha
        # A: [r, in], B: [out, r]
        self.A = nn.Parameter(torch.zeros(r, in_dim))
        self.B = nn.Parameter(torch.zeros(out_dim, r))
        nn.init.normal_(self.A, std=0.02)
        nn.init.zeros_(self.B)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        base_out = self.base(x)
        update = (x @ self.A.t()) @ self.B.t()  # [B, out]
        return base_out + (self.alpha / self.r) * update

    def lora_state_dict(self) -> dict[str, torch.Tensor]:
        return {"A": self.A.detach().cpu(), "B": self.B.detach().cpu()}

    def load_lora_state_dict(self, state: dict[str, torch.Tensor]) -> None:
        self.A.data.copy_(state["A"])
        self.B.data.copy_(state["B"])


def make_toy(seed: int = 42, n: int = 2000, d: int = 16) -> tuple[TensorDataset, TensorDataset]:
    rng = np.random.default_rng(seed)
    w = rng.normal(size=(d,))
    X = rng.normal(size=(n, d)).astype("float32")
    y = (X @ w > 0).astype("int64")
    idx = rng.permutation(n)
    split = int(0.8 * n)
    tr, te = idx[:split], idx[split:]
    ds_tr = TensorDataset(torch.from_numpy(X[tr]), torch.from_numpy(y[tr]))
    ds_te = TensorDataset(torch.from_numpy(X[te]), torch.from_numpy(y[te]))
    return ds_tr, ds_te


@torch.no_grad()
def acc(model: nn.Module, loader: DataLoader) -> float:
    model.eval()
    correct = 0
    total = 0
    for xb, yb in loader:
        pred = model(xb).argmax(dim=1)
        correct += int((pred == yb).sum())
        total += int(yb.numel())
    return correct / total


ds_tr, ds_te = make_toy()
tr = DataLoader(ds_tr, batch_size=128, shuffle=True)
te = DataLoader(ds_te, batch_size=256, shuffle=False)

# Base model
torch.manual_seed(42)
base = nn.Linear(16, 2)

# 1) LoRA adapter on frozen base
model_lora = nn.Sequential(LoRALinear(base, r=4, alpha=8.0))
opt = torch.optim.Adam([p for p in model_lora.parameters() if p.requires_grad], lr=1e-2)
loss_fn = nn.CrossEntropyLoss()

for _epoch in range(10):
    model_lora.train()
    for xb, yb in tr:
        logits = model_lora(xb)
        loss = loss_fn(logits, yb)
        opt.zero_grad()
        loss.backward()
        opt.step()

print("lora acc", acc(model_lora, te))

# 2) Save and reload adapter weights
artifact = Path("artifacts/lora_toy")
artifact.mkdir(parents=True, exist_ok=True)
state = model_lora[0].lora_state_dict()
torch.save(state, artifact / "lora.pt")

base2 = nn.Linear(16, 2)
base2.load_state_dict(base.state_dict())
fresh = LoRALinear(base2, r=4, alpha=8.0)
fresh.load_lora_state_dict(torch.load(artifact / "lora.pt", map_location="cpu"))

reloaded = nn.Sequential(fresh)
print("reloaded acc", acc(reloaded, te))
```

