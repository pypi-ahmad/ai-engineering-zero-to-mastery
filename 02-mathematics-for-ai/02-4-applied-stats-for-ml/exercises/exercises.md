# Exercises: 2.4 Applied Stats for ML

## Exercise 1: Split Discipline (No Leakage)

Using `sklearn.datasets.load_iris(as_frame=True)`:

1. Make train/test split.
2. Fit a scaler **only on train**.
3. Train logistic regression on scaled train.
4. Evaluate accuracy on scaled test.

Expected outcome:
- you can explain where leakage would occur if you scaled before splitting.

## Exercise 2: Accuracy vs F1 on Imbalanced Data

Use `sklearn.datasets.make_classification` to generate a dataset with class imbalance (e.g., 95/5).

Train a baseline classifier and compute:
- accuracy
- precision
- recall
- F1

Expected outcome:
- you can show a case where accuracy looks “good” but recall is poor.

## Exercise 3: Cross-Validation Comparison

Compare two models with 5-fold CV on the same dataset:

- logistic regression
- random forest

Expected outcome:
- report mean and std of a metric (e.g., accuracy or ROC AUC).

## Exercise 4: Confidence Interval for Mean (Bootstrap)

Generate a sample of `n=200` numbers and compute a bootstrap 95% CI for the mean.

Expected outcome:
- CI width shrinks if you increase `n`.

## Exercise 5: Threshold Tradeoff Note

Write a short note answering:
- what changes when you move the classification threshold from 0.5 to 0.8,
- why thresholds depend on business cost, not just model metrics.

