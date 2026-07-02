# Overview

Applied statistics in ML means making valid decisions from model outputs: choosing metrics, diagnosing error modes, and aligning evaluation with business cost.

# Correlation vs Causation

- Correlation: statistical association.
- Causation: intervention on one variable changes another.

Predictive models can be useful without causal interpretation, but decision-making must respect this limitation.

# Bias/Variance & Overfitting/Underfitting

Expected prediction error decomposes into bias, variance, and irreducible noise (conceptually).

- High bias: model too simple, systematic error.
- High variance: model too sensitive to training fluctuations.
- Underfitting: high bias.
- Overfitting: high variance.

# Evaluation Metrics

## Classification
- Accuracy: $rac{TP+TN}{N}$
- Precision: $rac{TP}{TP+FP}$
- Recall: $rac{TP}{TP+FN}$
- F1: harmonic mean of precision and recall.
- ROC-AUC: ranking quality across thresholds.

## Regression
- MAE, MSE, RMSE, $R^2$.

Metric choice must match error cost profile.

# Iris Classification Example

Iris offers multiclass baseline to compare metrics and confusion patterns. Use train/test split and standardized features before logistic regression.

# Common Pitfalls

- Reporting only accuracy for imbalanced problems.
- Tuning on test set (leakage).
- Ignoring calibration when probabilities drive decisions.

# Business Use Cases

- Fraud detection: recall often prioritized.
- Medical triage: high recall with controlled precision.
- Marketing targeting: precision-sensitive to avoid wasted spend.

# Business Case Studies & Exceptions

## Case 1: Accuracy-Led Decision Failure
Model with 95% accuracy missed rare but costly fraud cases.

Fix:
- Shift optimization to recall/F1/PR-AUC.
- Use class weighting and threshold tuning.

## Case 2: Poor Calibration in Risk Scores
Predicted 0.9 risk did not correspond to actual event rate, causing bad capacity planning.

Fix:
- Add calibration diagnostics.
- Use Platt scaling or isotonic calibration if needed.

# Interview Questions & Answers

1. **Q: Precision vs recall?**  
   **A:** Precision measures false-positive control; recall measures false-negative control.

2. **Q: When use F1?**  
   **A:** When balancing precision and recall under class imbalance.

3. **Q: Why ROC-AUC can mislead?**  
   **A:** It may look strong even when precision in rare-positive region is poor.

4. **Q: What is data leakage?**  
   **A:** Information from validation/test leaks into training, inflating metrics.

5. **Q: Bias-variance tradeoff in practice?**  
   **A:** Increasing model complexity often reduces bias but increases variance.

6. **Q: Why calibration matters?**  
   **A:** Business decisions based on probability thresholds require trustworthy probabilities.

7. **Q: Why keep separate train/val/test sets?**  
   **A:** To tune, select, and estimate generalization without optimistic bias.

8. **Q: Threshold tuning example?**  
   **A:** Lower threshold to catch more fraud (higher recall) at cost of more false alerts.

9. **Q: Metric for symmetric regression error?**  
   **A:** RMSE or MAE depending outlier sensitivity preference.

10. **Q: What is good evaluation report?**  
    **A:** Multiple metrics, confusion matrix, segment breakdown, and assumptions/limitations.
