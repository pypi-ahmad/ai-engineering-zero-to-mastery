# Overview

LLMOps is the operational discipline for large language model systems in production. It builds on MLOps principles but introduces new constraints:

- prompt and context are first-class artifacts,
- inference cost is token-driven,
- non-determinism is common,
- retrieval/tool chains can fail independently from the base model,
- safety and policy controls must be enforced at runtime.

In short:

- **MLOps** optimizes model lifecycle for predictive systems.
- **LLMOps** extends this to prompt orchestration, RAG indices, tool execution, and response quality governance.

LLMOps curricula (e.g., Duke/Coursera specialization) reflect this shift by covering cloud/local deployments, prompt patterns, RAG, and lifecycle controls as mandatory production skills.

# LLM-Specific Concerns

## Context management and token limits

LLM quality depends on context quality, not only model weights. Operational risks include:

- context truncation removing key evidence,
- prompt bloat increasing cost and latency,
- irrelevant retrieval degrading groundedness.

Token budget framing:

$$
C_{query} \approx (t_{in} + t_{out}) \times c_{token}
$$

where $t_{in}$ and $t_{out}$ are input/output tokens and $c_{token}$ is provider-specific unit cost.

## Cost, latency, and throughput

Core LLMOps trade-offs:

- larger models improve quality but increase latency/cost,
- more retrieved context may improve accuracy but hurt speed,
- agent loops improve task completion but risk unbounded runtime.

## Safety and policy controls

Production LLM stacks need:

- prompt/response filters,
- PII redaction,
- abuse prevention and rate limiting,
- restricted tool permissions,
- human escalation for high-risk actions.

# Operational Patterns for LLM Apps

## API-based vs local/self-hosted models

### API-based models

Pros:

- fastest path to production,
- managed scaling,
- rapid model upgrades.

Cons:

- vendor dependency,
- egress/privacy concerns,
- cost volatility.

### Local/self-hosted models

Pros:

- stronger data control,
- custom optimization possibilities,
- predictable infrastructure ownership.

Cons:

- higher ops burden (inference serving, scaling, patching).

## Orchestration patterns

- **Simple chain**: prompt -> model -> post-processing.
- **RAG chain**: retrieve -> augment -> generate.
- **Tool-augmented chain**: model invokes APIs/functions.
- **Agentic loop**: planner/executor/reviewer over multiple steps.

Use the simplest pattern that meets quality targets; complexity multiplies failure modes.

# RAG in Production

RAG remains a dominant enterprise pattern for factual grounding and fresh knowledge injection.

## RAG architecture recap

Core components:

1. corpus ingestion and chunking,
2. embedding and indexing,
3. retrieval and reranking,
4. prompt augmentation,
5. response generation.

Google, Microsoft, IBM, and NVIDIA references all converge on this core pattern with different platform tooling.

## Indexing pipelines and refresh strategy

RAG reliability depends on index freshness and quality:

- schedule incremental ingestion,
- detect ingestion failures,
- version index snapshots,
- keep rollback-able prior index.

If retriever index breaks, answer quality can degrade silently while model health dashboards look normal.

## RAG evaluation in production

Track both retrieval and generation quality:

- context recall/precision,
- groundedness/faithfulness,
- citation correctness,
- response usefulness,
- latency and cost per answer.

NVIDIA and RAG evaluation ecosystems commonly emphasize groundedness and retrieval metrics together; evaluating only final answer quality masks retrieval defects.

# Observability for LLM Systems

Observability must include model and orchestration layers.

## What to log

- prompt template version,
- retrieved passages and scores,
- tool calls (arguments, outputs, errors),
- model ID/configuration,
- token counts, latency, and cost,
- user feedback and correction outcomes.

## Tracing

Use request-level traces across stages:

$$
T_{total} = T_{retrieve} + T_{rerank} + T_{generate} + T_{tools}
$$

This decomposition reveals bottlenecks and failure hotspots.

## Evaluation harnesses

Maintain a replayable evaluation set with:

- representative tasks,
- high-risk failure cases,
- regression checks on prompt/index/model changes.

# Common Pitfalls

1. **Unbounded prompt growth**
   - Costs rise and useful signal dilutes.
2. **Retriever/index silent failures**
   - LLM still responds confidently using poor context.
3. **No prompt/version control**
   - Quality changes cannot be attributed.
4. **Tool over-permissioning**
   - Agents can call sensitive systems without adequate checks.
5. **Ignoring fallback behavior**
   - Systems fail hard instead of abstaining or escalating.

# Business Case Studies & Exceptions

## Case Study 1: Enterprise document assistant

Scenario:

- Global enterprise deploys internal policy assistant over large document corpus.

Production pattern:

- RAG with periodic indexing jobs,
- citation-required prompt templates,
- confidence-aware abstention,
- human escalation for policy-critical answers.

Observed gains:

- lower support load,
- faster employee response cycles.

