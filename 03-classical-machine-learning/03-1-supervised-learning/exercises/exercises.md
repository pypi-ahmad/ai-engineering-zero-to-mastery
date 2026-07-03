# Exercises: 3.1 Supervised Learning

All exercises should be runnable offline using sklearn built-in datasets.

## Exercise 1: Baseline Classifier (Breast Cancer)

Use `sklearn.datasets.load_breast_cancer(as_frame=True)` and:

1. create train/test split with stratification,
2. train logistic regression,
3. report accuracy and ROC AUC on test.

Expected outcome:
- you can explain why ROC AUC can be more informative than accuracy.

## Exercise 2: Model Comparison (Simple)

Train and compare:
- logistic regression
- random forest

Report:
- accuracy
- precision/recall/F1

Expected outcome:
- you can explain one reason the models might differ.

## Exercise 3: Pipeline (No Leakage)

Build a `Pipeline` that includes:
- `StandardScaler`
- logistic regression

Expected outcome:
- your workflow never fits scaling on test data.

## Exercise 4: Missing Values Handling

Create a copy of `X` and randomly set 5% of entries to missing.

Then build a pipeline with:
- `SimpleImputer(strategy=\"median\")`
- `StandardScaler`
- logistic regression

Expected outcome:
- pipeline trains without errors and metrics are reasonable.

## Exercise 5: Feature Importance (Permutation)

Compute permutation feature importance for the trained model.

Expected outcome:
- you can name the top 3 features and explain what “importance” does and does not mean.

