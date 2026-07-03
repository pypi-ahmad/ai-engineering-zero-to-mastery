# Learning Tracks

This repo supports multiple ways to learn. If you are a complete beginner, do not optimize for “coverage”. Optimize for **consistent execution** and **small shipped artifacts**.

## Track 1: Beginner Track (First Wins)

Goal: get hands-on, end-to-end experience quickly without skipping fundamentals.

1. Lesson 1: foundations (Python + engineering habits)
2. Lesson 2: math intuition (enough to reason about models)
3. Lesson 3: classical ML + evaluation basics
4. Run the capstone scaffold: `projects/capstone-template/`
5. Lesson 6: MLOps/LLMOps fundamentals

Expected outcome:
- you can train, evaluate, and serve a baseline model with saved artifacts and a basic API contract.

## Track 2: Practitioner Track (Systems Focus)

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

## Track 3: Full Track (Zero to Mastery)

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

