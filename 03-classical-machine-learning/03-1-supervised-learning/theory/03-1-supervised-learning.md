# Overview

Supervised learning fits a mapping from inputs to known targets using labeled data:
$$
D = \{(x_i, y_i)\}_{i=1}^{n}
$$
The objective is to learn a function $f_\theta(x)$ that generalizes to unseen samples by minimizing expected loss.

In production terms, supervised learning is a contract between historical labeled outcomes and future decision quality. The challenge is not just fitting the training set; it is preserving performance when data shifts, business rules evolve, and inference latency constraints apply. This is why model family selection should include operational characteristics (interpretability, retraining cost, stability) in addition to offline metrics.

# Regression vs Classification

## Formal Definitions

- **Supervised learning:** learning from input-output pairs where targets are available during training.
- **Regression:** target $y \in \mathbb{R}$ (continuous).
- **Classification:** target $y \in \{1,\dots,K\}$ (categorical classes).

## Regression

Model predicts continuous quantity (house price, demand, revenue).

Common losses:
- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)

## Classification

Model predicts class labels or probabilities.

Common losses:
- Log loss / cross-entropy

Output interpretation:
- Class label for decisions
- Probability for threshold-based risk actions

# Core Model Families

## Linear Regression

Model:
$$
\hat{y} = w^T x + b
$$

Pros:
- Interpretable baseline
- Fast to train/infer

Limitations:
- Underfits nonlinear patterns without feature engineering

## Logistic Regression

Binary class probability:
$$
P(y=1|x) = \sigma(w^T x + b)
$$
where $\sigma$ is sigmoid.

Pros:
- Strong calibrated baseline (with proper regularization/calibration)
- Interpretable coefficients

## k-Nearest Neighbors (k-NN)

Prediction based on nearby training points in feature space.

Pros:
- Simple, non-parametric

Limitations:
- Inference can be slow at scale
- Sensitive to feature scaling and high dimension

## Decision Trees

Recursive feature splits minimizing impurity (classification) or variance (regression).

Pros:
- Handles nonlinear interactions
- Easy to inspect

Limitations:
- High variance, can overfit if unconstrained

# Ensemble Methods

According to scikit-learn ensemble guidance, ensemble models combine multiple base estimators to improve robustness/generalization over single estimators.

## Bagging

Formal idea:
Train base estimators on bootstrapped samples and aggregate predictions.

- Classification aggregation: voting / averaged probabilities
- Regression aggregation: averaging

Primary effect:
- Reduces variance

## Random Forests

Random Forest is bagging with randomized feature subsets at split time.

Per scikit-learn docs, random forests fit many decision trees on sub-samples and use averaging to improve predictive accuracy and control overfitting.

Typical strengths:
- Strong default for tabular data
- Lower tuning burden than boosting

Tradeoffs:
- Larger memory footprint
- Less calibrated probabilities by default

## Boosting

Formal idea:
Build learners sequentially so each stage corrects residual errors from prior stages.

Primary effect:
- Reduces bias and builds strong predictive performance

## Gradient Boosting

Per scikit-learn docs, Gradient Boosting builds an additive model in forward stage-wise fashion and optimizes differentiable loss; each stage fits a learner to negative gradients.

Typical strengths:
- High accuracy on structured/tabular data
- Captures nonlinear interactions

Tradeoffs:
- More hyperparameter-sensitive than bagging
- Slower training than many linear methods

## XGBoost

XGBoost is an optimized gradient boosting system with regularization and system-level efficiency improvements.

From XGBoost docs, key parameters include:
- `eta` / `learning_rate`: shrinkage step size
- `gamma`: minimum loss reduction for split
- `max_depth`: max tree depth
- `min_child_weight`: minimum Hessian/instance weight in child
- `subsample`, `colsample_bytree`: row/feature subsampling
- `reg_alpha`, `reg_lambda`: L1/L2 regularization

Typical strengths:
- Excellent tabular performance
- Fine-grained regularization controls

Tradeoffs:
- More tuning complexity
- Requires careful validation to avoid leaderboard overfitting

# Model Selection Tradeoffs

