# Exercises: 5.4 RAG, Tools, and AI Agents

These exercises are runnable offline using TF-IDF retrieval and toy tool dispatch patterns.

## Exercise 1: Chunking Function

Implement `chunk_text(text: str, chunk_size: int, overlap: int) -> list[str]`.

Rules:
- `overlap < chunk_size`,
- preserve order,
- no empty chunks.

Expected outcome:
- you can print chunk boundaries and verify overlap works.

## Exercise 2: TF-IDF Retrieval

Given a list of documents and a query:
- build TF-IDF vectors,
- retrieve top-k documents by cosine similarity.

Expected outcome:
- relevant docs are returned for simple queries.

## Exercise 3: Recall@K Evaluation (Toy QA)

Create a toy dataset of 10 queries with “gold doc id”.

Compute recall@1 and recall@3 for your retriever.

Expected outcome:
- you can compare retrieval quality before/after changing chunk size or vectorizer settings.

## Exercise 4: Tool Dispatcher (Allowlist + Safe Failures)

Implement a tool dispatcher:
- allowlist tool names,
- validate tool args,
- return structured errors (not exceptions) for unknown tools.

Expected outcome:
- it is safe to expose this dispatcher to an LLM without arbitrary code execution.

## Exercise 5: Minimal Trace Log (JSONL)

Write a JSONL logger for a RAG run with fields:
- `query`, `retrieved_ids`, `answer`, `latency_ms`, `error` (nullable).

Expected outcome:
- logs are machine-readable and easy to grep.

