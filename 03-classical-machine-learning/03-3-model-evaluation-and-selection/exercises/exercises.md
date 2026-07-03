# Exercises: 3.3 Model Evaluation & Selection

## Exercise 1: CV vs Single Split

On `load_breast_cancer`:

1. compute a single train/test split metric (accuracy),
2. compute 5-fold CV accuracy.

Expected outcome:
- you can explain why CV gives a more stable estimate.

## Exercise 2: Leakage-Safe Scaling in CV

Compare two approaches:

1. scaling then CV (wrong),
2. `Pipeline(StandardScaler(), LogisticRegression)` with CV (correct).

Expected outcome:
- you can explain why approach 1 leaks.

## Exercise 3: Simple Grid Search

Run `GridSearchCV` for random forest over:
- `n_estimators`
- `max_depth`

Report best params and best CV score.

Expected outcome:
- you can explain what the “best score” actually measures.

## Exercise 4: Metric Choice (Imbalanced)

Create an imbalanced dataset and compare:
- accuracy
- F1
- ROC AUC

Expected outcome:
- you can justify which metric to optimize for a “rare positive” use-case.

## Exercise 5: Model Selection Decision Note

Write a short decision memo (8–12 lines):
- the baseline,
- what you tried,
- what improved,
- what you would ship today and why,
- what you would monitor after shipping.

