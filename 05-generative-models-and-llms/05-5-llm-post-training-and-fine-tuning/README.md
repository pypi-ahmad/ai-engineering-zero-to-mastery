# 5.5 LLM Post-Training & Fine-Tuning

This sub-lesson is the practical bridge from prompting to model adaptation. It covers supervised fine-tuning (SFT), PEFT, LoRA, QLoRA, and the transition to preference optimization methods such as DPO/RLHF.

## Key Terms (Plain English)

- **SFT**: supervised fine-tuning on labeled examples.
- **PEFT**: parameter-efficient fine-tuning (update fewer parameters).
- **LoRA/QLoRA**: PEFT techniques that reduce compute/memory cost.
- **Eval-first**: define evaluation before you train so you know what “better” means.

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

## Expected Outcomes

- You can decide between prompting vs RAG vs fine-tuning for a specific failure mode.
- You can run a small PEFT/LoRA adaptation with a defined eval set.
- You can describe the operational risks (dataset quality, overfit, regressions) and how to gate them.

## Verify Your Work

- Run the notebook from a clean kernel.
- Complete the exercises and write:
  - an eval set description,
  - a regression gate you would block releases on.

## Common Mistakes

- Fine-tuning without an eval set (you can’t tell if you improved).
- Training on small or biased data and overfitting behavior.
- Treating fine-tuning as a replacement for RAG when freshness is required.
