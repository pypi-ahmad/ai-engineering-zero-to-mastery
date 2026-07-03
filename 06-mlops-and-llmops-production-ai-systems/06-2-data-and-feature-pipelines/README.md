# 6.2 Data & Feature Pipelines

This sub-lesson covers production-grade data and feature engineering pipelines.

## Why This Matters

Most production failures come from data problems, not model code. If your pipeline is not validated, versioned, and leakage-safe, model metrics will lie and deployments will be brittle.

## Key Terms (Plain English)

- **Schema**: expected columns/types.
- **Point-in-time join**: joining features without using “future” information (prevents leakage).
- **Offline/online consistency**: same feature logic in training and serving.

## Start Here

1. `theory/06-2-data-and-feature-pipelines.md`
2. `notebooks/06-2-data-and-feature-pipelines-demo.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## Coverage

- Batch and streaming pipeline patterns
- Feature store concepts and point-in-time correctness
- Data quality gates and schema management
- Offline/online feature consistency challenges

## Verify Your Work

- Run the notebook from a clean kernel.
- Complete the exercises, especially point-in-time joins and dataset fingerprinting.

## Common Mistakes

- Building features with future information (silent leakage).
- Different preprocessing in training vs serving (offline/online skew).
