# Overview

An AI model is a component. An AI product is a socio-technical system that delivers value repeatedly under constraints. Teams fail when they optimize model quality in isolation and underinvest in system design, UX, reliability, and governance.

The design unit should be the full decision workflow, not the model call.

# Product Thinking for AI

## Problem Framing

Use a problem canvas:

1. User job-to-be-done.
2. Pain frequency and severity.
3. Current baseline process (time, cost, error rate).
4. AI leverage point (generation, classification, automation, orchestration).
5. Human oversight needs.

## ROI-Oriented Decision Gate

Before building:

$$
\text{Expected Value} = (\text{Benefit} \times \text{Adoption}) - (\text{Build Cost} + \text{Run Cost} + \text{Risk Cost})
$$

If expected value is weak, avoid forcing AI.

## When AI is the Wrong Tool

- deterministic business rules with stable logic
- very low-volume tasks
- high-stakes decisions without explainability path

# System Architecture Patterns

## Canonical AI Product Architecture

Text diagram:

Frontend -> API Gateway -> Orchestrator -> Model/Agent Services -> Data Stores -> Observability

Core components:

- API contract layer
- orchestration layer (workflow control)
- model runtime(s)
- retrieval and transactional data stores
- logging/tracing/evaluation pipeline

## Monolith vs Microservices

Monolith strengths:

- faster early delivery
- simpler deployment

Microservices strengths:

- independent scaling
- clearer fault isolation

Recommendation for early-stage teams: modular monolith first, then split only proven bottlenecks.

## Latency and Reliability Budgets

Define explicit SLOs:

- p95 response latency
- uptime target
- cost per successful task

Latency budget example:

- retrieval: 200 ms
- model inference: 1200 ms
- tool calls: 600 ms
- post-processing: 100 ms

Total p95 target: 2.1 s

# Non-Functional Requirements

## Cost Engineering

Track:

- tokens/request
- tool invocation count
- cache hit rates
- fallback usage rate

## Security and Privacy

- least-privilege credentials for tools
- PII redaction in logs
- tenant isolation
- secrets management

## Compliance and Governance

- audit trails for key decisions
- approval flows for sensitive actions
- retention and deletion policies

## Observability

Capture:

- prompts and response metadata
- tool call traces
- failure taxonomy
- user feedback signals

# Design for Failure & Safety

## Failure-Aware Architecture

Define failures by layer:

1. retrieval failure
2. model uncertainty
3. tool timeout
4. policy violation

For each failure define:

- detection method
- fallback behavior
- escalation owner

## Human-in-the-Loop Patterns

1. pre-action approval for high-risk actions
2. post-action audit for medium-risk workflows
3. full autonomy for low-risk repetitive tasks

## Safety Guardrails

- policy classifier before action execution
- blocked tool scopes by role
- output schema validation
- abuse and prompt injection defenses

# AI Product Roadmap Pattern

A practical roadmap:

1. Problem discovery and baseline metrics.
2. Pilot prototype with narrow scope.
3. Instrumented beta with human review.
4. Controlled production rollout.
5. Continuous optimization with eval loops.

Each stage requires explicit go/no-go criteria.

# Business Case Studies & Exceptions

## Case Study 1: Agentic Workflow Assistant

A B2B SaaS company built an assistant to orchestrate onboarding tasks across CRM, ticketing, and docs systems.

What worked:

- clear scope (onboarding only)
- strict action contracts
- approval gates for account-level changes

Outcome:

- onboarding cycle time dropped
- fewer dropped handoffs

## Case Study 2: Cost Blow-Up Failure

A team launched an LLM assistant without token budgets, caching, or routing logic.

Result:

- inference costs spiked 4x in six weeks
- latency exceeded UX tolerance

Fix:

- caching repeated retrievals
- model tiering (cheap router, strong generator)
- response-length controls

## Exceptions

- Some regulated workloads require human ownership of final decisions regardless of model quality.
- Certain enterprise stacks demand on-prem deployment even if cloud is cheaper.

# Interview Questions & Answers

1. **How is AI product design different from model development?**  
AI product design optimizes end-to-end value delivery under operational constraints, not just model metrics.

2. **What is the first system design artifact for an AI product?**  
A workflow-level architecture showing data flow, model calls, and decision checkpoints.

3. **When should you reject an AI solution?**  
When deterministic systems solve the problem better on cost, risk, or reliability.

4. **What non-functional requirements matter most?**  
Latency, cost, security, reliability, auditability, and compliance.

5. **How do you control AI cost in production?**  
Caching, routing to cheaper models, token budgets, and pruning unnecessary calls.

6. **What is modular monolith strategy?**  
One deployable service with strict internal module boundaries, enabling future service split.

7. **Why include human-in-the-loop?**  
To reduce risk on high-impact decisions and capture corrective feedback.

8. **How do you design fallback behavior?**  
Define deterministic alternatives and escalation paths per failure type.

9. **What is a good AI product SLO set?**  
Task success rate, p95 latency, error rate, and cost per successful task.

10. **How do you prevent data leakage?**  
Scoped access control, PII masking, and strict tenancy boundaries.

11. **How do you test an AI system before launch?**  
Offline eval suite, adversarial prompts, staging traffic replay, and human QA.

12. **What architecture supports long-running workflows best?**  
State-aware orchestrators with checkpoints, retries, and resumable execution.

13. **When should microservices be adopted?**  
After clear scaling, ownership, or isolation bottlenecks appear.

14. **How do you align with business stakeholders?**  
Tie technical metrics directly to business KPIs and risk thresholds.

15. **What is the biggest product mistake in AI teams?**  
Shipping model demos without operational and UX reliability.

# References

- NYU Stern Foundations of AI Agents: https://aiagents.stern.nyu.edu/
- DeepLearning.AI Agentic AI course: https://www.deeplearning.ai/courses/agentic-ai
- Harvard Online Agentic AI Foundations: https://harvardonline.harvard.edu/course/agentic-ai-foundations
- IITM Pravartak Applied AI with Context Engineering: https://futurense.com/iitm-pravartak/advanced-engineering-program-in-applied-ai-ml-with-context-engineering
- Google Cloud Generative AI architecture guides: https://docs.cloud.google.com/architecture/genai-overview?hl=en
- Google Cloud enterprise GenAI and MLOps blueprint: https://docs.cloud.google.com/architecture/blueprints/genai-mlops-blueprint
- NVIDIA OpenShell security-by-design post: https://blogs.nvidia.com/blog/secure-autonomous-ai-agents-openshell/
