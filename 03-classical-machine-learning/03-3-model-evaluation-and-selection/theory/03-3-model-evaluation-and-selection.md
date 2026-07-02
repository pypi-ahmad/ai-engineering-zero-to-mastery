# Overview

Model evaluation and selection determine whether model is genuinely useful or only appears good due to leakage, overfitting, or wrong metrics.

# Train/Validation/Test Strategy

- **Train set:** fit model parameters.
- **Validation set:** tune hyperparameters/thresholds.
- **Test set:** final unbiased estimate.

Never tune repeatedly on test set.

# Cross-Validation

## k-Fold CV
Split training data into $k$ folds; train on $k-1$ folds, validate on remaining fold; average performance.

## Stratified CV
Preserves class proportions in each fold; critical for imbalanced classification.

# Hyperparameter Tuning

- **Grid search:** exhaustive over predefined grid.
- **Random search:** sample configurations; often more efficient in high dimensions.
- **Bayesian optimization (high-level):** probabilistic model guides promising configurations.

# Model Comparison Framework

Use common pipeline and fixed splits for fair comparison.

Consider:
- Predictive performance.
- Latency and memory.
- Interpretability and governance constraints.
- Training/inference cost.

# Data Leakage and Robustness

Leakage examples:
- Fitting scaler on full dataset before split.
- Using future timestamps in training features.

Leakage inflates offline metrics and causes production failure.

# Business Case Studies & Exceptions

## Case 1: Fraud Detection Model Choice
Best AUC model had unacceptable latency for real-time scoring.

Decision:
- Select slightly lower AUC model with strong recall and lower latency.
- Use async secondary model for deeper review.

## Case 2: Overfitted Validation Leader
Model tuned excessively on single validation split failed post-deployment.

Mitigation:
- Nested or repeated CV.
- Holdout challenge set by time segment.

# Interview Questions & Answers

1. **Q: Why need separate test set?**  
   **A:** To estimate generalization on unseen data after all tuning decisions are finalized.

2. **Q: What is cross-validation?**  
   **A:** Repeated train/validate over multiple folds to reduce split variance.

3. **Q: Stratified CV use case?**  
   **A:** Imbalanced classification where class ratios must be preserved.

4. **Q: Grid vs random search?**  
   **A:** Grid exhaustive but expensive; random search often finds strong configs faster.

5. **Q: What is data leakage?**  
   **A:** Train process receives info unavailable at prediction time.

6. **Q: Why model selection not only about metric score?**  
   **A:** Real systems need latency, interpretability, and cost constraints.

7. **Q: How evaluate imbalanced data?**  
   **A:** Use precision/recall/F1/PR-AUC and class-aware thresholding.

8. **Q: What is calibration relevance?**  
   **A:** Threshold decisions require reliable probabilities, not only ranking.

9. **Q: Why repeated CV?**  
   **A:** Reduces randomness from one fold partitioning.

10. **Q: Example of leakage in feature engineering?**  
    **A:** Target encoding computed using full data including validation rows.
