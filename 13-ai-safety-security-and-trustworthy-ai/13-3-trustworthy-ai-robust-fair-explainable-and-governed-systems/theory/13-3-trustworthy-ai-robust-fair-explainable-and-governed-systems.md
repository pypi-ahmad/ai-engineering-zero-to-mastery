# Trustworthy AI: Robust, Fair, Explainable & Governed Systems

## Overview

Trustworthy AI is a systems property, not a single model feature. A trustworthy system is expected to be:

- Robust: stable under shift and stress.
- Fair: avoids unjustified discrimination.
- Explainable: supports human understanding and accountability.
- Secure and governed: controlled by policy, audit, and operational safeguards.

A practical definition:

$$
\text{Trustworthiness} = f(\text{technical reliability}, \text{ethical validity}, \text{governance maturity})
$$

## Fairness & Non-Discrimination

### Core Definitions

- `Group fairness`: compare outcome distributions across protected groups.
- `Individual fairness`: similar individuals should receive similar treatment.

Common group metrics (high-level):

- Demographic parity difference:

$$
P(\hat{Y}=1 \mid A=a) - P(\hat{Y}=1 \mid A=b)
$$

- Equal opportunity difference:

$$
TPR_{a} - TPR_{b}
$$

where $A$ is protected attribute and $TPR$ is true positive rate.

### Bias Sources

- Historical bias in labels.
- Representation bias in sampling.
- Measurement bias in features.
- Deployment context drift that affects groups unequally.

### Mitigation Patterns

- Pre-processing: rebalancing, feature review, label audits.
- In-processing: fairness-constrained optimization.
- Post-processing: threshold adjustments and calibrated policies.

## Explainability & Interpretability

### Global vs Local Explanations

- `Global`: understand overall model behavior (feature importance, monotonic patterns).
- `Local`: explain one prediction (counterfactuals, local feature attribution).

Why this matters:

- Regulatory and legal defensibility.
- Error analysis and debugging.
- Human trust calibration (neither blind trust nor blind rejection).

### Technique Families

- Intrinsic interpretability: linear models, decision trees.
- Post-hoc explanations: SHAP/LIME-like local attributions.
- Example-based explanations and counterfactual analysis.

Caveat:

- Explanations can be plausible but incomplete; do not treat them as proof of correctness.

## Governance & Assurance

### Governance Artifacts

- Model Cards: purpose, data, evaluation, limitations.
- Datasheets for Datasets: provenance, consent, collection context.
- Risk registers: identified harms, controls, residual risk.
- Change logs and approval trails.

### Assurance Lifecycle

1. Pre-deployment risk assessment.
2. Validation and stress testing.
3. Deployment gating with sign-off.
4. Continuous monitoring and incident response.
5. Periodic re-certification.

### Reference Frameworks

- NIST AI RMF and associated profiles.
- Organization-specific Responsible AI policies.
- Sector-specific compliance overlays (finance, healthcare, public services).

## Building Trustworthy Systems in Practice

Textual architecture:

1. Data governance layer: provenance, quality checks, protected-attribute policy.
2. Modeling layer: baseline + fairness/robustness diagnostics.
3. Explanation layer: global and local explanation tooling.
4. Decision policy layer: human override and escalation.
5. Operations layer: monitoring, audits, incident management.

## Safety & Security Case Studies & Exceptions

### Case 1: Credit Scoring Fairness Audit

Scenario:

- Binary classifier for credit approvals shows strong AUC.
- Group-level approval rates differ sharply.

Actions:

- Evaluate parity and opportunity metrics.
- Investigate feature proxies for protected attributes.
- Apply threshold/policy adjustment and monitor portfolio-level impact.

Key lesson:

- High predictive performance does not guarantee equitable outcomes.

### Case 2: Healthcare Risk Model Explainability

Scenario:

- Clinical triage model performs well overall.
- Clinicians distrust opaque scores and need rationale.

Actions:

