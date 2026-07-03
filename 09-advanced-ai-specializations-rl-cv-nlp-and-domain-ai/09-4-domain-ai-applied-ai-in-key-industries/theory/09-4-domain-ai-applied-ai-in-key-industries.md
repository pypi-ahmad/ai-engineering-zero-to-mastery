# Overview

Domain specialization is where generic AI skill becomes business value. The same model family behaves very differently across industries because data quality, constraints, regulation, risk tolerance, and operational environments vary.

A useful principle:

$$
\text{Domain AI Success} = \text{Model Quality} \times \text{Domain Fit} \times \text{Operational Readiness}
$$

This chapter covers four representative domains:

1. healthcare,
2. finance,
3. smart cities,
4. robotics and autonomous systems.

# Domain Patterns

## Healthcare AI

### Typical data types

- EHR tabular records,
- clinical notes,
- medical imaging,
- biosignal time-series.

### Common tasks

- risk prediction and triage,
- clinical documentation support,
- diagnostic image analysis,
- care pathway optimization.

### Constraints

- patient safety,
- privacy and consent,
- explainability and clinician trust,
- validation requirements across populations.

## Finance AI

### Typical data types

- transactions/events,
- customer profiles,
- market time-series,
- text (filings/news/research).

### Common tasks

- fraud detection,
- credit risk scoring,
- portfolio optimization,
- compliance surveillance.

### Constraints

- regulatory audits,
- fairness and adverse action requirements,
- strict latency for risk controls,
- high cost of false positives/negatives.

## Smart Cities AI

### Typical data types

- traffic sensors,
- camera streams,
- IoT infrastructure telemetry,
- weather and mobility data.

### Common tasks

- traffic forecasting and signal optimization,
- predictive maintenance of infrastructure,
- public safety anomaly detection,
- energy optimization.

### Constraints

- multi-agency governance,
- privacy and surveillance concerns,
- edge inference and reliability,
- heterogeneous legacy infrastructure.

## Robotics and Control

### Typical data types

- multimodal sensor streams (vision, lidar, imu),
- control and telemetry logs,
- simulation rollouts.

### Common tasks

- navigation and planning,
- manipulation and grasping,
- adaptive control,
- human-robot collaboration.

### Constraints

- safety-critical real-time control,
- sim-to-real transfer gap,
- hardware reliability and maintenance costs.

# Example Architectures

## 1) Clinical Decision Support Architecture

- data ingestion (EHR + notes + imaging),
- feature/embedding service,
- prediction + explanation layer,
- clinician-facing UI with override,
- monitoring + post-deployment outcome tracking.

## 2) Fraud Detection Architecture

- streaming transaction ingestion,
- feature store (behavioral + graph features),
- hybrid model stack (rules + ML anomaly scorer),
- real-time decision engine,
- case management and feedback loop.

## 3) Smart City Monitoring Architecture

- edge sensor/camera ingestion,
- event stream processing,
- CV/time-series models for anomalies,
- control center dashboard,
- predictive maintenance ticketing.

## 4) Robotics AI Architecture

- simulator for safe pretraining,
- policy/perception stack,
- runtime safety supervisor,
- fleet telemetry and policy update loop.

# Business Case Studies & Exceptions

## Case Study 1: Clinical Deterioration Early Warning

Scenario:

- Hospital predicts patient deterioration risk in the next 12 hours.

System design:

- time-series model on vitals/labs,
- uncertainty-aware risk bands,
- mandatory physician review before intervention.

Trade-off:

- maximizing sensitivity can overwhelm staff with alerts; calibration and triage routing are critical.

## Case Study 2: Real-Time Card Fraud Detection

Scenario:

- Payments network needs sub-second fraud decisions.

Design pattern:

- layered decisions: hard rules + ML risk score + adaptive thresholding by segment.

Trade-off:

- aggressive blocking reduces fraud but increases customer friction and false declines.

## Case Study 3: Smart Traffic Optimization

Scenario:

- City optimizes signal timing using live camera/sensor inputs.

Benefits:

- lower congestion and emissions.

Risks:

- outages or wrong predictions can cause broad disruptions.