Critical risk:

- stale or partial index causes confident but outdated answers.

## Case Study 2: Outage from upstream index failure

Scenario:

- Indexing pipeline failed after schema change; retriever returned near-empty context.

Symptom:

- Model still generated fluent responses, but factual error rate spiked.

Mitigations:

1. Retrieval health checks (min retrieved docs, score thresholds).
2. Circuit breaker: if retrieval confidence low, abstain.
3. Independent alert channel for indexing jobs.
4. Rollback to previous index snapshot.

## Exceptions and trade-offs

- Fine-tuning is not a substitute for frequently changing knowledge. RAG plus strong retrieval ops is often better for freshness.
- For ultra-sensitive domains, a narrow deterministic workflow with constrained generation may outperform a general agentic stack.

# Interview Questions & Answers

1. **Q: What is LLMOps?**
   **A:** The practice of building, deploying, monitoring, and governing LLM applications in production, including prompts, retrieval, tools, and agent behavior.

2. **Q: How is LLMOps different from MLOps?**
   **A:** LLMOps adds prompt/context management, token economics, RAG/tool orchestration, and runtime safety controls.

3. **Explain RAG vs fine-tuning in production.**  
   RAG injects external knowledge at inference for freshness; fine-tuning adapts model behavior/skills and is slower to update for factual changes.

4. **Q: What are core RAG components?**
   **A:** Ingestion/chunking, embeddings/index, retrieval/reranking, prompt augmentation, generation.

5. **Q: How do you monitor an LLM application?**
   **A:** Track groundedness, retrieval quality, latency, token cost, tool-call errors, and user feedback outcomes.

6. **Q: What causes cost explosions in LLM systems?**
   **A:** Prompt bloat, unnecessary long outputs, repeated retries, and uncontrolled agent loops.

7. **Q: What is groundedness?**
   **A:** Degree to which response claims are supported by retrieved evidence/context.

8. **Q: Why is retrieval observability critical?**
   **A:** Poor retrieval silently degrades answer quality even if model service appears healthy.

9. **Q: How do you control agent risk?**
   **A:** Tool schemas, permission boundaries, approval checkpoints, and action audit logs.

10. **Q: When should a system abstain?**
   **A:** When retrieval confidence is low, evidence conflicts, or policy constraints are unmet.

11. **Q: What should be versioned in LLMOps?**
   **A:** Prompt templates, model IDs, retrieval settings, index versions, tool interfaces, and evaluation datasets.

12. **Q: What is a good LLMOps promotion workflow?**
   **A:** Offline eval -> shadow/limited rollout -> monitor quality/cost/safety -> staged promotion.

13. **Q: How do you reduce latency in RAG systems?**
   **A:** Optimize retrieval pipeline, cache frequent queries, cap context size, and tune model size/decoding.

14. **Q: What metrics are specific to tool-using agents?**
   **A:** tool success rate, invalid call rate, retry count, step depth, and task completion fidelity.

15. **Q: How do you debug a sudden quality drop?**
   **A:** Trace request path across prompt changes, retriever behavior, index freshness, and model version changes.

16. **Q: Can a high-quality base model compensate for weak retrieval?**
   **A:** Only partially; in factual tasks weak retrieval typically dominates failure patterns.

17. **Q: What is the highest-risk anti-pattern in LLMOps?**
   **A:** Shipping an agent with broad tool access and no policy enforcement or observability.
# Further Reading & Sources

- Duke/Coursera LLMOps specialization: https://www.coursera.org/specializations/large-language-model-operations
- Duke LLMOps curriculum repository: https://github.com/alfredodeza/llmops-duke-aipi
- Google Cloud RAG reference architectures: https://docs.cloud.google.com/architecture/rag-reference-architectures
- Google RAG infrastructure architecture: https://docs.cloud.google.com/architecture/rag-capable-gen-ai-app-using-vertex-ai
- Google RAG overview: https://cloud.google.com/use-cases/retrieval-augmented-generation
- Microsoft RAG overview: https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview
- IBM RAG overview: https://www.ibm.com/think/topics/retrieval-augmented-generation
- NVIDIA RAG evaluation docs: https://docs.nvidia.com/rag/latest/evaluate.html
- NVIDIA RAG metrics: https://docs.nvidia.com/nemo-platform/documentation/evaluate-models/metrics/rag-metrics
- Azure MLOps/GenAIOps perspective: https://learn.microsoft.com/en-us/azure/well-architected/ai/mlops-genaiops

## Bridge to Next Lesson

- **What you now know:** You can operationalize ML and LLM applications with lifecycle thinking, pipelines, deployment controls, and observability basics.
- **Why the next lesson follows:** The next lesson follows because once systems are operable, the key challenge becomes architecting agentic workflows and multi-step AI product behavior.
- **What you'll build next:** You will build agentic AI designs with orchestration patterns, context engineering, memory/planning, and end-to-end agent system blueprints.