| Model family | Best fit scenarios | Strengths | Risks |
|---|---|---|---|
| Linear/Logistic | Need interpretability, fast baseline | Fast, stable, explainable | Underfitting nonlinear patterns |
| k-NN | Small datasets, local structure | Simple, intuitive | Slow inference, scale sensitivity |
| Decision Tree | Rule-like interactions | Interpretable nonlinear splits | Overfitting if deep |
| Random Forest | Tabular baseline with low tuning budget | Robust, variance reduction | Larger models, weaker calibration |
| Gradient Boosting | High-performance tabular modeling | Strong accuracy, interaction capture | Hyperparameter sensitivity |
| XGBoost | Competitive tabular optimization | Regularized powerful boosting | Complexity, tuning overhead |

Practical selection workflow:
1. Start with interpretable baseline (linear/logistic or shallow tree).
2. Compare against one bagging and one boosting model using consistent splits.
3. Evaluate calibration and threshold behavior for business decision points.
4. Choose the simplest model that clears target KPI and operational constraints.

# Business Case Studies & Exceptions

## Case 1: Credit Scoring Classification

Scenario:
Regulated lending requires both strong discrimination and explainability.

Pattern:
- Start with logistic regression baseline for governance.
- Evaluate tree ensembles for incremental lift.
- Add explainability/calibration layer if ensemble adopted.

Exception:
If policy requires transparent adverse-action reason codes, simpler interpretable models may be preferred despite small metric loss.

## Case 2: House Price Regression

Scenario:
Linear model underfits location-feature interactions.

Pattern:
- Compare linear baseline vs random forest vs gradient boosting/XGBoost.
- Inspect residuals by neighborhood segment.
- Choose model balancing accuracy and maintainability.

## Case 3: High-Cardinality Features and Leakage Risk

Scenario:
Entity IDs leak memorized behavior in tree ensembles.

Pattern:
- Use leakage-safe encoding and strict split strategy.
- Validate on time-aware holdout where relevant.

# Interview Questions & Answers

1. **Q: Define bagging and boosting.**
   **A:** Bagging trains models in parallel on bootstrapped data and aggregates outputs (variance reduction). Boosting trains sequentially to correct prior errors (bias reduction).

2. **Q: Random Forest vs Gradient Boosting?**
   **A:** Random Forest averages many randomized trees for robustness; Gradient Boosting adds trees sequentially to optimize residual loss.

3. **Q: Random Forest vs XGBoost?**
   **A:** RF is simpler and robust with low tuning; XGBoost is often more accurate on tabular data but more sensitive to hyperparameters and setup.

4. **Q: When prefer linear models over ensembles?**
   **A:** Strong interpretability/governance needs, low-latency constraints, or when nonlinear lift is minimal.

5. **Q: Why is baseline model mandatory?**
   **A:** Baselines anchor complexity and quantify whether advanced models provide meaningful lift.

6. **Q: What does learning rate do in boosting?**
   **A:** Controls contribution of each tree; lower values usually require more trees and can improve generalization.

7. **Q: Why can boosting overfit?**
   **A:** Excessive depth/rounds or weak regularization can fit noise.

8. **Q: Why are calibrated probabilities important in classification?**
   **A:** Business thresholds depend on trustworthy probabilities, not only ranking quality.

9. **Q: What is one practical ensemble tuning strategy?**
   **A:** Tune depth and learning rate jointly, then adjust number of estimators with early stopping.

10. **Q: How do you compare supervised models fairly?**
    **A:** Same data splits, same preprocessing pipeline, same evaluation metrics, and held-out final test.

11. **Q: Why is model-family choice a product decision as well as a technical one?**
    **A:** Because explainability, latency, retraining cadence, and governance needs affect deployment viability.

12. **Q: When is Random Forest often preferable to boosting in practice?**
    **A:** When you need robust tabular performance with lower tuning and faster iteration.

13. **Q: What is one warning sign that a boosted model is over-tuned?**
    **A:** Validation gains are tiny while complexity and instability increase across folds/slices.

14. **Q: Why should calibration be checked even for high-AUC models?**
    **A:** Decision thresholds require reliable probabilities, not only ranking quality.

15. **Q: What is a good supervised-learning baseline policy?**
    **A:** Always ship with a reproducible simple baseline and justify any complexity increase with measured business lift.

# References

- scikit-learn ensembles guide: https://scikit-learn.org/stable/modules/ensemble.html
- RandomForestClassifier docs: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
- GradientBoostingClassifier docs: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html
- XGBoost parameter docs: https://xgboost.readthedocs.io/en/stable/parameter.html
