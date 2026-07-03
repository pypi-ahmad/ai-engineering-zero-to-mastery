# Exercises: 6.1 MLOps Fundamentals & Lifecycle

These are offline-first and focus on lifecycle discipline: reproducibility, metadata, and clear boundaries.

## Exercise 1: Run Metadata (Reproducibility)

Create a function `make_run_metadata()` that captures:
- timestamp,
- python version,
- git commit hash (if available),
- dataset id/version string,
- model type,
- key hyperparameters.

Expected outcome:
- metadata is saved as JSON next to your artifact.

## Exercise 2: “Pipeline as Functions” (Idempotent)

Implement a 3-step pipeline:
- `ingest()` -> returns a DataFrame,
- `train(df)` -> returns a fitted model,
- `evaluate(model, df)` -> returns metrics dict.

Constraints:
- no hidden global state,
- rerunning does not depend on notebook order.

Expected outcome:
- you can call the pipeline from a single `main()` function.

## Exercise 3: Model Card (Minimal)

Write a minimal model card section including:
- intended use,
- data,
- metrics,
- limitations,
- monitoring plan.

Expected outcome:
- a teammate can understand what was shipped and what could go wrong.

## Exercise 4: Baseline + Regression Gate

Train a baseline model (e.g., logistic regression on breast cancer) and save:
- baseline metric(s),
- a “regression gate” threshold you would block releases on.

Expected outcome:
- you can justify the gate in terms of business risk.

## Exercise 5: Maturity Mapping

Write 6–10 lines mapping your current workflow to:
- Level 0 / 1 / 2 / 3 maturity (as described in the theory),
- the next most valuable improvement.

