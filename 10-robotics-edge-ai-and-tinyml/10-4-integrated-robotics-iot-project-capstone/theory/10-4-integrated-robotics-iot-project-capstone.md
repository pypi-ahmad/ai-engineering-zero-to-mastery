# Overview

This capstone integrates robotics control, perception/planning, and edge AI deployment into a single applied system. The goal is not maximal complexity; the goal is a coherent, testable, and portfolio-ready engineering artifact.

Core integration objective:

- sensing + edge inference + control + logging + reliability design.

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

# Interview Questions & Answers

1. **Describe your robotics/IoT capstone in one minute.**  
State problem, architecture, key constraints, and measurable outcomes.

2. **How did you handle edge constraints?**  
Used model compression, measured memory/latency, and tuned design to device limits.

3. **Why did you choose edge inference instead of cloud-only?**  
To meet latency/offline/privacy requirements.

4. **How did you validate reliability?**  
Scenario tests, disturbance injections, and telemetry-based monitoring.

5. **What was your biggest technical trade-off?**  
Balancing model accuracy against footprint and response-time constraints.

6. **How did you design monitoring?**  
Logged model version, prediction confidence, latency, and error events.

7. **What would you improve with more time?**  
Stronger dataset diversity, better failure recovery, and automated deployment tests.

8. **How did you manage safety risk?**  
Added rule-based guardrails and fallback behaviors for uncertain states.

9. **How does this project map to production systems?**  
Same architecture pattern with stronger tooling, security, and governance controls.

10. **What did this capstone teach you about real-world AI?**  
System integration and reliability matter as much as model performance.

11. **How did you select evaluation metrics?**  
Combined model metrics with system metrics (latency, uptime, false alarm rate).

12. **How do you justify ROI of robotics/edge AI deployments?**  
Compare baseline manual process vs automated throughput, downtime reduction, and risk reduction.

# References

- NVIDIA DLI Edge AI and Robotics Teaching Kit syllabus: https://developer.nvidia.com/edge-ai-robotics-teaching-kit-syllabus
- NVIDIA teaching-kit blog: https://developer.nvidia.com/blog/nvidia-launches-teaching-kit-for-edge-ai-and-robotics-educators/
- UCLA IoT capstone examples: https://www.meng.ucla.edu/2023-ucla-master-of-engineering-iot-capstone-projects/
- Harvard TinyML certificate description: https://harvardonline.harvard.edu/program/professional-certificate-in-tiny-machine-learning-tinyml
- TensorFlow Lite Micro docs: https://www.tensorflow.org/lite/microcontrollers
