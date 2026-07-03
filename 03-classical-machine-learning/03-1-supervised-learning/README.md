# 3.1 Supervised Learning

This lesson covers regression and classification workflows, including classical baselines and ensemble methods.

## Why This Matters

Supervised learning is the baseline skill behind most production ML: risk scoring, ranking, forecasting, and classification. Even if you later use deep learning or LLMs, you still need strong baselines and evaluation discipline.

## Learning Goals
- Distinguish supervised regression vs classification formally.
- Train and compare linear models, tree models, and ensemble variants.
- Interpret trade-offs between performance, interpretability, and deployment cost.

## How It Fits in the Curriculum
Supervised learning is a core baseline capability reused in deep learning, MLOps, and domain AI applications.

## Key Terms (Plain English)

- **Regression**: predict a number (price, demand).
- **Classification**: predict a class/label (spam/not spam).
- **Baseline**: a simple first model that sets a reference point.
- **Ensemble**: combine multiple models (often improves performance).

## Start Here
1. Theory: `theory/03-1-supervised-learning.md`
2. Notebook: `notebooks/03-1-supervised-learning.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## Expected Outcomes

- You can train at least 2 different model families and compare them fairly.
- You can explain metric tradeoffs (precision/recall/F1/ROC AUC).
- You can identify when “simple model + clean data” beats a complex model.

## Verify Your Work

- Run the notebook from a clean kernel and reproduce the key plots/tables.
- Complete the exercises and add one extra comparison (e.g., logistic regression vs random forest).

## Common Mistakes

- Evaluating on the training set and believing the metric.
- Picking a model based only on accuracy without considering class imbalance.
- Forgetting to control randomness (seeds, splits) when comparing models.
