# Exercises: 4.3 CNNs & Computer Vision

Prerequisite (recommended):

```bash
uv sync --frozen --extra dl
```

Use digits (8x8) offline to keep iteration fast.

## Exercise 1: Convolution Output Shapes

Given an input image size `(H, W) = (8, 8)` and a conv layer with:
- kernel `k=3`, stride `s=1`, padding `p=1`

Compute output `(H_out, W_out)`.

Then compute output after a `2x2` max-pool with stride `2`.

Expected outcome:
- you can derive the shape formula and apply it.

## Exercise 2: Train a Tiny CNN on Digits

Implement a CNN:
- `Conv2d(1, 16, 3, padding=1) -> ReLU -> MaxPool2d(2)`
- `Conv2d(16, 32, 3, padding=1) -> ReLU -> MaxPool2d(2)`
- linear classifier head

Expected outcome:
- test accuracy above a simple baseline (often > 0.95 for digits with a small CNN).

## Exercise 3: “Freeze Layers” Sanity Check

Freeze all conv layers and train only the classifier head.

Expected outcome:
- conv parameters do not receive gradients (`param.grad is None` or stays zero).

## Exercise 4: Robust Inference Function

Write `predict_topk(model, x, k=3)` that:
- accepts a single image tensor `(1, H, W)` or a batch `(B, 1, H, W)`,
- returns top-k class indices and probabilities.

Expected outcome:
- function works for both single and batch inputs.

## Exercise 5: CV Failure Modes Note

Write 6–10 lines answering:
- why train/test leakage is common in vision datasets,
- one augmentation that can hurt performance if misapplied,
- one deployment pitfall (lighting/camera domain shift).

