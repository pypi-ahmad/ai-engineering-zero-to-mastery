# 07: Production Ops (MLOps + LLMOps Fundamentals)

Goal: learn the operational discipline required to keep AI systems reliable: versioning, deployment patterns, monitoring, and incident readiness.

## Prerequisites

- Minimum: [02-ml-basics](../02-ml-basics/README.md)
- Recommended: [05-genai-and-llms](../05-genai-and-llms/README.md)

## Do These Lessons

Start with Lesson 6 (fundamentals):
- [`06-mlops-and-llmops-production-ai-systems/README.md`](../../06-mlops-and-llmops-production-ai-systems/README.md)

Suggested ordering inside Lesson 6:
1. 6.1 Lifecycle + run metadata
2. 6.2 Data and feature pipelines (lineage, fingerprinting, point-in-time joins)
3. 6.3 Serving + API contracts (when you are ready to deploy)
4. 6.4 Monitoring/drift/governance (alerts, thresholds, retraining triggers)
5. 6.5 LLMOps (prompt versioning, eval harnesses, cost/latency gates, tool policy)

Then (optional, advanced): Lesson 12 (operations depth and scaling)
- [`12-mlops-and-llmops-production-ai-and-operations/README.md`](../../12-mlops-and-llmops-production-ai-and-operations/README.md)

## Why This Module Is Here (And Why It’s Split)

- Lesson 6 is the “baseline ops layer” you need early.
- Lesson 12 is intentionally deeper and broader. Do it after you have shipped something and have real constraints (latency, cost, reliability).

## Completion Criteria (Self-Check)

- You can define a regression gate that blocks a release.
- You can design an alerting policy that avoids “alert fatigue”.
- You can explain what you would do during an incident (rollback, circuit breaker, escalation).

## Next

Continue to [08-safety-and-governance](../08-safety-and-governance/README.md).
