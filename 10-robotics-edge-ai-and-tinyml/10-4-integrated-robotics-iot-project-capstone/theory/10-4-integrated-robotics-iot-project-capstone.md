# Overview

This capstone integrates robotics control, perception/planning, and edge AI deployment into a single applied system. The goal is not maximal complexity; the goal is a coherent, testable, and portfolio-ready engineering artifact.

Core integration objective:

- sensing + edge inference + control + logging + reliability design.

A strong capstone here should demonstrate system thinking across the full loop, not isolated model scores. Reviewers should be able to see how sensing uncertainty propagates into planning/control decisions and how telemetry closes the loop for operations. Even in simulation, your design should reflect real deployment pressures: constrained compute, non-ideal sensors, intermittent connectivity, and safety fallbacks.

# Suggested Capstone Project Briefs

## Option 1: Smart Home TinyML Sensor Network

- Devices detect wake-word/gesture/activity locally.
- Edge gateway aggregates events and triggers automations.
- Cloud dashboard tracks reliability, false alarms, and device health.

## Option 2: Simulated Warehouse Robot

- Grid-map navigation with A* planner.
- Basic perception hook (obstacle detection proxy).
- Controller executes path with disturbance handling.

## Option 3: IoT Vibration Monitor with Edge Anomaly Detection

- Sensor stream from motor-like signal generator.
- Tiny classifier detects anomaly classes on device.
- Alert pipeline with severity and maintenance recommendations.

Selection guidance:
- Choose the project where you can produce the strongest end-to-end evidence in available time.
- Prefer one complete workflow over multiple half-built prototypes.
- Keep one explicit fallback mode in scope from day one.

# Architecture Templates

## Template A: Device -> Edge -> Cloud

1. Sensor node captures data.
2. Edge model performs local inference.
3. Controller executes action.
4. Cloud logger stores telemetry and events.
5. Monitoring service raises alerts and rollout decisions.

## Template B: Robotics Navigation Stack

1. Perception node updates occupancy representation.
2. Localizer estimates pose.
3. Planner computes route.
4. Controller generates velocity commands.
5. Safety supervisor enforces guardrails.

## Template C: TinyML Fleet Management

1. Data collection and labeling pipeline.
2. Model compression and export pipeline.
3. OTA deployment with staged rollout.
4. Device health and model drift dashboards.

# Implementation Roadmap

Suggested implementation phases:

1. Simulated prototype with deterministic inputs.
2. Controller + inference integration.
3. Reliability and disturbance testing.
4. Edge optimization and deployment packaging.
5. Monitoring and alert workflow integration.

Phase template:

```text
Phase objective:
Hardware/simulation assumptions:
Primary KPI:
Safety gate:
Exit criteria:
```

# Evaluation Criteria

## Technical Completeness

- clear architecture,
- runnable demo,
- reproducible environment setup.

## Robustness and Monitoring

- failure-mode handling,
- telemetry and logging,
- alerting and rollback plan.

## Domain Constraints

- latency target,
- power/footprint budget,
- safety and reliability boundaries.

## Communication Quality

- concise README,
- architecture diagram,
- measurable results and limitations.

# Capstone Scoring Rubric

| Dimension | Weight | Evidence |
|---|---:|---|
| Problem framing and scope realism | 15% | clear domain constraints and success criteria |
| System architecture and implementation | 25% | integrated sensing-inference-control pipeline |
| Evaluation and robustness | 20% | stress tests, failure handling, reliability metrics |
| Deployment and ops readiness | 20% | edge packaging, telemetry, and incident response plan |
| Documentation and presentation | 20% | reproducible artefacts and clear technical narrative |

# Pitfalls & Guidance

## Scope Management

- choose one core workflow and do it well,
- freeze scope early,
- document future extensions instead of building everything.

## Hardware Constraints

- simulate first, then transfer to real device incrementally,
- measure memory and latency from early milestones,
- plan for calibration and sensor-noise handling.

## Portfolio Packaging

Deliverables should include:

- short problem statement,
- architecture and trade-offs,
- before/after metrics,
- demo artifact (video or notebook),
- lessons learned.

# Documentation, Presentation, and Reflection

Required documentation package:

- component diagram (sensor, edge model, controller, logger),
- deployment assumptions (simulation/hardware),
- evaluation report (accuracy + latency + reliability),
- safety and fallback behavior notes,
- operations checklist for incident response.

Final presentation flow:

1. Domain problem and constraints.
2. System architecture and control loop.
3. Edge trade-offs (performance vs power/latency).
4. Reliability and safety evidence.
5. What would be needed for real-world rollout.

Reflection prompts:

- Which constraint (power, latency, noise, safety) was hardest?
- What simplified design choice improved robustness most?
- What would be your first production hardening milestone?

# Capstone Case Studies & Exceptions

## Case Study 1: Warehouse Robot Capstone That Passed Demo but Failed Stress Test

