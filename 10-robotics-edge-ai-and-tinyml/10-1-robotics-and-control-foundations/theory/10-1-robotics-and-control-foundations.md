# Overview

A robot is a physical system that senses the environment, computes decisions, and acts through actuators. In applied engineering, robotics sits at the intersection of three disciplines:

1. mechanical and electrical systems,
2. control theory,
3. AI/perception/planning.

A compact architecture is:

- Sensors -> State Estimation -> Planner/Policy -> Controller -> Actuators -> Environment.

Relationship between AI, control, and robotics:

- AI handles perception, prediction, and decision-making in uncertain environments.
- Control handles stable execution of desired trajectories and setpoints.
- Robotics integrates both into real-time physical systems with safety constraints.

# Kinematics & Dynamics (High Level)

## Configuration Space, Joints, and Degrees of Freedom

Configuration space (C-space) represents all possible robot configurations. Each independent joint variable contributes one degree of freedom (DoF).

Examples:

- Differential-drive mobile base: typically 3 DoF in planar pose (x, y, heading).
- Industrial manipulator: commonly 6 DoF for full 3D pose control.

## Forward vs Inverse Kinematics

- Forward kinematics (FK): joint values -> end-effector pose.
- Inverse kinematics (IK): desired end-effector pose -> joint values.

FK is usually straightforward; IK may have multiple, zero, or infinite solutions depending on geometry and constraints.

## Dynamics Intuition

Dynamics connects motion and force:

- torque drives joint acceleration,
- inertia, friction, and gravity shape response,
- control inputs must account for these effects.

In real robots, the same command can behave differently as payload, friction, or battery state changes.

# Control Basics

## Feedback Control

Feedback compares desired state and measured state, then corrects error.

Error definition:

$$
error(t) = target(t) - measured(t)
$$

Why feedback matters:

- rejects disturbances,
- compensates for modeling inaccuracies,
- improves repeatability and robustness.

## PID Controllers

PID combines three terms:

- P (proportional): reacts to current error.
- I (integral): corrects accumulated bias.
- D (derivative): damps rapid changes.

Control law:

$$
u(t)=K_p e(t)+K_i \int e(t)dt + K_d \frac{de(t)}{dt}
$$

## Stability and Response

Practical tuning focuses on:

- rise time,
- overshoot,
- settling time,
- steady-state error.

Too much P can overshoot, too much I can oscillate (integral windup), too little D can reduce damping.

# Robot Architectures

## Mobile Robots, Manipulators, Drones

- Mobile robots: logistics, delivery, inspection.
- Manipulators: assembly, welding, pick-and-place.
- Drones/UAVs: surveying, monitoring, delivery in constrained airspace.

## On-board vs Off-board Compute (Edge vs Cloud)

On-board (edge) advantages:

- low latency,
- works offline,
- privacy/control.

Cloud/off-board advantages:

- larger model capacity,
- centralized coordination,
- easier fleet-wide updates.

Most production systems use hybrid architectures: safety-critical loops on edge, heavy analytics in cloud.

# Business Case Studies & Exceptions

## Case Study 1: Warehouse Mobile Robots

Problem:

- route goods efficiently while avoiding collisions and congestion.

System pattern:

- local feedback control for wheel velocity,
- global task allocation from fleet manager,
- edge inference for obstacle detection.

Trade-off:

- aggressive speed improves throughput but increases safety risk and navigation error.

## Case Study 2: Industrial Manipulators in Manufacturing

Problem:

- high-precision repeated motion under variable payloads.

System pattern:

- calibrated kinematic model,
- tight feedback control,
- vision guidance for part alignment.

Exception:

- for ultra-high precision tasks, classical control with rigorous calibration may outperform complex AI controllers.

# Interview Questions & Answers

1. **Explain feedback control in simple terms.**  
It measures error between target and actual state, then continuously corrects actuator commands to reduce that error.

2. **Forward vs inverse kinematics?**  
Forward maps joint values to pose; inverse computes joint values needed for a desired pose.

3. **What is a degree of freedom?**  
An independent variable needed to define robot configuration.

4. **What does the P term do in PID?**  
Applies correction proportional to current error.

5. **What does the I term do?**  
Removes persistent steady-state error by accumulating past error.

6. **What does the D term do?**  
Predicts error trend and adds damping to reduce overshoot.

7. **What is overshoot?**  
When the response exceeds target before settling.

8. **Why can integral windup be harmful?**  
Integral term accumulates excessively under saturation, causing instability/slow recovery.

9. **How does AI integrate into robotics?**  
AI supports perception/planning, while control executes safe physical behavior.

10. **On-board vs cloud control trade-off?**  
On-board gives low latency and reliability; cloud gives scale and heavier compute.

11. **Why is latency critical in robotics?**  
Control loops must update quickly to remain stable and safe.

12. **What is C-space used for?**  
Planning feasible motion while respecting robot geometry and joint limits.

13. **Why are models alone insufficient in robotics?**  
Real hardware has disturbances, noise, and nonideal dynamics requiring feedback.

14. **What is a common robotics deployment failure?**  
Good simulation performance but poor real-world robustness due to unmodeled dynamics.

15. **When should simple controllers be preferred over learned policies?**  
In tightly bounded repetitive tasks where interpretability and certification matter.

# References

- Modern Robotics specialization (mechanics/planning/control outcomes): https://www.coursera.org/specializations/modernrobotics
- MIT Underactuated Robotics notes: https://underactuated.csail.mit.edu/
- NVIDIA Edge AI and Robotics Teaching Kit syllabus: https://developer.nvidia.com/edge-ai-robotics-teaching-kit-syllabus
- NVIDIA edge AI robotics teaching-kit blog: https://developer.nvidia.com/blog/nvidia-launches-teaching-kit-for-edge-ai-and-robotics-educators/
