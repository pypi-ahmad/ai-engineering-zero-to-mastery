# Exercises: 4.2 Training Deep Neural Networks

Prerequisite (recommended):

```bash
uv sync --frozen --extra dl
```

Use digits (offline) so you can iterate fast.

## Exercise 1: Learning Rate Sweep

Train the same small MLP with learning rates:
- `1e-4`, `1e-3`, `1e-2`

Track training loss for 5 epochs and compare.

Expected outcome:
- you can identify “too slow” vs “unstable” learning rates.

## Exercise 2: Weight Decay vs No Weight Decay

Train two models:
- Adam with `weight_decay=0.0`
- Adam with `weight_decay=1e-2`

Expected outcome:
- you can explain how weight decay affects generalization.

## Exercise 3: Dropout Overfitting Check

Train:
- a slightly larger MLP without dropout,
- the same MLP with dropout (e.g., `p=0.2`).

Expected outcome:
- you can observe and explain a train-vs-test gap change.

## Exercise 4: Early Stopping (Patience)

Implement early stopping with:
- validation split from train,
- patience (e.g., 3 epochs),
- best checkpoint restore.

Expected outcome:
- training stops early on plateau and returns best model weights.

## Exercise 5: Reproducibility Spot Check

Run the same training twice with the same seed.

Expected outcome:
- metrics match exactly on CPU (or are extremely close), and you can list reasons GPU runs may differ.

