# Lesson 6: MLOps & LLMOps: Production AI Systems

Lesson 6 introduces operational foundations for moving ML/LLM work from notebooks into repeatable production workflows.

## Why This Matters

Great models still fail in production without operational discipline. This lesson teaches how to ship with: reproducibility, stable data pipelines, explicit contracts, monitoring, and rollback-ready controls.

## Learning Objectives
- Understand ML lifecycle stages, CI/CD/CT/CM, and artifact/version discipline.
- Build baseline data/feature pipelines, deployment patterns, and drift monitoring.
- Apply first-pass LLMOps patterns for RAG and tool-augmented applications.

## Expected Outcomes

- You can define run metadata and save artifacts so results are reproducible.
- You can design a basic serving contract and a rollback strategy.
- You can write a monitoring policy (alerts + retraining triggers) that avoids noise.

## Start Here (Theory + Notebooks)
- `06-1-mlops-fundamentals-and-lifecycle/theory/06-1-mlops-fundamentals-and-lifecycle.md`
- `06-2-data-and-feature-pipelines/theory/06-2-data-and-feature-pipelines.md`
- `06-3-model-deployment-and-serving/theory/06-3-model-deployment-and-serving.md`
- `06-4-monitoring-drift-and-governance/theory/06-4-monitoring-drift-and-governance.md`
- `06-5-llmops-operationalizing-llms-rag-and-agents/theory/06-5-llmops-operationalizing-llms-rag-and-agents.md`
- Run the matching notebook in each sub-folder `notebooks/`.

## Prerequisites
- Lessons 1-5 (programming, ML foundations, deep learning, and GenAI basics).
- Python environment with common ML libraries and Jupyter.

## Lesson Boundary
This lesson is the foundational operations layer: lifecycle setup, baseline pipelines, serving, and first-pass monitoring/governance.

Lesson 12 is intentionally separate and advanced: it assumes these basics and adds inference systems engineering, evaluation flywheels, distributed training strategy, privacy-preserving operations, and data-centric labeling loops for mature production environments.

## What's Next
Move to Lesson 7 to apply these ops fundamentals to agentic systems design and orchestration patterns.
