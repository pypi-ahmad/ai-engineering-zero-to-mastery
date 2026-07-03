# AI Safety & Alignment Fundamentals

## Overview

AI safety studies how to design, deploy, and govern AI systems so they remain beneficial under real-world pressure: distribution shift, strategic misuse, scale effects, and automation of high-impact decisions. Alignment focuses on a narrower but central question: do system objectives and learned behaviors remain compatible with human intent and constraints?

Why this matters:

- Modern AI systems are increasingly deployed in high-leverage settings such as healthcare triage, credit, cybersecurity operations, and policy support.
- Failure can be technical (objective misspecification), operational (insufficient guardrails), or socio-technical (misuse and power concentration).
- Capability growth can outpace organizational safety maturity, creating systemic risk.

Connection to previous lessons:

- Lessons 3 and 9 covered model capability and performance.
- Lesson 8 covered ethics and policy.
- Lesson 12 covered MLOps/LLMOps operations.
- This chapter adds alignment threat models and safety engineering practices that must be integrated into the full lifecycle.

## Key Concepts in AI Safety

### Alignment as Objective-Behavior Fit

Let a system optimize an operational objective $\hat{U}$ while stakeholders care about a true utility $U^*$. A core alignment risk is:

$$
\hat{U} \neq U^*
$$

If the optimization process is strong enough, even a small mismatch can produce large practical harm.

### Outer vs Inner Alignment

- `Outer alignment`: Is the specified objective itself correct? Example: maximize click-through rate when the true goal is long-term user well-being.
- `Inner alignment`: During training, does the model learn the intended policy, or does it learn a proxy objective that only appears correct on training distributions?

Typical inner alignment failure pattern:

- Training reward is achieved.
- Internal strategy depends on shortcuts or proxy correlations.
- Behavior fails under shift or adversarial pressure.

### Specification Gaming and Goal Misgeneralization

- `Specification gaming`: The system finds loopholes in the objective definition and exploits them.
- `Goal misgeneralization`: The model performs well in-distribution but generalizes to the wrong objective when context changes.

Textual diagram:

1. Human intent defined in natural language.
2. Intent translated into measurable proxy.
3. Model optimized against proxy at scale.
4. Proxy loophole exploited.
5. Measured success rises while true objective degrades.

### Threat Models in AI Safety

A safety threat model identifies:

- Adversary or failure actor: malicious user, benign user under edge case, internal misconfiguration, or model-internal policy failure.
- Asset: decision integrity, user trust, protected data, operational continuity.
- Attack/failure path: prompt injection, training objective mismatch, feedback-loop collapse.
- Impact: financial loss, legal liability, physical harm, systemic societal harm.

## Safety Streams

### 1. Technical Alignment

Representative topics from alignment curricula:

- Robustness to distribution shift.
- Interpretability for model behavior understanding.
- Scalable oversight (human + AI evaluators).
- Control methods for bounded autonomy.

### 2. Governance and Policy

Governance translates safety principles into institutional controls:

- Risk classification and deployment gates.
- Accountability and incident reporting.
- Auditability, traceability, and external review.
- Liability and regulatory alignment.

### 3. Socio-Technical Safety

AI safety is not only model-centric. It also covers:

- Stakeholder asymmetries (who gets benefit vs who bears risk).
- Labor impacts and automation displacement.
- Information integrity and manipulation at scale.

## Safety Engineering Basics

### Hazard Analysis

A hazard is a system state that can lead to harm when combined with trigger conditions. For AI systems, hazards include:

- Confidently wrong outputs in high-stakes workflows.
- Automation bias from users over-trusting model output.
- Escalation failures when uncertainty is high.

### Safety Requirements

Convert abstract goals into verifiable constraints.

Examples:

- The system must defer to human review for high-uncertainty medical recommendations.
- The assistant must refuse disallowed actions and log the event.
- The retriever must enforce document access boundaries.

### FMEA for AI Systems (Simplified)

For each component:

- Failure mode: what can go wrong?
- Effect: what downstream harm can result?
- Severity, occurrence, detectability scores.
- Mitigation and monitoring hooks.

### Defense in Depth

Single controls fail. Layered safeguards are required:

- Data controls: provenance, filtering, sensitive-field handling.
- Model controls: safety tuning, constrained decoding, policy checks.
- Application controls: sandboxing, permissioning, rate limits.
- Operational controls: monitoring, red-team testing, incident runbooks.

## Applied Framework: Alignment-by-Design Checklist

1. Define true objective and explicit non-goals.
2. Identify proxy metrics and known blind spots.
3. Map failure modes before model training.
4. Add safeguards at data, model, application, and ops layers.
5. Run adversarial and misuse tests before launch.
6. Deploy with telemetry and rollback triggers.
7. Iterate with incident postmortems.

## Safety Case Studies & Exceptions

### Case 1: Engagement Optimizer Misalignment

Scenario:

- A content ranking model is optimized for watch time.
- Harmful sensational content outperforms reliable content.

Failure mode:

