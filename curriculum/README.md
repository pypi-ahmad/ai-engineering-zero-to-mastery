# Curriculum (Beginner-First Learning Path)

This folder turns the repository into a **guided learning journey** for complete beginners.

If you are not sure where to start:
1. Start with [00-orientation](./00-orientation/README.md).
2. Follow the modules in order.

## What You Are Learning (In One Sentence)

AI engineering is building **reliable AI systems end-to-end**: data -> training -> evaluation -> serving -> monitoring -> safety -> iteration.

## How To Use This Curriculum

For each module:
1. Read the module page (what to do, why it matters, and what to skip).
2. Complete the linked lessons/sub-lessons.
3. Run at least one notebook from a clean kernel (restart -> run all).
4. Do the `exercises/` and compare with `solutions.md`.
5. Produce a small artifact (saved model/metrics, a tiny API, or a short write-up).

## The Path (Recommended Order)

1. Orientation and setup:
   - [00-orientation](./00-orientation/README.md)
2. Core foundations (Python + engineering habits):
   - [01-foundations](./01-foundations/README.md)
3. ML essentials (train/val/test, metrics, baselines):
   - [02-ml-basics](./02-ml-basics/README.md)
4. First shipped system (your first end-to-end loop):
   - [03-first-production-system](./03-first-production-system/README.md)
5. Deep learning fundamentals (enough to be dangerous):
   - [04-deep-learning](./04-deep-learning/README.md)
6. GenAI and LLM systems (prompting -> RAG -> eval):
   - [05-genai-and-llms](./05-genai-and-llms/README.md)
7. Agentic systems (tools, state, guardrails):
   - [06-agentic-systems](./06-agentic-systems/README.md)
8. Production ops (MLOps + LLMOps fundamentals):
   - [07-production-ops](./07-production-ops/README.md)
9. Safety + governance (ship responsibly):
   - [08-safety-and-governance](./08-safety-and-governance/README.md)
10. Specializations (pick based on interest):
   - [09-specializations](./09-specializations/README.md)
11. Capstone (portfolio-ready delivery):
   - [10-capstone](./10-capstone/README.md)

## Prerequisite Flow (What Depends On What)

- Lesson 1 is required for everything.
- Lesson 3 is the minimum baseline for “production thinking” (splits, metrics, baselines).
- Deep learning (Lesson 4) unlocks modern GenAI (Lesson 5).
- GenAI (Lesson 5) unlocks agentic design (Lesson 7) and LLMOps (Lesson 6.5).
- MLOps foundations (Lesson 6.1/6.2) should be learned early, even if you postpone serving.

## If You Want The “Shortest Path” (First Wins)

1. Lesson 1 -> Lesson 3
2. Run the capstone scaffold: `projects/capstone-template/`
3. Lesson 6.1 + 6.2 (run metadata + data pipeline discipline)
4. Lesson 5.3 + 5.4 (prompting + RAG basics)
