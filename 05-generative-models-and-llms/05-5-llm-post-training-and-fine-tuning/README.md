# 5.5 LLM Post-Training & Fine-Tuning

This sub-lesson is the practical bridge from prompting to model adaptation. It covers supervised fine-tuning (SFT), PEFT, LoRA, QLoRA, and the transition to preference optimization methods such as DPO/RLHF.

## What You Will Learn
- How to decide between prompting, RAG, and fine-tuning.
- How PEFT/LoRA/QLoRA reduce adaptation cost.
- How to design eval-first post-training workflows.
- How to package and operationalize tuned artifacts safely.

## Start Here
- Theory: `theory/05-5-llm-post-training-and-fine-tuning.md`
- Notebook: `notebooks/05-5-llm-post-training-and-fine-tuning-peft-lora-qlora.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## Prerequisites
- Lesson 5.3 (LLM foundations and prompt engineering)
- Lesson 5.4 (RAG/tool patterns)
- Basic familiarity with Python and transformers workflows

## Why This Matters
Modern LLM systems often fail due to behavior inconsistency rather than missing model capacity. This module shows how to tune behavior rigorously while keeping cost and operations manageable.
