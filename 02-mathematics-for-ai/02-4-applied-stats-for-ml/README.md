# 2.4 Applied Stats for ML

This lesson turns statistics into applied model diagnostics and selection decisions.

## Why This Matters

This is where statistics becomes engineering: you learn how to trust metrics, compare models fairly, and avoid deploying models that “look good” but fail on real data.

## Learning Goals
- Diagnose bias/variance, overfitting, and underfitting.
- Choose metrics aligned with business risk (classification and regression).
- Use train/validation/test splits and cross-validation correctly.

## How It Fits in the Curriculum
This bridges mathematical theory to practical model evaluation workflows used heavily in Lesson 3 and production lessons.

## Key Terms (Plain English)

- **Bias/variance**: underfitting vs sensitivity to data (overfitting risk).
- **Cross-validation**: repeated splits to estimate generalization.
- **Threshold**: decision cutoff for classification probabilities.

## Start Here
1. Theory: `theory/02-4-applied-stats-for-ml-iris.md`
2. Notebook: `notebooks/02-4-applied-stats-for-ml-iris.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## Expected Outcomes

- You can explain and diagnose overfitting vs underfitting.
- You can choose a metric and threshold appropriate for a cost tradeoff.
- You can design a safe evaluation split and avoid leakage.

## Verify Your Work

- Run the notebook from a clean kernel.
- Complete the exercises and write a “metric choice note” for one task.

## Common Mistakes

- Optimizing a metric that doesn’t match the real objective.
- Using the test set to pick a model.
