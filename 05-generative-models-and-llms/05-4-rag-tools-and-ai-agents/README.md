# 5.4 RAG, Tools, and AI Agents

This chapter explains how to move from standalone LLM prompts to grounded, tool-augmented systems:

- RAG components and pipeline design
- Tool/function-calling patterns
- Agentic loops (planning, execution, state)
- Observability and failure analysis for production AI systems

## Why This Matters

Most real LLM products need grounding (RAG) and actions (tools). This is where “cool demos” become systems you can measure, debug, and make safer.

## Key Terms (Plain English)

- **RAG**: retrieve relevant documents and include them as context for generation.
- **Tool/function calling**: the model requests a controlled function to run (search, DB query).
- **Agent loop**: multi-step reasoning + tool use with state.
- **Groundedness**: answer is supported by retrieved evidence.

## Start Here

1. Theory: `theory/05-4-rag-tools-and-ai-agents.md`
2. Notebook: `notebooks/05-4-rag-tools-and-ai-agents-demo.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## What You Will Learn

- RAG architecture and where quality bottlenecks occur.
- How tools extend LLM capabilities with deterministic actions.
- Typical agent failure modes and guardrails.
- Business-aligned evaluation metrics for retrieval and grounded generation.

## Expected Outcomes

- You can implement a basic retriever and measure recall@k.
- You can design a tool allowlist that prevents arbitrary code execution.
- You can add trace logs so failures are debuggable.

## Verify Your Work

- Run the notebook from a clean kernel.
- Complete the exercises and ensure you can answer:
  - What happens when retrieval returns zero docs?
  - How do you stop unsafe tool calls?

## Common Mistakes

- Evaluating only the final answer and ignoring retrieval quality.
- Allowing unrestricted tools (security risk).
- Logging nothing, then debugging by guessing.
