# Exercises: 6.5 LLMOps (LLMs, RAG & Agents in Production)

These are offline-first exercises focused on operational discipline for LLM systems:
prompts as artifacts, evaluation harnesses, cost/latency controls, and runtime guardrails.

## Exercise 1: Prompt as an Artifact (Version + Fingerprint)

Create a prompt template file (e.g., `prompts/answer_with_citations_v1.txt`) and write:
- a small loader that reads the prompt from disk,
- a function that computes a stable fingerprint (SHA-256) of the prompt text.

Expected outcome:
- you can refer to a prompt by both `version` and `fingerprint` in logs.

## Exercise 2: Mini Evaluation Harness (Regression Check)

Create a tiny eval set of 10 cases for your LLM app behavior. Each case should include:
- `input`,
- `expected` (can be a label, keywords, or a structured JSON shape),
- `risk_level` (low/medium/high).

Write an evaluator that:
- runs your system function (use a deterministic stub if you don't have an API call),
- scores each case,
- fails the run if any `high` risk case regresses.

Expected outcome:
- prompt/index/tool changes can be tested before rollout.

## Exercise 3: Token/Cost Budget Gate (Offline Estimation)

Implement a token estimator (offline approximation is fine) and compute:
- estimated input tokens,
- estimated output tokens,
- estimated cost given a configurable price per 1K tokens.

Add a gate:
- reject or truncate requests when estimated total tokens exceed a budget.

Expected outcome:
- runaway context growth is prevented with an explicit policy.

## Exercise 4: Retrieval Circuit Breaker (RAG Health Check)

Given retrieval results (doc ids + scores), implement a circuit breaker:
- if `top_k == 0`, or
- if `max_score < threshold`, or
- if average score is too low,

then return an abstention response (or a fallback path) instead of generating confidently.

Expected outcome:
- silent index failures do not silently degrade answer quality.

## Exercise 5: Tool Policy (Allowlist + Risk Routing)

Implement a policy function for tool calls that:
- allowlists tool names,
- blocks "high risk" tools unless an explicit `approved=True` flag is present,
- logs every decision (allow/block) with a reason.

Expected outcome:
- agents cannot freely call sensitive tools without an explicit gate.

