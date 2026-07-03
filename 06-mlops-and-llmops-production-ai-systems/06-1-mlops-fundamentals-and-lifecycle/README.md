# 6.1 MLOps Fundamentals & Lifecycle

This sub-lesson introduces MLOps as an engineering discipline for production ML systems.

## Why This Matters

Without lifecycle discipline, teams can’t answer basic questions: “What model is deployed?”, “What data trained it?”, “Can we reproduce this metric?”, “How do we rollback safely?”

## Key Terms (Plain English)

- **Run metadata**: what code/data/config produced an artifact.
- **Artifact**: saved model/metrics/config you can reuse later.
- **Maturity level**: how repeatable and automated your ML delivery is.

## Start Here

1. `theory/06-1-mlops-fundamentals-and-lifecycle.md`
2. `notebooks/06-1-mlops-fundamentals-and-lifecycle-demo.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## Coverage

- MLOps lifecycle and maturity levels
- Team structures and delivery responsibilities
- CI/CD/CT/CM for machine learning systems
- Tooling landscape and common anti-patterns

## Verify Your Work

- Run the notebook from a clean kernel.
- Complete the exercises and save at least one JSON metadata file for a run.

## Common Mistakes

- Training “one-off” models with no saved config/metrics.
- Changing data/code without versioning, then guessing why quality changed.
