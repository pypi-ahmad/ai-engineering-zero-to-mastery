# Solutions: 6.5 LLMOps (LLMs, RAG & Agents in Production)

These solutions are intentionally minimal and offline-friendly. Replace stubs with
real model/RAG/tool integrations as you progress.

## Exercise 1: Prompt as an Artifact (Version + Fingerprint)

```python
from __future__ import annotations

import hashlib
from pathlib import Path


def load_prompt(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def prompt_fingerprint(prompt: str) -> str:
    return hashlib.sha256(prompt.encode("utf-8")).hexdigest()


prompt_path = Path("prompts/answer_with_citations_v1.txt")
prompt = load_prompt(prompt_path)
print("prompt_version", "v1")
print("prompt_sha256", prompt_fingerprint(prompt))
```

## Exercise 2: Mini Evaluation Harness (Regression Check)

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Case:
    input: str
    expected: dict[str, Any]
    risk_level: str  # "low" | "medium" | "high"


def system_stub(user_input: str) -> dict[str, Any]:
    # Deterministic placeholder for "the system under test".
    # Swap with your real chain (RAG -> generate -> postprocess).
    if "refund" in user_input.lower():
        return {"intent": "refund", "needs_escalation": True}
    return {"intent": "general", "needs_escalation": False}


def score(output: dict[str, Any], expected: dict[str, Any]) -> bool:
    # Minimal exact-match on selected keys; make this stricter over time.
    for k, v in expected.items():
        if output.get(k) != v:
            return False
    return True


def run_eval(cases: list[Case]) -> None:
    failures: list[str] = []
    for i, c in enumerate(cases):
        out = system_stub(c.input)
        ok = score(out, c.expected)
        if not ok:
            failures.append(f"case={i} risk={c.risk_level} out={out} expected={c.expected}")
    high_failures = [f for f in failures if "risk=high" in f]
    if high_failures:
        raise AssertionError("High-risk regression(s):\n" + "\n".join(high_failures))


cases = [
    Case(
        input="I want a refund for my last order",
        expected={"intent": "refund", "needs_escalation": True},
        risk_level="high",
    ),
    Case(
        input="What are your business hours?",
        expected={"intent": "general"},
        risk_level="low",
    ),
]
run_eval(cases)
print("eval passed")
```

## Exercise 3: Token/Cost Budget Gate (Offline Estimation)

```python
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Budget:
    max_total_tokens: int
    price_per_1k_tokens_usd: float


def estimate_tokens(text: str) -> int:
    # Offline approximation: replace with provider tokenizer when available.
    # This is good enough to prevent obvious runaway prompts.
    return max(1, len(text.split()))


def estimate_cost_usd(total_tokens: int, price_per_1k_tokens_usd: float) -> float:
    return (total_tokens / 1000.0) * price_per_1k_tokens_usd


def budget_gate(prompt: str, user_input: str, expected_output_tokens: int, budget: Budget) -> dict:
    t_in = estimate_tokens(prompt) + estimate_tokens(user_input)
    t_out = expected_output_tokens
    total = t_in + t_out
    if total > budget.max_total_tokens:
        return {
            "ok": False,
            "reason": "token_budget_exceeded",
            "estimated_tokens": total,
            "estimated_cost_usd": estimate_cost_usd(total, budget.price_per_1k_tokens_usd),
        }
    return {
        "ok": True,
        "estimated_tokens": total,
        "estimated_cost_usd": estimate_cost_usd(total, budget.price_per_1k_tokens_usd),
    }


res = budget_gate(
    prompt="You are a helpful assistant.",
    user_input="Summarize the quarterly report and list key risks.",
    expected_output_tokens=300,
    budget=Budget(max_total_tokens=800, price_per_1k_tokens_usd=0.50),
)
print(res)
```

## Exercise 4: Retrieval Circuit Breaker (RAG Health Check)

```python
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RetrievalResult:
    doc_id: str
    score: float


def rag_circuit_breaker(results: list[RetrievalResult], *, min_max_score: float, min_avg_score: float) -> dict:
    if not results:
        return {"ok": False, "reason": "no_retrieval_results"}
    max_score = max(r.score for r in results)
    avg_score = sum(r.score for r in results) / len(results)
    if max_score < min_max_score:
        return {"ok": False, "reason": "low_confidence_max_score", "max_score": max_score, "avg_score": avg_score}
    if avg_score < min_avg_score:
        return {"ok": False, "reason": "low_confidence_avg_score", "max_score": max_score, "avg_score": avg_score}
    return {"ok": True, "max_score": max_score, "avg_score": avg_score}


ok = [RetrievalResult("doc1", 0.72), RetrievalResult("doc2", 0.55)]
bad = [RetrievalResult("doc1", 0.08), RetrievalResult("doc2", 0.05)]

print(rag_circuit_breaker(ok, min_max_score=0.3, min_avg_score=0.2))
print(rag_circuit_breaker(bad, min_max_score=0.3, min_avg_score=0.2))
```

## Exercise 5: Tool Policy (Allowlist + Risk Routing)

```python
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ToolDecision:
    allow: bool
    reason: str


TOOL_RISK = {
    "search_docs": "low",
    "summarize": "low",
    "send_email": "high",
    "create_ticket": "medium",
}


def tool_policy(tool_name: str, *, approved: bool) -> ToolDecision:
    if tool_name not in TOOL_RISK:
        return ToolDecision(False, "tool_not_allowlisted")
    risk = TOOL_RISK[tool_name]
    if risk == "high" and not approved:
        return ToolDecision(False, "high_risk_requires_approval")
    return ToolDecision(True, "ok")


for tool in ["search_docs", "send_email", "rm_rf"]:
    for approved in [False, True]:
        d = tool_policy(tool, approved=approved)
        print(tool, "approved", approved, "=>", d)
```

