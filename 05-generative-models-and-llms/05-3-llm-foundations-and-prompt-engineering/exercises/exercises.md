# Exercises: 5.3 LLM Foundations & Prompt Engineering

These exercises are **offline-first**: they focus on reliability patterns around prompts, schemas, and evaluation harnesses (not on calling a hosted model).

Optional prereq (only if you want to run Transformers locally and you have network/model access):

```bash
uv sync --frozen --extra genai
```

## Exercise 1: JSON Output Contract (Pydantic)

Define a Pydantic model for a structured LLM response, for example:
- `answer: str`
- `citations: list[str]`
- `confidence: float` in `[0,1]`

Write a validator function that:
- extracts JSON from a raw text blob,
- validates against the schema,
- returns a helpful error on failure.

Expected outcome:
- bad outputs fail fast with clear messages.

## Exercise 2: Prompt Template (Constraints First)

Write a prompt template that forces:
- role and goal,
- output format (JSON),
- refusal policy (what to do if missing info),
- “do not hallucinate sources” rule.

Expected outcome:
- template is reusable across tasks and has minimal ambiguity.

## Exercise 3: Injection Heuristic Filter

Implement a lightweight heuristic detector that flags user messages containing common injection patterns (e.g., “ignore previous”, “system prompt”, “reveal secrets”).

Expected outcome:
- you can explain false positives/negatives and why this is only a weak layer.

## Exercise 4: Mini Eval Harness (Exact + Partial)

Create a small evaluation set of 10 items:
- each item has `input`, `expected_answer`, and optional `expected_fields`.

Write a scorer that computes:
- exact match rate,
- “contains expected keywords” rate.

Expected outcome:
- you can compare two prompt variants objectively using the same rubric.

## Exercise 5: Cost Estimator

Given:
- prompt tokens,
- completion tokens,
- $/1K tokens for input/output,

Compute per-request cost and total cost for `N` requests.

Expected outcome:
- you can budget experiments and production usage.

