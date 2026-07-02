# Overview

Applied statistics in ML focuses on evaluation and diagnostics: choosing the right metrics, understanding model errors, and validating performance trade-offs.

# Correlation vs Causation

Correlation describes co-movement; causation implies a direct mechanism. ML models often learn correlation, not causal truth.

# Bias/Variance & Overfitting/Underfitting

- Bias: overly simple assumptions leading to systematic error.
- Variance: sensitivity to training noise leading to unstable predictions.
- Underfitting corresponds to high bias; overfitting corresponds to high variance.

# Evaluation Metrics

- Accuracy.
- Precision and recall.
- F1-score.
- ROC-AUC (high-level ranking quality in binary/one-vs-rest settings).

# Iris Classification Example

The Iris dataset provides a compact multiclass classification case for training a baseline model and evaluating metrics beyond accuracy.

# Common Pitfalls

- Relying on accuracy alone, especially when class balance changes.
- Misinterpreting AUC without understanding class framing.

# Business Use Cases

- Metric-driven model selection and release decisions.
- Threshold tuning for cost-sensitive decisions.
- Ongoing production monitoring with alert thresholds.

# Interview Prep Checklist

- Explain precision vs recall and when each matters.
- Explain F1 and its trade-off meaning.
- Give a practical bias/variance trade-off example.
