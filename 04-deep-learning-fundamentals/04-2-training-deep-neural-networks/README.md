# 4.2 Training Deep Neural Networks

Covers practical optimization and generalization mechanics: initialization, normalization, regularization, learning-rate schedules, and training diagnostics.

## Why This Matters

Most deep learning failure modes are training issues, not architecture issues. If you can read learning curves and understand optimization knobs, you can fix models faster and avoid shipping unstable systems.

## Key Terms (Plain English)

- **Regularization**: techniques that reduce overfitting (weight decay, dropout).
- **Normalization**: stabilizes training (batch norm, layer norm).
- **Learning-rate schedule**: changes step size over time.

## Start Here

1. Theory: `theory/04-2-training-deep-neural-networks.md`
2. Notebook: `notebooks/04-2-training-deep-neural-networks.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## Outcomes

- Diagnose underfitting/overfitting with training curves.
- Choose practical optimization settings for stable convergence.
- Apply regularization and monitoring patterns used in production teams.

## Verify Your Work

- Run the notebook from a clean kernel and reproduce the learning curve behavior.
- Complete the exercises and explain one training failure mode you observed.

## Common Mistakes

- Changing multiple knobs at once (hard to know what helped).
- Comparing runs without fixed seeds/splits.
- Using “final accuracy” without looking at curves and instability.
