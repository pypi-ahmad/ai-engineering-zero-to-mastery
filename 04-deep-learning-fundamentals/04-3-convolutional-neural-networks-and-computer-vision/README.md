# 4.3 Convolutional Neural Networks & Computer Vision

Builds deep vision intuition: convolutions, pooling, feature hierarchies, transfer learning, and practical CV pipeline choices.

## Why This Matters

Computer vision is one of the highest-impact applied AI areas. CNNs and transfer learning teach patterns you’ll reuse in other domains: inductive bias, pretrained models, and data pipeline discipline.

## Key Terms (Plain English)

- **Convolution**: a sliding filter that detects local patterns.
- **Inductive bias**: assumptions that make learning easier (CNN locality).
- **Transfer learning**: start from a pretrained model and adapt to your task.

## Start Here

1. Theory: `theory/04-3-convolutional-neural-networks-and-computer-vision.md`
2. Notebook: `notebooks/04-3-convolutional-neural-networks-and-computer-vision.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## Outcomes

- Explain why convolutional inductive bias works for images.
- Compare CNN training from scratch vs transfer learning.
- Design a basic image classification workflow with deployment considerations.

## Verify Your Work

- Run the notebook from a clean kernel.
- Complete the exercises and compare scratch vs transfer learning behavior.

## Common Mistakes

- Training from scratch with too little data and expecting magic.
- Ignoring input normalization/preprocessing (hurts performance).
- Evaluating on data that leaked from training (e.g., duplicates).
