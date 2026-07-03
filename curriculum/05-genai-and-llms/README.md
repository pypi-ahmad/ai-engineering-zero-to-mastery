# 05: GenAI and LLM Systems (Prompting -> RAG -> Evaluation)

Goal: build grounded LLM applications and learn how to evaluate them so you can improve quality safely.

## Prerequisites

- [04-deep-learning](../04-deep-learning/README.md) (recommended)
- [02-ml-basics](../02-ml-basics/README.md) (required baseline evaluation discipline)

## Do These Lessons

- Lesson 5:
  - [`05-generative-models-and-llms/README.md`](../../05-generative-models-and-llms/README.md)

Suggested beginner order inside Lesson 5:
1. 5.3 LLM foundations and prompt engineering
2. 5.4 RAG, tools, and AI agents (foundation, not “agent hype”)
3. 5.5 Fine-tuning (optional until you have a real dataset + eval loop)

## When To Install Extras

GenAI extra:

```bash
uv sync --frozen --extra genai
```

## What To Build (Mini-Deliverable)

Build a tiny offline RAG demo (TF-IDF is fine) plus an eval script:
- recall@k for retrieval
- a small regression test set for generation behavior

You can use the `exercises/` in 5.4 and 6.5 as the scaffold.

## Next

Continue to [06-agentic-systems](../06-agentic-systems/README.md).
