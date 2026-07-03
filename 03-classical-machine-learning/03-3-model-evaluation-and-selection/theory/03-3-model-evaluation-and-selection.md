# Overview

Model evaluation determines whether performance is real or an artifact of leakage, overfitting, or metric mismatch. Selection determines which model is best under business constraints, not just benchmark scores.

# Train/Validation/Test Strategy

Standard split roles:
- **Train:** fit model parameters.
- **Validation:** tune hyperparameters and thresholds.
- **Test:** final unbiased estimate after all tuning.

Per scikit-learn guidance, evaluating on training data is a methodological mistake because memorization can appear as high performance but fails on unseen data.

# Cross-Validation

## k-Fold CV

Split training set into $k$ folds; for each fold:
- Train on $k-1$ folds
- Validate on remaining fold
- Aggregate metrics

Benefits:
- More stable estimate than a single split.

## Stratified CV

For classification, preserve class proportions in each fold.

Essential for imbalanced classes where random splits can distort minority representation.

Diagram in words:
Imagine training data as stacked cards. k-fold rotates which stack is held out, so every sample is validated once.

# Hyperparameter Tuning

## Grid Search

Exhaustive search over predefined parameter grid.

Pros: simple, deterministic.
Cons: expensive in high-dimensional spaces.

## Random Search

Randomly sample parameter combinations.

Pros: often more efficient when only a subset of parameters strongly affects performance.

## Bayesian Optimization (High-Level)

Build surrogate model of objective and select promising points iteratively.

Pros: sample-efficient on expensive objectives.
Cons: added tooling/complexity.

# Model Comparison Framework

A fair comparison requires:
- Same data splits
- Same preprocessing pipeline
- Same evaluation metrics
- Same leakage-safe procedure

Decision criteria beyond metric score:
- Latency
- Memory footprint
- Interpretability/regulatory constraints
- Training and serving cost
- Failure mode severity

# Evaluation Workflow Template

Use this repeatable workflow before model promotion:

1. Define success metric and business constraint metric (for example latency or cost).
2. Establish baseline model and frozen data split policy.
3. Run CV/tuning under identical preprocessing pipelines.
4. Compare candidates on mean + variance, not mean only.
5. Perform error analysis by important segments.
6. Validate on untouched holdout/test set.
7. Record deployment/rollback recommendation.

Template snippet:

```text
Objective metric:
Constraint metrics:
Baseline score:
Candidate score:
Variance/uncertainty:
Segment risks:
Promotion decision:
```

# Data Leakage and Robustness

Leakage examples:
- Fitting scalers/imputers on full dataset before split.
- Using future timestamps in historical training features.
- Target leakage through post-outcome features.

Leakage effect:
Inflated offline metrics and degraded production generalization.

Mitigation:
- Use pipelines that fit transforms only on training folds.
- Use temporal validation for time-dependent problems.
- Review feature lineage and availability time.

# Edge Cases in Model Selection

1. **Metric conflict**
- Highest AUC model may fail precision-at-threshold constraints.
- Use decision thresholds and business utility curves.

2. **Distribution shift expected post-launch**
- Static random split may overestimate quality.
- Add temporal or stress holdout aligned to deployment reality.

3. **Tiny datasets**
- Single test split variance can be extreme.
- Prefer repeated CV and report uncertainty explicitly.

# Handling Imbalanced Data in Selection

Strategies:
- Use precision/recall/F1/PR-AUC with class-aware thresholding.
- Apply class weights or sampling when justified.
- Report confusion matrix and calibration.

# Business Case Studies & Exceptions

## Case 1: Fraud Detection Model Choice

Scenario:
Highest AUC model exceeds latency budget for real-time scoring.

Decision pattern:
- Choose slightly lower AUC model with acceptable recall and latency.
- Route ambiguous cases to asynchronous secondary review.

## Case 2: Overfitted Validation Leader

Scenario:
Model tuned heavily on one validation split wins offline but fails after deployment.

Fix pattern:
- Use repeated CV and untouched holdout.
- Add temporal/challenge holdout when drift expected.

## Case 3: Leakage Through Target Encoding

Scenario:
Target encoding computed on full data includes validation labels.

Fix pattern:
- Fold-aware encoding inside CV loops.
- Audit pipeline step ordering.

Exception:
For tiny datasets, strict split separation may cause high variance; use repeated CV with transparent uncertainty reporting.

# Interview Questions & Answers

1. **Q: Explain cross-validation briefly.**
   **A:** It repeatedly trains/validates across folds to estimate generalization more reliably than one split.

2. **Q: Why keep a final test set if CV is used?**
   **A:** CV guides model selection; test set gives final unbiased estimate after choices are locked.

3. **Q: Why is data leakage dangerous?**
   **A:** It makes metrics look better than real-world performance by using unavailable information.

4. **Q: Grid search vs random search?**
   **A:** Grid is exhaustive but costly; random is usually more efficient in high-dimensional spaces.

5. **Q: How select model for imbalanced data?**
   **A:** Optimize business-relevant metrics (precision/recall/PR-AUC), tune thresholds, and validate calibration.

6. **Q: Why compare models within the same pipeline?**
   **A:** Different preprocessing/splits can create unfair comparisons.

7. **Q: What is stratified CV?**
   **A:** CV splitting that preserves class distribution across folds.

8. **Q: Why is latency part of model selection?**
   **A:** A model that misses serving SLA can fail business objectives despite strong offline metrics.

9. **Q: What is one robust anti-overfitting evaluation practice?**
   **A:** Keep an untouched holdout and avoid repeated test peeking.

10. **Q: What should be reported alongside mean CV score?**
    **A:** Variability (std/confidence), metric definitions, and key assumptions/limitations.

11. **Q: Why is “mean CV score only” insufficient for promotion decisions?**
    **A:** Variance and segment-specific failures can hide significant risk.

12. **Q: What is one practical anti-leakage safeguard during tuning?**
    **A:** Put preprocessing and model in a single pipeline inside CV folds.

13. **Q: When is temporal validation mandatory?**
    **A:** When feature/label generation depends on time and drift is plausible.

14. **Q: How do you choose between two close models?**
    **A:** Use business constraints (latency, cost, interpretability, failure severity) as tie-breakers.

15. **Q: Why include rollback criteria in model selection docs?**
    **A:** Selection is operational; decisions should include recovery paths, not only scores.

# References

- scikit-learn cross-validation guide: https://scikit-learn.org/stable/modules/cross_validation.html
- scikit-learn model selection guide: https://scikit-learn.org/stable/modules/grid_search.html
- scikit-learn `cross_validate`: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html

## Bridge to Next Lesson

- **What you now know:** You can frame ML tasks, train classical models, and evaluate them with principled validation, tuning, and leakage-aware workflows.
- **Why the next lesson follows:** The next lesson follows because many modern AI applications need representation learning and non-linear function approximation beyond classical feature engineering.
- **What you'll build next:** You will build deep learning systems with neural networks, optimization strategies, computer vision models, and transformer-based sequence models.

