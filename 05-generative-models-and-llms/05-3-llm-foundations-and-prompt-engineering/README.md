# 5.3 LLM Foundations & Prompt Engineering

This chapter covers the practical foundations for building with LLMs:

- LLM architecture and training lifecycle (pre-training to adaptation)
- Prompt design patterns for reliability and control
- Fine-tuning and PEFT overview (including LoRA)
- Evaluation beyond single offline metrics

## Why This Matters

LLMs are powerful but not reliable by default. Prompting is a form of programming: if you don’t control inputs/outputs, you’ll ship brittle behavior that fails silently.

## Key Terms (Plain English)

- **Prompt**: instructions + context you send to a model.
- **System vs user prompt**: higher-priority policy vs user request (conceptually).
- **Hallucination**: confident output not supported by evidence.
- **Few-shot**: include examples in the prompt to shape behavior.

## Start Here

1. Theory: `theory/05-3-llm-foundations-and-prompt-engineering.md`
2. Notebook: `notebooks/05-3-llm-foundations-and-prompt-engineering-demo.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## What You Will Learn

- How prompt structure affects model behavior.
- When prompting is enough vs when fine-tuning is justified.
- Common LLM failure modes and mitigation patterns.
- Interview-ready distinctions across prompting, fine-tuning, and evaluation.

## Expected Outcomes

- You can write a prompt that produces structured output reliably (JSON schema or bullet format).
- You can identify common failure modes (prompt injection, ambiguity, missing constraints).
- You can define a tiny evaluation set to prevent regressions.

## Verify Your Work

- Run the notebook from a clean kernel.
- Complete the exercises and produce:
  - a prompt template file,
  - a small eval set (5–10 cases),
  - one regression check that fails when you intentionally break the prompt.

## Common Mistakes

- “Prompt until it looks good once” without an eval set.
- Overstuffing context (cost/latency grows, quality can drop).
- Not specifying output format, then struggling to parse results.
