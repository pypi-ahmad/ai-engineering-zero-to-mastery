# Robustness, Adversarial ML & AI Security

## Overview

Robustness and security are foundational to safe AI operations. A model can be accurate on clean validation data and still fail under intentional attack or small environmental shifts. Adversarial ML studies those failures and defensive techniques.

Two complementary perspectives:

- `Reliability`: maintain performance under benign shift and noise.
- `Security`: resist strategic, malicious manipulation of data, model interfaces, and supply chain.

## Adversarial Machine Learning

### Threat Modeling Basics

A useful adversarial ML threat model specifies:

- Attacker goal: misclassification, exfiltration, service degradation, model theft.
- Attacker knowledge: white-box, gray-box, black-box.
- Attacker capability: query access, training-data access, pipeline access.
- Success criteria: targeted or untargeted error increase, data extraction, policy bypass.

### Attack Taxonomy

#### 1. Evasion Attacks (Inference-time)

- Input is perturbed to induce wrong predictions while appearing benign.
- Examples: adversarial image perturbations, prompt injection payloads.

#### 2. Poisoning Attacks (Training-time)

- Attacker inserts malicious samples or labels to corrupt learned behavior.
- Subtypes: availability attacks (degrade global performance), backdoor attacks (trigger-based misbehavior).

#### 3. Model Extraction / Stealing

- Adversary queries API to approximate model decision boundary.
- Risks: IP theft and follow-on attack optimization.

#### 4. Privacy Attacks

- Membership inference: infer whether a record was in training data.
- Model inversion: reconstruct sensitive attributes from model behavior.

## Robustness & Evaluation

### Robustness Metrics

Common operational metrics:

- Accuracy under perturbation budget $\epsilon$.
- Worst-case loss on adversarial examples.
- Calibration and confidence stability under perturbation.
- Attack success rate (ASR).

### Evaluation Framework

1. Define assets and acceptable failure thresholds.
2. Select realistic threat scenarios (not only benchmark attacks).
3. Run attack suites across data slices.
4. Track both security and utility metrics.
5. Build regression checks into CI.

### Defense Strategies (High-Level)

- `Adversarial training`: train on adversarially perturbed samples.
- `Input transformations`: denoising, smoothing, normalization (limited protection alone).
- `Detection layers`: identify suspicious inputs and trigger fallback.
- `Certified robustness` (where feasible): mathematically bounded guarantees for specific perturbation classes.
- `Access controls`: rate limits, authentication, query anomaly detection.

Important caveat:

- No single defense is universally effective; combine controls and validate continuously.

## AI Security & Offensive AI

### Attacks On AI Systems

- Data pipeline compromise.
- Model artifact tampering in registry or deployment path.
- Insecure tool integrations in agent systems.
- Prompt injection into retrieval corpora.

### Attacks Using AI

- Deepfake generation for fraud and social engineering.
- Automated phishing personalization.
- Malware development acceleration.

This dual-use reality requires defenders to secure both AI-enabled products and AI-enhanced adversaries.

## Security Operations Pattern for AI Systems

Textual architecture:

1. Threat model using a framework such as MITRE ATLAS.
2. Security controls mapped to lifecycle stages (data, training, serving, monitoring).
3. Continuous testing with adversarial scenarios.
4. Incident response runbooks specific to model failures and abuse.
5. Post-incident patching and policy updates.

## Safety & Security Case Studies & Exceptions

### Case 1: Evasion Attack on Vision Classifier

Scenario:

- A safety camera classifier is highly accurate in lab conditions.
- Small perturbations crafted by an attacker cause misclassification.

Impact:

- False negatives for restricted-object detection.

Mitigation stack:

- Adversarial training on realistic perturbation sets.
- Confidence thresholding + abstain behavior.
- Human review for critical alerts.

### Case 2: Data Poisoning in Feedback Loop

Scenario:

- User feedback stream is used for daily retraining.
- Coordinated adversarial accounts inject biased labels.

Impact:

- Gradual degradation and policy drift.

Mitigation stack:

- Data provenance checks and anomaly scoring.
- Delayed promotion with holdout validation.
- Signed data and role-based ingestion permissions.

### Case 3: Deepfake-Driven Identity Fraud

Scenario:

- Automated onboarding system relies on selfie/video verification.
- Synthetic media bypasses weak liveness checks.

Mitigation stack:

- Multi-factor verification.
- Deepfake detection signals.
- Risk-tiered manual escalation.

### Exceptions

- Not every internal low-stakes model needs heavy red-team investment.
- High-stakes external-facing systems require recurring adversarial evaluation, not one-time tests.

## Interview Questions & Answers

1. **Q:** What is adversarial ML?
   **A:** The study of attacks and defenses for ML systems under strategic manipulation.

2. **Q:** What is the difference between reliability and security?
   **A:** Reliability addresses benign failures; security addresses adversarial failures.

3. **Q:** Explain white-box vs black-box attack.
   **A:** White-box attackers know model internals; black-box attackers only observe inputs/outputs.

4. **Q:** What is an evasion attack?
   **A:** An inference-time input manipulation that causes incorrect model output.

5. **Q:** What is data poisoning?
   **A:** Corruption of training data to degrade model quality or implant targeted behavior.

6. **Q:** What is a backdoor attack?
   **A:** A poisoning attack where a hidden trigger causes attacker-chosen outputs.

7. **Q:** What is model extraction?
   **A:** Reconstructing a substitute model from API queries to steal behavior/IP.

8. **Q:** What is membership inference?
   **A:** Inferring whether specific records were present in training data.

9. **Q:** Why is adversarial training useful?
   **A:** It improves robustness by exposing models to attack-like perturbations during training.

10. **Q:** Is adversarial training enough?
    **A:** No. It should be combined with detection, access control, monitoring, and incident response.

11. **Q:** What is attack success rate (ASR)?
    **A:** The fraction of attacked inputs for which the attacker achieves target failure.

12. **Q:** Why is calibration relevant in security?
    **A:** Overconfident wrong predictions make attacks more damaging and harder to detect.

13. **Q:** How do you secure a model API?
    **A:** AuthN/AuthZ, rate limiting, input validation, anomaly detection, and request logging.

14. **Q:** How can prompt injection relate to adversarial ML?
    **A:** It is an adversarial input attack against LLM behavior and tool-use policies.

15. **Q:** What is AI supply chain risk?
    **A:** Tampered datasets, model artifacts, dependencies, or deployment scripts compromising system integrity.

16. **Q:** When should you run adversarial tests?
    **A:** Before launch and continuously after updates, retraining, or major traffic shifts.

17. **Q:** Why use MITRE ATLAS?
    **A:** It offers a structured threat taxonomy for AI-specific attack tactics and techniques.

18. **Q:** What is a practical first step for teams new to AI security?
    **A:** Build a minimal threat model and run a focused adversarial test suite on highest-risk endpoints.

19. **Q:** How do you measure defense quality?
    **A:** Compare clean accuracy, robust accuracy, ASR, and operational incident metrics.

20. **Q:** What trade-off is common in robustness engineering?
    **A:** Stronger defenses can reduce throughput or clean accuracy; teams optimize risk-adjusted utility.

## Further Reading and Source-Informed References

- MITRE ATLAS: https://atlas.mitre.org/
- MITRE ATLAS GitHub: https://github.com/mitre/advmlthreatmatrix
- Microsoft Counterfit announcement: https://www.microsoft.com/en-us/security/blog/2021/05/03/ai-security-risk-assessment-using-counterfit/
- Microsoft threat modeling for AI/ML systems: https://learn.microsoft.com/en-us/security/engineering/threat-modeling-aiml
- SANS SEC546 Securing Agentic AI: https://www.sans.org/cyber-security-courses/securing-agentic-ai
- NCSC guidance on adversarial attacks against ML and AI: https://www.ncsc.gov.uk/sites/default/files/2026-05/Understanding-adversarial-attacks-against-Machine-Learning-and-AI.pdf