Scenario:
A team built a simulated warehouse robot with path planning and PID control. Demo runs were successful, but reliability dropped under noisy sensing and dynamic obstacles.

Failure pattern:

- planner assumed static map,
- controller tuned only for nominal conditions,
- no watchdog/fallback mode.

Remediation:

- add periodic replanning with obstacle updates,
- include disturbance-injection tests in evaluation,
- implement safety stop and degraded-mode behavior.

## Case Study 2: TinyML Sensor Network with Strong Accuracy but Weak Operations

Scenario:
An edge anomaly detector achieved good offline F1 but generated frequent false alarms in deployment.

Root causes:

- concept drift from seasonal machine behavior,
- no threshold governance per site/equipment type,
- weak telemetry granularity.

Remediation:

- add site-level calibration and drift-aware thresholding,
- log model version + confidence + device health per event,
- create retraining trigger policy.

Exception:
In low-stakes monitoring workflows, periodic human review may be a cheaper first step than full closed-loop retraining.

## Case Study 3: Smart Home Automation with Privacy Constraints

Scenario:
Voice/gesture models worked well, but cloud sync design risked exposing sensitive household activity patterns.

Practical redesign:

- edge-first inference by default,
- send only aggregated/anonymized events upstream,
- provide explicit user controls for retention and sharing.

Lesson:
Capstone evaluation should include privacy and operational safety constraints, not only predictive metrics.

# Capstone Readiness Checklist

- Core workflow is end-to-end runnable (sensor/perception -> inference -> action -> logging).
- Architecture includes clear fallback behavior.
- Metrics cover both model quality and system reliability.
- Domain constraints (latency/power/safety/privacy) are explicitly tested.
- Demo artefacts and reproducibility instructions are complete.

# Interview Questions & Answers

1. **Describe your robotics/IoT capstone in one minute.**  
State problem, architecture, key constraints, and measurable outcomes.

2. **Q: How did you handle edge constraints?**
   **A:** Used model compression, measured memory/latency, and tuned design to device limits.

3. **Q: Why did you choose edge inference instead of cloud-only?**
   **A:** To meet latency/offline/privacy requirements.

4. **Q: How did you validate reliability?**
   **A:** Scenario tests, disturbance injections, and telemetry-based monitoring.

5. **Q: What was your biggest technical trade-off?**
   **A:** Balancing model accuracy against footprint and response-time constraints.

6. **Q: How did you design monitoring?**
   **A:** Logged model version, prediction confidence, latency, and error events.

7. **Q: What would you improve with more time?**
   **A:** Stronger dataset diversity, better failure recovery, and automated deployment tests.

8. **Q: How did you manage safety risk?**
   **A:** Added rule-based guardrails and fallback behaviors for uncertain states.

9. **Q: How does this project map to production systems?**
   **A:** Same architecture pattern with stronger tooling, security, and governance controls.

10. **Q: What did this capstone teach you about real-world AI?**
   **A:** System integration and reliability matter as much as model performance.

11. **Q: How did you select evaluation metrics?**
   **A:** Combined model metrics with system metrics (latency, uptime, false alarm rate).

12. **Q: How do you justify ROI of robotics/edge AI deployments?**
    **A:** Compare baseline manual process vs automated throughput, downtime reduction, and risk reduction.

13. **Q: What is the minimum evidence set for a credible robotics/IoT capstone?**
    **A:** Runnable pipeline, reliability metrics, failure-handling behavior, and reproducible setup/documentation.

14. **Q: Why is simulation-first still valuable for portfolio quality?**
    **A:** It demonstrates architecture, control reasoning, and evaluation discipline before hardware scaling.

15. **Q: How do you show production thinking without real-device deployment?**
    **A:** Include deployment assumptions, telemetry design, rollback/fallback strategy, and incident-response checklist.
# References

- NVIDIA DLI Edge AI and Robotics Teaching Kit syllabus: https://developer.nvidia.com/edge-ai-robotics-teaching-kit-syllabus
- NVIDIA teaching-kit blog: https://developer.nvidia.com/blog/nvidia-launches-teaching-kit-for-edge-ai-and-robotics-educators/
- UCLA IoT capstone examples: https://www.meng.ucla.edu/2023-ucla-master-of-engineering-iot-capstone-projects/
- Harvard TinyML certificate description: https://harvardonline.harvard.edu/program/professional-certificate-in-tiny-machine-learning-tinyml
- TensorFlow Lite Micro docs: https://www.tensorflow.org/lite/microcontrollers

## Bridge to Next Lesson

- **What you now know:** You can scope and design integrated robotics/IoT solutions with perception, planning, control, and edge deployment constraints.
- **Why the next lesson follows:** The next lesson follows because technical delivery alone is not enough; product strategy, venture thinking, and research literacy shape real-world impact.
- **What you'll build next:** You will build AI product management, entrepreneurship, and AI-for-science research-method workflows tied to practical execution.
