# Overview

Applied statistics for ML is about decision quality: selecting metrics, diagnosing error patterns, and avoiding evaluation traps.

A model is useful only when its measured performance maps to business outcomes under realistic constraints.

Applied statistics is therefore an interface between model behavior and decision policy. Two models with similar aggregate metrics can produce very different business outcomes once you account for thresholding, calibration, segment performance, and error costs. This is why production ML teams track metric trees: top-level objective metrics (e.g., revenue at risk reduced) linked to operational metrics (false positives, review queue load, latency).

# Correlation vs Causation

- Correlation: variables co-vary statistically.
- Causation: intervention on one variable changes another.

Predictive ML often uses correlation successfully, but product/policy decisions may require causal evidence.

Practical implication:
Correlation-based predictors can be excellent for ranking and forecasting, but intervention decisions (pricing, policy, treatment) need stronger causal assumptions or experiments.

# Bias/Variance & Overfitting/Underfitting

Expected prediction error can be decomposed conceptually as:
$$
\mathbb{E}[(y-\hat{f}(x))^2] = \text{Bias}^2 + \text{Variance} + \text{Noise}
$$

- High bias: model too simple, systematic error.
- High variance: model too sensitive to training fluctuations.
- Underfitting: typically high bias.
- Overfitting: typically high variance.

Diagram in words:
Imagine model complexity on x-axis and validation error on y-axis. Error decreases initially (bias drops), then rises (variance dominates), forming a U-shaped curve.

# Evaluation Metrics

## Classification

Confusion matrix components: TP, TN, FP, FN.

- Accuracy:
$$
\frac{TP+TN}{TP+TN+FP+FN}
$$
- Precision:
$$
\frac{TP}{TP+FP}
$$
- Recall:
$$
\frac{TP}{TP+FN}
$$
- F1:
$$
2\cdot\frac{\text{Precision}\cdot\text{Recall}}{\text{Precision}+\text{Recall}}
$$
- ROC-AUC: ranking quality over thresholds.

Calibration concept:
If model predicts 0.8 risk for many items, around 80% should be positive in that bucket.

## Regression

- MAE:
$$
\frac{1}{n}\sum_i |y_i-\hat{y}_i|
$$
- MSE:
$$
\frac{1}{n}\sum_i (y_i-\hat{y}_i)^2
$$
- RMSE: $\sqrt{MSE}$
- $R^2$: proportion of variance explained (with caveats)

Metric selection rule:
Choose metrics by error cost asymmetry and operational objective, not popularity.

# Cross-Validation and Data Splits

Standard strategy:
- Train split: fit parameters
- Validation split: tune/hyperparameter choices
- Test split: final unbiased estimate

k-fold cross-validation reduces split variance.
Stratified splits preserve class proportions for imbalanced problems.

Real-world split policy:
- Random split for IID settings.
- Time-aware split for drift-prone systems.
- Group-aware split when entities repeat (users/devices/patients).

# Iris Classification Example (and Beyond)

Iris is useful for controlled multiclass metric interpretation.

To move toward realistic settings:
- Use probability calibration checks.
- Evaluate threshold sensitivity.
- Add segment-level metric breakdown.

# Common Pitfalls

- Reporting accuracy only for imbalanced data.
- Tuning repeatedly on test set.
- Ignoring calibration when probabilities drive actions.
- Comparing models on different splits/pipelines.

# Business Use Cases

- Medical triage: prioritize recall with acceptable precision.
- Fraud detection: maximize recall under alert capacity limits.
- Ad targeting: precision-sensitive to reduce wasted spend.

# Business Case Studies & Exceptions

## Case 1: Accuracy-Led Decision Failure

Scenario:
Fraud model shows high accuracy due to dominant negative class.

Impact:
Misses costly fraud positives.

Fix pattern:
- Shift focus to recall, precision, PR-AUC.
- Tune threshold using business cost matrix.

Exception:
If false positives are extremely expensive (manual investigations), precision constraints may dominate.

## Case 2: Poor Calibration in Risk Scores

Scenario:
Predicted probabilities overconfident relative to observed frequencies.

Impact:
Bad resource allocation and SLA planning.

Fix pattern:
- Reliability diagrams + Brier score.
- Calibration methods (Platt/isotonic) where appropriate.

## Case 3: Data Leakage via Preprocessing

Scenario:
Scaler fit on full dataset before split.

Impact:
Optimistic metrics that fail in production.

Fix pattern:
- Use leakage-safe pipeline fit only on training folds.

# Interview Questions & Answers

1. **Q: Why can accuracy be misleading?**
   **A:** In imbalanced datasets, trivial majority-class predictions can appear accurate but useless.

2. **Q: Precision vs recall tradeoff?**
   **A:** Precision controls false positives; recall controls false negatives.

3. **Q: When is F1 useful?**
   **A:** When balancing precision and recall is important.

4. **Q: Why keep a holdout test set after CV?**
   **A:** To provide final unbiased performance estimate after model selection.

5. **Q: What is calibration and why important?**
   **A:** Calibration aligns predicted probabilities with true event frequencies, critical for threshold-based decisions.

6. **Q: Explain bias-variance tradeoff practically.**
   **A:** More complex models reduce bias but may overreact to noise, increasing variance.

7. **Q: What is data leakage?**
   **A:** Information unavailable at prediction time influences training/evaluation, inflating offline metrics.

8. **Q: Which regression metric is more outlier-sensitive, MAE or RMSE?**
   **A:** RMSE due to squaring errors.

9. **Q: How do you select a metric for business use?**
   **A:** Map FP/FN costs and operational constraints to metric/threshold objectives.

10. **Q: What should an evaluation report include?**
    **A:** Multiple metrics, confusion matrix, calibration view, segment analysis, and limitations.

11. **Q: Why can two models with similar AUC still behave differently in production?**
    **A:** Their calibration, threshold sensitivity, and segment-level errors may differ.

12. **Q: When should you use a time-based validation split?**
    **A:** When data-generating processes evolve and future predictions must reflect chronological reality.

13. **Q: What is an evaluation anti-pattern in product teams?**
    **A:** Optimizing one headline metric while ignoring operational capacity or fairness impacts.

14. **Q: Why is segment-level analysis important?**
    **A:** Aggregate metrics can hide severe underperformance in critical cohorts.

15. **Q: How do you connect model metrics to business KPIs?**
    **A:** Translate FP/FN rates and thresholds into expected cost, risk, or conversion impact under real traffic volumes.

# References

- scikit-learn model evaluation docs: https://scikit-learn.org/stable/modules/model_evaluation.html
- scikit-learn cross-validation guide: https://scikit-learn.org/stable/modules/cross_validation.html
- ISLR: https://www.statlearning.com/

## Bridge to Next Lesson

- **What you now know:** You now understand the math toolkit behind ML: vector/matrix operations, gradients, probability, and practical metric selection under business constraints.
- **Why the next lesson follows:** The next lesson follows because these mathematical concepts become concrete when training and comparing real supervised and unsupervised models.
- **What you'll build next:** You will build end-to-end classical ML workflows for regression, classification, clustering, and robust model selection.
