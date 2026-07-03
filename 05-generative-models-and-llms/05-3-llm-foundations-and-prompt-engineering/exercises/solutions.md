# Solutions: 5.3 LLM Foundations & Prompt Engineering

## Exercise 1: JSON Output Contract (Pydantic)

```python
from __future__ import annotations

import json
import re
from typing import Any

from pydantic import BaseModel, Field, ValidationError


class LLMAnswer(BaseModel):
    answer: str = Field(min_length=1)
    citations: list[str] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0)


_JSON_RE = re.compile(r"\\{.*\\}", re.DOTALL)


def extract_json(text: str) -> dict[str, Any]:
    m = _JSON_RE.search(text)
    if not m:
        raise ValueError("no JSON object found in text")
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON: {exc}") from exc


def parse_llm_answer(text: str) -> LLMAnswer:
    data = extract_json(text)
    try:
        return LLMAnswer.model_validate(data)
    except ValidationError as exc:
        raise ValueError(f"schema validation failed: {exc}") from exc
```

## Exercise 2: Prompt Template (Constraints First)

Example (adapt per task):

```text
You are a helpful assistant.
Goal: Answer the user question using only information you are confident about.

Output format: JSON only, matching this schema:
{ "answer": string, "citations": string[], "confidence": number 0..1 }

Rules:
- If key information is missing, say what is missing in `answer` and set confidence <= 0.4.
- Do not invent citations. Use empty citations if none are available.
```

## Exercise 3: Injection Heuristic Filter

```python
from __future__ import annotations


def looks_like_injection(user_text: str) -> bool:
    t = user_text.lower()
    patterns = [
        "ignore previous",
        "system prompt",
        "developer message",
        "reveal secret",
        "bypass",
        "jailbreak",
        "do anything now",
    ]
    return any(p in t for p in patterns)
```

## Exercise 4: Mini Eval Harness (Exact + Partial)

```python
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    inp: str
    expected: str
    keywords: list[str]


def score(pred: str, item: Item) -> tuple[bool, bool]:
    exact = pred.strip() == item.expected.strip()
    partial = all(k.lower() in pred.lower() for k in item.keywords)
    return exact, partial


items = [
    Item("Q1", "A1", ["a1"]),
    Item("Q2", "A2", ["a2"]),
]
preds = ["A1", "A2 but extra"]

exact_hits = 0
partial_hits = 0
for p, it in zip(preds, items):
    ex, pa = score(p, it)
    exact_hits += int(ex)
    partial_hits += int(pa)

print("exact", exact_hits / len(items), "partial", partial_hits / len(items))
```

## Exercise 5: Cost Estimator

```python
from __future__ import annotations


def request_cost_usd(
    prompt_tokens: int,
    completion_tokens: int,
    input_per_1k: float,
    output_per_1k: float,
) -> float:
    return (prompt_tokens / 1000) * input_per_1k + (completion_tokens / 1000) * output_per_1k


def total_cost_usd(per_req: float, n: int) -> float:
    return per_req * n


per = request_cost_usd(prompt_tokens=900, completion_tokens=300, input_per_1k=0.005, output_per_1k=0.015)
print(per, total_cost_usd(per, 1000))
```

