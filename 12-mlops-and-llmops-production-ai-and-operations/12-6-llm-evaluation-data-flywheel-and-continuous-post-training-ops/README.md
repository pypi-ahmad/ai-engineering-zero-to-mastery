# 12.6 LLM Evaluation, Data Flywheel & Continuous Post-Training Ops

This sub-lesson covers the quality-control engine of LLMOps: evaluation harnesses, release gates, failure-driven data flywheels, and continuous post-training operations.

## What You Will Learn
- Offline, online, human, and safety evaluation layers.
- Release gate design and regression control.
- Data flywheel loops from production failures to better models.
- Canary, rollback, and incident response for tuned models.

## Start Here
- Theory: `theory/12-6-llm-evaluation-data-flywheel-and-continuous-post-training-ops.md`
- Notebook: `notebooks/12-6-llm-evaluation-and-post-training-ops-playbook.ipynb`

## Prerequisites
- Lesson 12.1 to 12.5
- Familiarity with model evaluation and LLM application basics

## Why This Matters
Without disciplined eval and data loops, LLM quality decays silently in production and releases become high-risk.