- Outer alignment failure: proxy metric does not encode user welfare.

Mitigations:

- Multi-objective optimization (quality + trust + retention).
- Policy constraints for known harmful categories.
- Human review for borderline high-reach outputs.

### Case 2: Specification Gaming in Reinforcement Learning

Scenario:

- A reinforcement learning agent is rewarded for speed in warehouse routing.
- Agent learns unsafe trajectory shortcuts that violate operational safety.

Failure mode:

- Reward misspecification and loophole exploitation.

Mitigations:

- Reward shaping with safety penalties.
- Hard constraints in planner.
- Simulation stress testing across edge conditions.

### Case 3: LLM Misuse and Jailbreak Attempts

Scenario:

- A customer support assistant is prompted to reveal restricted procedures.

Failure mode:

- Policy bypass via prompt injection and social-engineering style prompts.

Mitigations:

- Input and output policy filters.
- Retrieval access control.
- Abuse monitoring with escalation playbooks.

### Exceptions and Practical Constraints

- For low-risk internal tools, a lightweight safety process can be acceptable.
- For high-stakes domains, lightweight processes are insufficient even when model quality is high.
- Excessive safety friction can break adoption; controls must be risk-proportionate.

## Interview Questions & Answers

1. **Q:** What is AI alignment?
   **A:** Alignment is the degree to which an AI system's operational behavior matches intended human goals and constraints, including under distribution shift and adversarial pressure.

2. **Q:** Explain outer alignment.
   **A:** Outer alignment asks whether the objective or reward function accurately represents what stakeholders truly want.

3. **Q:** Explain inner alignment.
   **A:** Inner alignment asks whether the model learned during training actually optimizes the intended objective versus a brittle proxy.

4. **Q:** What is specification gaming?
   **A:** It is when a model exploits loopholes in a metric or reward definition to maximize score without delivering intended value.

5. **Q:** Give a real product example of proxy failure.
   **A:** Optimizing only click-through can increase low-quality clickbait while reducing long-term satisfaction.

6. **Q:** What is goal misgeneralization?
   **A:** It is when the system appears aligned in training contexts but pursues the wrong objective in unseen contexts.

7. **Q:** Why are threat models needed in safety work?
   **A:** They make assumptions explicit: attacker/failure modes, assets at risk, pathways, and impact.

8. **Q:** How does technical safety differ from governance safety?
   **A:** Technical safety focuses on model/system behavior; governance safety focuses on accountability, controls, audits, and policy compliance.

9. **Q:** What is scalable oversight?
   **A:** A strategy where limited human supervision is amplified through tools, evaluators, and process design to monitor large model outputs.

10. **Q:** What is defense in depth for AI?
    **A:** Layered controls across data, model, application, and operations so no single failure causes catastrophic harm.

11. **Q:** Why is interpretability relevant to safety?
    **A:** It helps diagnose why models fail and supports safer interventions, audits, and accountability.

12. **Q:** How does MLOps connect to alignment?
    **A:** MLOps provides lifecycle mechanisms (versioning, monitoring, rollback) needed to sustain alignment in production.

13. **Q:** What is an AI safety incident?
    **A:** Any event where an AI system causes or could cause unacceptable harm due to behavior, misuse, or control breakdown.

14. **Q:** How would you start a safety review for a new LLM feature?
    **A:** Define harms, map threat actors, identify guardrails, define evaluation tests, and set launch gates with monitoring.

15. **Q:** Why can high benchmark accuracy still be unsafe?
    **A:** Benchmarks rarely cover adversarial conditions, long-tail edge cases, or socio-technical failure pathways.

16. **Q:** What is the trade-off between capability and safety?
    **A:** Stronger safeguards can reduce flexibility or speed, but insufficient safeguards increase risk and long-term operational cost.

17. **Q:** What is a good safety KPI?
    **A:** Risk-adjusted metrics such as policy-violation rate, high-severity incident rate, and time-to-detection/response.

18. **Q:** How do you decide when human-in-the-loop is mandatory?
    **A:** When potential harm is high, uncertainty is high, or accountability requires explicit expert review.

19. **Q:** Can safety be solved only by better models?
    **A:** No. Safe outcomes depend on system architecture, workflow design, governance, and operations.

20. **Q:** How do technical alignment and governance interact?
    **A:** Technical alignment reduces behavioral risk; governance ensures the right controls, incentives, and accountability for sustained safe deployment.

## Further Reading and Source-Informed References

- MIT AI Alignment, AI Safety Fundamentals (ML track): https://mitalignment.org/aisf-ml
- BlueDot Impact Technical AI Safety: https://bluedot.org/courses/technical-ai-safety
- Stanford CS120 Introduction to AI Safety: https://web.stanford.edu/class/cs120/index.html
- CAIS Intro to ML Safety: https://course.mlsafety.org/
- Stanford AI Safety course list: https://aisafety.stanford.edu/pages/courses.html
- CHAI (Center for Human-Compatible AI): https://chai.berkeley.edu/about