Mitigation:

- fail-safe fixed timing plans, health checks, and staged rollout by corridor.

## Case Study 4: Warehouse Robotics Allocation

Scenario:

- RL policy assigns pick routes for autonomous robots.

Benefits:

- throughput gains under dynamic demand.

Constraints:

- safety envelopes and collision avoidance dominate pure reward maximization.

## Exceptions

- In highly regulated contexts, interpretable models may be preferred over marginally better black-box performance.
- When data drift is extreme and labels lag heavily, human-led workflow redesign can outperform model-first approaches.

# Interview Questions & Answers

1. **Q: Why does domain specialization matter in AI engineering?**
   **A:** Because constraints, data properties, and failure costs differ sharply by domain.

2. **Q: How would you design an AI system for healthcare triage?**
   **A:** Use multimodal patient data, calibrated risk outputs, clinician oversight, and outcome monitoring.

3. **Q: What are key constraints in finance AI?**
   **A:** Regulatory compliance, auditability, fairness, and low-latency risk decisions.

4. **Q: What makes smart city AI difficult?**
   **A:** Heterogeneous infrastructure, privacy concerns, and multi-stakeholder governance.

5. **Q: What is sim-to-real gap in robotics?**
   **A:** Difference between simulation-trained behavior and real-world performance.

6. **Q: How do you evaluate domain AI beyond model accuracy?**
   **A:** Use domain KPIs, operational reliability, safety incidents, and stakeholder acceptance.

7. **Q: Why use hybrid rule+ML systems in finance?**
   **A:** Rules provide hard guarantees while ML handles complex patterns.

8. **Q: How do you reduce alert fatigue in clinical AI systems?**
   **A:** Calibrate thresholds, prioritize precision in specific workflows, and route alerts by severity.

9. **Q: When is RL appropriate in operations?**
   **A:** When decisions have long-term sequential impact and environment feedback is rich.

10. **Q: What is a common deployment failure in domain AI?**
   **A:** Ignoring process integration and human workflow constraints.

11. **Q: How do you adapt a generic AI skillset to a new industry?**
   **A:** Learn domain objectives, regulations, data semantics, and operational failure costs.

12. **Q: Why is explainability more important in some domains?**
   **A:** Because decisions affect rights, safety, or legal accountability.

13. **Q: How do you structure cross-functional collaboration?**
   **A:** Pair engineers with domain experts, legal/compliance, and operations owners from day one.

14. **Q: What is a practical first step in domain AI discovery?**
   **A:** Map decision points, baseline process metrics, and pain points before choosing models.

15. **Q: How do you move from pilot to production in regulated domains?**
   **A:** Use phased rollout, robust documentation, monitoring, and incident playbooks with clear ownership.
# References

- Stanford AI-assisted healthcare course: https://cs337.stanford.edu/
- Stanford AI in healthcare programs: https://computationalmedicine.stanford.edu/seminars-and-training/stanford-ai-in-healthcare/
- Stanford AIMI course ecosystem: https://aimi.stanford.edu/education/stanford-courses
- MIT Sloan AI in Finance course info: https://executive.mit.edu/artificial-intelligence-for-financial-services.html
- MIT Sloan AI in Finance syllabus PDF: https://mitsloan.mit.edu/sites/default/files/inline-files/2025JA_15.S52_AI%20in%20Finance_Syllabus.pdf
- Smart city AI/traffic and predictive maintenance examples: https://arxiv.org/abs/2502.02821 and https://arxiv.org/abs/2306.04653
- Robotics specialization example (curriculum framing): https://www.iams.uni-stuttgart.de/teaching/specialization-area-robotics/

## Bridge to Next Lesson

- **What you now know:** You now understand how AI design changes across regulated and high-stakes industries, where relationship structure often matters as much as model accuracy.
- **Why the next lesson follows:** The next lesson introduces graph AI and GraphRAG because many enterprise problems require multi-hop relational retrieval, provenance paths, and knowledge-graph reasoning.
- **What you'll build next:** You will build hybrid graph + vector retrieval flows, then move to speech/voice systems before transitioning to robotics and edge AI in Lesson 10.
