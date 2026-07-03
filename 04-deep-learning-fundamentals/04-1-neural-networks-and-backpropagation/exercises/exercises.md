# Exercises: 4.1 Neural Networks & Backpropagation

Prerequisite (recommended):

```bash
uv sync --frozen --extra dl
```

Use `sklearn.datasets.load_digits` for offline runs (8x8 images).

## Exercise 1: MLP Forward Pass (Shapes)

Build a 2-layer MLP in PyTorch and verify:

- input batch shape is `(B, 64)` for digits,
- output logits shape is `(B, 10)`.

Expected outcome:
- your forward pass runs without shape errors.

## Exercise 2: Gradient Check (Scalar)

For a scalar function:

$$
f(w) = (w^3 + 2w)
$$

Compute:
- analytic derivative,
- PyTorch autograd derivative,
- numerical derivative (central difference).

Expected outcome:
- all three are close at several values of `w`.

## Exercise 3: Train a Small MLP (Digits)

Train a small MLP on digits with:
- train/test split with stratification,
- fixed seed,
- cross-entropy loss.

Expected outcome:
- test accuracy above a simple baseline (e.g., > 0.90 is typical for a small MLP).

## Exercise 4: Loss Function Sanity

Show that:
- `CrossEntropyLoss` expects raw logits (no softmax),
- applying softmax before `CrossEntropyLoss` is a common mistake.

Expected outcome:
- you can demonstrate the difference on a tiny batch and explain why it matters.

## Exercise 5: Backprop Failure Modes Note

Write 6–10 lines answering:
- what exploding gradients look like,
- what vanishing gradients look like,
- one mitigation for each.