- Add local explanations for individual predictions.
- Validate explanation stability across cohorts.
- Add policy that low-confidence predictions require clinician review.

### Case 3: Governance Failure in Fast Deployment

Scenario:

- A chatbot is released without documented limitations or monitoring ownership.

Impact:

- Delayed response to harmful outputs and accountability confusion.

Mitigations:

- Assign model owner and escalation chain.
- Establish telemetry standards and incident SLAs.
- Require model card completion before launch.

### Exceptions

- In low-risk internal automation, lightweight explainability may be sufficient.
- In regulated decisions, lightweight documentation is insufficient regardless of performance.

## Interview Questions & Answers

1. **Q:** Define Trustworthy AI.
   **A:** Trustworthy AI is the design and operation of AI systems that are robust, fair, explainable, secure, and governed through accountable processes.

2. **Q:** What is demographic parity?
   **A:** A fairness criterion requiring similar positive prediction rates across groups.

3. **Q:** What is equal opportunity?
   **A:** A fairness criterion requiring similar true positive rates across groups.

4. **Q:** Can a model satisfy all fairness metrics simultaneously?
   **A:** Often no; fairness metrics can conflict under different base rates.

5. **Q:** What is group fairness vs individual fairness?
   **A:** Group fairness compares aggregates by group; individual fairness compares treatment of similar individuals.

6. **Q:** Why is explainability important for governance?
   **A:** It supports contestability, auditability, and debugging of high-impact decisions.

7. **Q:** Difference between interpretability and explainability?
   **A:** Interpretability often refers to inherent model transparency; explainability includes post-hoc methods for opaque models.

8. **Q:** What is a model card?
   **A:** A structured document describing intended use, evaluation results, limitations, and risks.

9. **Q:** Why is monitoring needed after fairness evaluation?
   **A:** Data distributions and user populations change; fairness can degrade after deployment.

10. **Q:** What is proxy discrimination?
    **A:** When non-sensitive features encode sensitive attributes and lead to discriminatory outcomes.

11. **Q:** How do you prioritize fairness mitigations?
    **A:** By risk severity, legal exposure, user impact, and business constraints.

12. **Q:** What governance controls are essential?
    **A:** Ownership, approval gates, telemetry, incident response, and documentation.

13. **Q:** What are limitations of SHAP/LIME-style explanations?
    **A:** They can be unstable, approximation-based, and sensitive to assumptions.

14. **Q:** Why can removing protected attributes be insufficient?
    **A:** Correlated proxy features can still carry protected information.

15. **Q:** What is assurance in AI context?
    **A:** Ongoing evidence-based activities that demonstrate system safety and compliance over time.

16. **Q:** How do fairness and utility trade off?
    **A:** Some mitigations can reduce raw accuracy; the objective is risk-adjusted, policy-compliant performance.

17. **Q:** What is a practical first fairness test?
    **A:** Compare selection and error rates across protected groups on a holdout set.

18. **Q:** How do you involve domain experts?
    **A:** Include them in metric selection, threshold policy, and exception handling design.

19. **Q:** What is governance debt?
    **A:** Accumulated lack of controls/documentation that later increases incident cost and compliance risk.

20. **Q:** How do you make trustworthy AI actionable for teams?
    **A:** Convert principles into explicit requirements, test suites, ownership, and release gates.

## Further Reading and Source-Informed References

- ETH Reliable & Trustworthy AI course: https://www.sri.inf.ethz.ch/teaching/rtai24
- SUTD Trustworthy AI course: https://www.sutd.edu.sg/course/trustworthy-ai-designing-robust-ethical-and-secure-ai-system/
- Coursera Building Trustworthy AI specialization: https://www.coursera.org/specializations/building-trustworthy-ai
- NIST AI RMF resource page: https://www.nist.gov/itl/ai-risk-management-framework
- USC AI curriculum (includes trustworthy AI coursework): https://viterbiadmission.usc.edu/wp-content/uploads/2026/03/AI-Curriculum-Computing-Foundations-2-26.pdf
