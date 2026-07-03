# Overview
Privacy-preserving ML/LLMOps aims to generate model value while minimizing exposure of sensitive data. In healthcare, finance, and public-sector systems, privacy controls are not optional "add-ons"; they are design constraints that shape architecture, operations, and release criteria.

The practical question is rarely "privacy or performance?" It is "which privacy mechanism satisfies legal and risk requirements with acceptable utility and operational complexity?"

# Core Privacy-Preserving Concepts
## Federated learning
Federated learning trains a shared model using decentralized local datasets:
1. initialize global model,
2. distribute model to clients,
3. local client updates,
4. aggregate updates centrally,
5. repeat for multiple rounds.

Variants:
- horizontal FL (same features, different users),
- vertical FL (different features, overlapping users),
- federated transfer patterns.

## Differential privacy (DP)
DP introduces calibrated randomness to limit individual record influence. Teams usually track privacy budget $(\epsilon, \delta)$ and explicitly trade privacy strength against model utility.

## Secure aggregation
Secure aggregation ensures the server can recover aggregate updates without revealing individual client contributions.

Together, federated learning + secure aggregation + DP can form a defense-in-depth privacy posture.

# Threat Model and Risk Mapping
## Threat categories
- data exfiltration from centralized pipelines,
- sensitive memorization in model outputs,
- membership inference attempts,
- unauthorized access to training/evaluation artifacts,
- over-retention of logs and prompts.

## Control mapping
- architecture controls: decentralization, on-device/edge inference, isolated environments,
- cryptographic controls: secure aggregation, encrypted transport/storage,
- operational controls: RBAC, least privilege, audit trails,
- evaluation controls: privacy red-team tests and leakage checks.

# Privacy-Preserving LLMOps Patterns
## Data minimization and lifecycle controls
- collect only fields required for task outcomes,
- enforce retention and deletion policies,
- separate identity data from training corpora,
- tokenize or pseudonymize where feasible.

## Prompt and log handling
- PII scanning/redaction before persistence,
- selective logging by risk tier,
- anonymized analytics for operational dashboards.

## Deployment architecture options
| Pattern | Strength | Trade-off | Typical use |
|---|---|---|---|
| Centralized training + strong controls | Simpler ML iteration | Higher concentration risk | Internal enterprise assistants |
| Federated updates | Better data locality/privacy | More operational complexity | Cross-institution healthcare/finance |
| Edge/local inference | Strong privacy + offline | Device constraints | Mobile/edge assistants |
| Hybrid | Balanced posture | More moving parts | Large regulated deployments |

# Governance and Compliance Integration
Privacy engineering should be tied to governance checkpoints:
- policy-driven data contracts,
- model/data lineage,
- privacy budget and leakage gate before release,
- documented incident response workflow.

Operationally, privacy is successful only when teams can prove controls are active through audit-ready evidence.

# Production Case Studies & Exceptions
## Case 1: Hospital consortium risk modeling
Pattern: federated updates across institutions with secure aggregation and strict identity boundaries.

Impact: improved coverage without centralizing raw patient datasets.

Exception: schema mismatches across institutions reduced convergence and required harmonization projects.

## Case 2: Mobile keyboard personalization
Pattern: on-device adaptation + periodic federated aggregation.

Impact: personalization gains with reduced central raw text exposure.

Exception: heterogeneous hardware/network availability increased training variance.

## Case 3: Regulated credit scoring enhancement
Pattern: privacy-aware feature engineering, redacted logs, and DP-protected shared analytics.

Impact: stronger governance posture and safer cross-team analytics sharing.

Exception: over-aggressive DP settings reduced signal and required feature redesign plus metric re-baselining.

# Interview Questions & Answers
1. **Q:** What is federated learning?  
   **A:** Decentralized collaborative training without moving raw local data to a central store.
2. **Q:** Why use FL?  
   **A:** To learn from distributed sensitive datasets while reducing central data exposure.
3. **Q:** Horizontal vs vertical FL?  
   **A:** Horizontal shares feature space across different samples; vertical shares sample overlap across different feature spaces.
4. **Q:** What is secure aggregation?  
   **A:** A protocol where only aggregate client updates are recoverable.
5. **Q:** What does DP provide?  
   **A:** Formal bounds on individual record influence in outputs.
6. **Q:** Is FL alone enough for privacy?  
   **A:** No; combine with secure aggregation, access controls, and leakage monitoring.
7. **Q:** Main FL operational risk?  
   **A:** Client heterogeneity and unstable participation.
8. **Q:** Why track privacy budget?  
   **A:** It quantifies cumulative privacy loss and supports release gates.
9. **Q:** What is data minimization?  
   **A:** Collecting/storing only data required for explicit objectives.
10. **Q:** Why redact logs?  
    **A:** Operational logs are a major leakage surface in LLM systems.
11. **Q:** Edge inference privacy benefit?  
    **A:** Sensitive data can remain on device, reducing central exposure.
12. **Q:** Key governance artifact?  
    **A:** Audit-ready lineage of data, model versions, and access events.
13. **Q:** Typical anti-pattern?  
    **A:** Treating privacy as a legal checklist rather than an architecture decision.
14. **Q:** How to detect privacy regressions?  
    **A:** Add privacy-specific tests (leakage probes, policy compliance checks) to release gates.
15. **Q:** Why can privacy hurt utility?  
    **A:** Noise and constrained data access can reduce effective learning signal.
16. **Q:** What is least privilege in ML ops?  
    **A:** Restricting access to minimum data/artifacts needed for each role.
17. **Q:** How does privacy connect to incident response?  
    **A:** Faster containment and evidence trails depend on strong logging and ownership controls.
18. **Q:** What is the role of environment separation?  
    **A:** Isolating dev/staging/prod reduces accidental data leakage paths.
19. **Q:** Can small teams adopt privacy-preserving patterns?  
    **A:** Yes, start with minimization, redaction, RBAC, and staged architecture hardening.
20. **Q:** One-line guidance?  
    **A:** Engineer privacy as a measurable system property, not a policy afterthought.

# References
- Google federated learning overview: https://cloud.google.com/discover/what-is-federated-learning
- TensorFlow Federated docs: https://www.tensorflow.org/federated
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
