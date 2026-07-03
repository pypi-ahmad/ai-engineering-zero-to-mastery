# 3.3 Model Evaluation & Selection

This lesson focuses on selecting models rigorously with cross-validation, tuning strategies, and leakage-aware experimentation.

## Why This Matters

If evaluation is wrong, everything downstream is wrong: you’ll deploy models that fail in production. This sub-lesson teaches the discipline that makes ML trustworthy: splits, cross-validation, leakage checks, and metric choice tied to business risk.

## Learning Goals
- Design reliable train/validation/test workflows.
- Use cross-validation and search strategies for hyperparameter tuning.
- Align metric choice with business and risk constraints.

## How It Fits in the Curriculum
This is the decision-quality layer that connects model development to production readiness and later MLOps/LLMOps evaluation practices.

## Key Terms (Plain English)

- **Cross-validation (CV)**: repeated train/validate splits to estimate generalization more reliably.
- **Hyperparameter**: a configuration you set before training (not learned weights).
- **Leakage**: using information you won’t have at prediction time.
- **Calibration**: whether predicted probabilities match real frequencies.

## Start Here
1. Theory: `theory/03-3-model-evaluation-and-selection.md`
2. Notebook: `notebooks/03-3-model-evaluation-and-selection.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## Expected Outcomes

- You can choose an evaluation workflow appropriate for your data and risk.
- You can tune models without accidentally leaking test information.
- You can justify a metric choice (and threshold) in business terms.

## Verify Your Work

- Run the notebook from a clean kernel and confirm you understand each split.
- Complete the exercises and add one leakage check to your workflow.

## Common Mistakes

- Using the test set to pick hyperparameters.
- Reporting a single metric without context (class balance, cost of errors).
- Comparing models with different preprocessing or different splits.
