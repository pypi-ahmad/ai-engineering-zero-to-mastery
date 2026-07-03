# Learning Tracks

This repo supports multiple ways to learn. If you are a complete beginner, do not optimize for “coverage”. Optimize for **consistent execution** and **small shipped artifacts**.

If you want one clear path without thinking, follow: [`curriculum/README.md`](../curriculum/README.md).

## Track 1: Absolute Beginner Track (First Wins)

Goal: get hands-on, end-to-end experience quickly without skipping fundamentals.

1. Lesson 1: foundations (Python + engineering habits)
2. Lesson 3: classical ML + evaluation basics
3. (Optional support) Lesson 2: math intuition (enough to reason about models)
4. Run the capstone scaffold: `projects/capstone-template/`
5. Lesson 6.1 + 6.2: MLOps fundamentals (run metadata + data pipeline discipline)

Tip: for Lessons 1–3, do the `exercises/` after running each notebook once.

Expected outcome:
- you can train, evaluate, and serve a baseline model with saved artifacts and a basic API contract.

## Track 2: GenAI Builder Track (RAG + Evaluation + Guardrails)

Goal: build grounded LLM systems with an evaluation loop and safe tool use.

Recommended prerequisites:
- Lesson 1 (especially 1.3)
- Lesson 3.3 (evaluation discipline)

Sequence:
1. Lesson 5.3: LLM foundations and prompt engineering
2. Lesson 5.4: RAG/tools foundations (offline TF-IDF is fine)
3. Lesson 6.5: LLMOps practice (prompt versioning, eval harnesses, cost/latency gates)
4. Lesson 13.4: practical guardrails and safe agent design

Expected outcome:
- you can build a small RAG app that is measurable (eval set + regression checks) and safer (tool allowlist + circuit breakers).

## Track 3: Practitioner Track (Systems Focus)

Goal: learn the production layer for AI systems (deployment, monitoring, evaluation loops).

Recommended prerequisites:
- basic Python + basic ML familiarity

Sequence:
1. Lesson 6: production AI systems (foundations)
2. Lesson 12: production hardening + ops depth
3. Lesson 13: safety, security, and trustworthy AI controls
4. Lesson 15: capstone professional practice

Expected outcome:
- you can design a production deployment path and an evaluation/monitoring plan, and you can explain tradeoffs.

## Track 4: Full Track (Zero to Mastery)

Goal: go from fundamentals to advanced applied topics and capstone practice.

Sequence:
- Lessons 1 → 15 in order.

Expected outcome:
- you can build and reason about ML/DL/GenAI systems end-to-end, including ops, safety, and specialization directions.

## When To Install Extras

- Deep learning: `uv sync --extra dl`
- GenAI lessons: `uv sync --extra genai`
- RL demos: `uv sync --extra rl`
- Serving demos: `uv sync --extra serving`
- Ops tooling: `uv sync --extra ops`
