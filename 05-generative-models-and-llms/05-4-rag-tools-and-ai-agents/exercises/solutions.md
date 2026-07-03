# Solutions: 5.4 RAG, Tools, and AI Agents

## Exercise 1: Chunking Function

```python
from __future__ import annotations


def chunk_text(text: str, chunk_size: int, overlap: int) -> list[str]:
    if chunk_size < 1:
        raise ValueError("chunk_size must be >= 1")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be in [0, chunk_size)")

    chunks: list[str] = []
    i = 0
    n = len(text)
    step = chunk_size - overlap
    while i < n:
        chunk = text[i : i + chunk_size]
        if chunk:
            chunks.append(chunk)
        i += step
    return chunks
```

## Exercise 2: TF-IDF Retrieval

```python
from __future__ import annotations

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def retrieve_topk(docs: list[str], query: str, k: int = 3) -> list[int]:
    vec = TfidfVectorizer(ngram_range=(1, 2))
    X = vec.fit_transform(docs)
    q = vec.transform([query])
    scores = (X @ q.T).toarray().ravel()
    order = np.argsort(scores)[::-1]
    return [int(i) for i in order[:k]]


docs = [
    "cat sat on the mat",
    "dogs are great pets",
    "transformers use attention",
    "rag retrieves documents",
]
print(retrieve_topk(docs, "attention in transformers", k=2))
```

## Exercise 3: Recall@K Evaluation (Toy QA)

```python
from __future__ import annotations


def recall_at_k(pred_ids: list[int], gold_id: int, k: int) -> float:
    return 1.0 if gold_id in pred_ids[:k] else 0.0


qa = [
    ("attention", 2),
    ("retrieval augmented generation", 3),
]

docs = [
    "cats and mats",
    "dogs and parks",
    "transformers use attention and multi-head attention",
    "rag retrieves documents and grounds responses",
]

r1 = 0.0
r3 = 0.0
for q, gold in qa:
    pred = retrieve_topk(docs, q, k=3)
    r1 += recall_at_k(pred, gold, k=1)
    r3 += recall_at_k(pred, gold, k=3)

print("recall@1", r1 / len(qa), "recall@3", r3 / len(qa))
```

## Exercise 4: Tool Dispatcher (Allowlist + Safe Failures)

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True)
class ToolResult:
    ok: bool
    data: dict[str, Any] | None = None
    error: str | None = None


def tool_add(a: float, b: float) -> ToolResult:
    return ToolResult(ok=True, data={"sum": float(a + b)})


TOOLS: dict[str, Callable[..., ToolResult]] = {"add": tool_add}


def dispatch(tool_name: str, args: dict[str, Any]) -> ToolResult:
    if tool_name not in TOOLS:
        return ToolResult(ok=False, error="unknown_tool")
    try:
        return TOOLS[tool_name](**args)
    except TypeError:
        return ToolResult(ok=False, error="invalid_args")


print(dispatch("add", {"a": 1, "b": 2}))
print(dispatch("rm", {"path": "/"}))
```

## Exercise 5: Minimal Trace Log (JSONL)

```python
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any


def log_jsonl(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")


log_path = Path("artifacts/rag_trace.jsonl")
start = time.perf_counter()
retrieved = [2, 3, 1]
answer = "RAG retrieves documents to ground answers."
lat_ms = int((time.perf_counter() - start) * 1000)
log_jsonl(log_path, {"query": "what is rag", "retrieved_ids": retrieved, "answer": answer, "latency_ms": lat_ms, "error": None})
```

