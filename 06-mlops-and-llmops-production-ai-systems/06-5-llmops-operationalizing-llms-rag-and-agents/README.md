# 6.5 LLMOps: Operationalizing LLMs, RAG & Agents

This sub-lesson covers operational excellence for LLM applications, RAG systems, and tool-using agents.

## Why This Matters

LLM systems fail in production in predictable ways: prompt drift, retrieval outages, unsafe tool use, runaway cost/latency, and silent quality regressions. LLMOps is the discipline for preventing and responding to these failures.

## Key Terms (Plain English)

- **Prompt artifact**: a versioned prompt template you can fingerprint and rollback.
- **Eval harness**: a repeatable test set + scoring that catches regressions.
- **Budget gate**: token/cost/latency limits enforced by policy.
- **Circuit breaker**: stop/abstain when retrieval confidence is low.

## Start Here

1. `theory/06-5-llmops-operationalizing-llms-rag-and-agents.md`
2. `notebooks/06-5-llmops-operationalizing-llms-rag-and-agents-demo.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## Coverage

- LLM-specific reliability, latency, and cost controls
- RAG indexing and retrieval operations
- Agent/tool orchestration guardrails
- LLM observability, evaluation, and incident response

## Verify Your Work

- Run the notebook from a clean kernel.
- Complete the exercises and ensure you can explain each operational gate:
  - prompt versioning,
  - eval regression checks,
  - token/cost budget policy,
  - retrieval circuit breaker,
  - tool allowlist/risk routing.

## Common Mistakes

- Treating prompt edits as “harmless” without regression tests.
- Logging only final answers and missing retrieval/tool traces.
