# Overview
Data-centric labeling ops treats labels as production assets managed by engineering discipline. Many teams plateau not because model architecture is weak, but because label policy, coverage, and quality are inconsistent. This chapter focuses on building repeatable labeling flywheels that improve model performance with measurable ROI.

# Labeling Operations Framework
## End-to-end lifecycle
1. define label ontology and policy boundaries,
2. sample candidate data from production streams,
3. annotate with quality controls,
4. adjudicate disagreements,
5. publish versioned dataset,
6. retrain/evaluate and measure gains,
7. feed model failures back into prioritization queues.

## Label quality dimensions
- policy clarity and boundary consistency,
- inter-annotator agreement,
- edge-case coverage,
- label freshness versus data drift,
- traceability of rationale and revisions.

## Data contracts for labeling
Treat labels as governed interfaces:
- schema version,
- allowed classes and definitions,
- required metadata (source, timestamp, annotator role),
- acceptance criteria and QA thresholds.

# Active Learning in Production
Active learning prioritizes examples that maximize model improvement per annotation dollar.

Common strategies:
- uncertainty sampling (high predictive entropy),
- diversity sampling (coverage of underrepresented clusters),
- disagreement sampling (ensemble/model disagreement).

A practical loop:
1. train baseline model,
2. score unlabeled pool,
3. select informative batch,
4. annotate + QA,
5. retrain and compare against baseline.

Key metric:

$$
\text{Gain per batch} = \frac{\Delta \text{target metric}}{\text{annotation cost}}
$$

# Weak Supervision and Programmatic Labeling
Weak supervision uses heuristics, labeling functions, rules, or external signals to create noisy labels at scale.

Best uses:
- bootstrap for low-resource tasks,
- pre-labeling before human verification,
- expanding coverage for repetitive patterns.

Risks:
- systematic heuristic bias,
- stale rules under drift,
- over-trust in pseudo-label confidence.

Mitigations:
- confidence-based routing to human review,
- periodic rule audits,
- holdout evaluation with high-quality human labels.

# Governance, Tooling, and Metrics
## Governance controls
- versioned annotation guidelines,
- adjudication logs for disputed cases,
- train/validation/test leakage checks,
- protected-attribute handling and fairness review.

## Ops telemetry
Track:
- labels per hour and cycle time,
- acceptance rate after QA,
- inter-annotator agreement,
- cost per accepted label,
- model lift per labeling batch.

## Queue design patterns
- high-risk queue (safety/compliance critical),
- uncertainty queue (model confusion),
- drift queue (recent distribution shifts),
- exploration queue (rare/novel patterns).

# Production Case Studies & Exceptions
## Case 1: Support ticket intent model
Pattern: uncertainty-driven active learning + weekly calibration review.

Impact: better intent accuracy with lower annotation spend.

Exception: unstable taxonomy caused churn; active learning amplified inconsistency until ontology was fixed.

## Case 2: Compliance document classifier
Pattern: weak supervision rules for known legal phrases + human review for low-confidence samples.

Impact: much faster initial dataset creation.

Exception: rules drifted as policy language evolved; required scheduled rule maintenance.

## Case 3: Fraud alert triage
Pattern: disagreement-based sampling from multiple models plus analyst feedback loop.

Impact: improved recall on rare fraud patterns.

Exception: class imbalance still required targeted cohort sampling and synthetic augmentation.

# Interview Questions & Answers
1. **Q:** What is data-centric AI in operations terms?  
   **A:** Improving model outcomes by systematically improving data and labels, not only model architecture.
2. **Q:** Why is labeling frequently a bottleneck?  
   **A:** High-quality annotation is expensive, slow, and domain-dependent.
3. **Q:** What is active learning?  
   **A:** Selecting the most informative unlabeled samples for annotation.
4. **Q:** Common active learning strategies?  
   **A:** Uncertainty, diversity, and disagreement sampling.
5. **Q:** What is weak supervision?  
   **A:** Programmatic generation of noisy labels from heuristics or external signals.
6. **Q:** Main weak-supervision benefit?  
   **A:** Rapid bootstrap of training data before full human labeling.
7. **Q:** Main weak-supervision risk?  
   **A:** Hidden bias from brittle labeling functions.
8. **Q:** Why measure inter-annotator agreement?  
   **A:** It reflects policy clarity and labeling consistency.
9. **Q:** Why version annotation guidelines?  
   **A:** Reproducibility and auditable dataset lineage.
10. **Q:** How do you tie labeling to business value?  
    **A:** Measure model lift and business KPI impact per annotation spend.
11. **Q:** How do you prevent leakage during data ops?  
    **A:** Split discipline, dedupe checks, and pipeline-level validation gates.
12. **Q:** When is active learning not enough?  
    **A:** When label definitions are unstable or business policy is unclear.
13. **Q:** Why use disagreement queues?  
    **A:** They surface ambiguous and high-information samples quickly.
14. **Q:** How does this connect to LLMOps?  
    **A:** Prompt failures and bad outputs become prioritized data for post-training loops.
15. **Q:** What is a labeling data contract?  
    **A:** A formal schema and quality agreement for label production and consumption.
16. **Q:** Why track label freshness?  
    **A:** Stale labels degrade model relevance under shifting data distributions.
17. **Q:** Typical anti-pattern?  
    **A:** Chasing model changes while ignoring policy ambiguity in labels.
18. **Q:** How do you scale annotation quality?  
    **A:** Calibration sessions, adjudication workflows, and targeted reviewer training.
19. **Q:** What is gain-per-annotation?  
    **A:** Incremental model performance improvement normalized by label cost.
20. **Q:** One-line guidance?  
    **A:** Build labeling as a governed production system with explicit quality economics.

# Bridge to Lesson 13
**What you now know:** You can operate labeling flywheels with active learning, weak supervision, and governed quality controls.

**Why the next lesson follows:** Strong operations still need robust safety and security controls under adversarial and high-stakes conditions.

**What you'll build next:** threat-aware evaluation, guardrails, and trustworthy deployment patterns.

# References
- Snorkel active learning and weak supervision docs: https://docs.snorkel.ai/docs/25.4/user-guide/intro/active-learning-weak-supervision
- Snorkel weak supervision paper: https://arxiv.org/abs/1711.10160
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
