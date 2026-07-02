# Overview

Supervised learning maps labeled inputs to outputs. Given dataset $D=\{(x_i,y_i)\}_{i=1}^n$, model learns function $f_	heta(x)$ minimizing expected loss.

Two major task families:
- **Regression:** target is continuous.
- **Classification:** target is categorical.

# Regression vs Classification

## Regression
Predict real-valued quantity, e.g., house price.
Typical losses: MSE, MAE.

## Classification
Predict class label/probability, e.g., fraud vs non-fraud.
Typical losses: log loss (cross-entropy).

# Core Model Families

## Linear Regression
Assumes linear relation:
$$\hat{y}=w^Tx+b$$
Fast, interpretable, strong baseline for regression.

## Logistic Regression
Models class probability:
$$P(y=1|x)=\sigma(w^Tx+b)$$
where $\sigma$ is sigmoid. Despite name, used for classification.

## k-Nearest Neighbors
Prediction from nearby samples in feature space. Non-parametric, sensitive to scaling and high dimensions.

## Decision Trees
Recursive feature splits minimizing impurity (classification) or variance (regression). Interpretable but can overfit.

# Ensemble Methods

## Bagging
Train multiple base models on bootstrapped samples and aggregate predictions. Reduces variance.

## Random Forests
Bagging of decision trees + random feature subsets per split. Usually strong default for tabular data.

## Boosting
Sequentially add weak learners to correct predecessor errors. Reduces bias and can model complex patterns.

## Gradient Boosting
Builds additive model by fitting learners to negative gradients of loss function.

## XGBoost
Optimized gradient boosting with regularization, shrinkage, and system-level efficiency (parallelism, sparsity-aware handling).

# Model Selection Tradeoffs

- Linear models: fast, interpretable, may underfit non-linear patterns.
- Random forests: robust, less tuning, larger memory.
- Gradient boosting/XGBoost: high performance on tabular data, careful tuning needed.
- k-NN: simple, expensive inference at scale.

# Business Case Studies & Exceptions

## Case 1: Credit Scoring Classification
Regulatory need for interpretability favored logistic regression baseline. Ensemble models improved AUC but required explainability overlays.

## Case 2: House Price Regression
Linear model underfit neighborhood interactions; gradient boosting captured non-linearities and reduced error.

## Case 3: High-Cardinality Features
Tree ensembles overfit sparse IDs without proper encoding and regularization.

# Interview Questions & Answers

1. **Q: Define supervised learning.**  
   **A:** Learning mapping from labeled input-output pairs to generalize on unseen inputs.

2. **Q: Regression vs classification?**  
   **A:** Regression predicts continuous values; classification predicts categories/probabilities.

3. **Q: What is bagging?**  
   **A:** Bootstrap aggregating: train models on resampled data and aggregate outputs.

4. **Q: What is boosting?**  
   **A:** Sequentially train models where each focuses on previous errors.

5. **Q: Random Forest vs Gradient Boosting?**  
   **A:** RF reduces variance via independent trees; GB reduces bias via sequential corrections.

6. **Q: Why XGBoost often strong on tabular data?**  
   **A:** Regularized boosting, efficient implementation, and flexible objective/feature handling.

7. **Q: When prefer linear model over ensemble?**  
   **A:** Need interpretability, low latency, small data, or simple relationships.

8. **Q: Main risk with boosting?**  
   **A:** Overfitting and sensitivity to hyperparameters if unchecked.

9. **Q: Why feature scaling matters for k-NN/logistic?**  
   **A:** Distance/gradient behavior depends on feature magnitudes.

10. **Q: Baseline role in supervised projects?**  
    **A:** Establish reference performance before complex models.
