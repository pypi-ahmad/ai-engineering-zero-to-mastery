# Lesson 3: Classical Machine Learning

This module covers core ML paradigms and model families used in many production systems, including strong baselines for deep/GenAI projects.

## Why This Matters

Classical ML provides strong baselines and the evaluation discipline you’ll reuse everywhere. Many real products ship “boring” models that win because the data pipeline and evaluation are solid.

## Learning Goals
- Master supervised and unsupervised learning fundamentals.
- Compare model families using robust evaluation workflows.
- Build defensible model-selection decisions based on metrics and constraints.

## Expected Outcomes

- You can train multiple model families and compare them fairly.
- You can identify leakage and prevent it with proper splits.
- You can choose metrics and thresholds based on real costs of errors.

## How It Fits in the Curriculum
Lesson 3 is the bridge between math foundations (Lesson 2) and deep learning/GenAI systems (Lessons 4+). It also supplies baseline models for MLOps lessons.

## Sub-lessons
- `3.1 Supervised Learning`
- `3.2 Unsupervised Learning`
- `3.3 Model Evaluation & Selection`

## Artifacts
Each sub-lesson includes:
- `theory/` chapter markdown (+ PDF export)
- `notebooks/` runnable experiments and comparisons

## How to Use This Lesson
1. Start with `3.1` for regression/classification foundations.
2. Continue to `3.2` for label-free pattern discovery.
3. Finish with `3.3` to formalize evaluation and selection.

## Verify Your Work

- Complete the `exercises/` for 3.1 and 3.3 (minimum recommended).
- Produce a short “model decision note”:
  - chosen baseline,
  - key metric(s),
  - why this model is acceptable to ship as v0.

## Bridge from Lesson 2
**Why this follows:** mathematical foundations now become operational ML workflows with measurable performance trade-offs.

**You should already know:** vectors/matrices, gradients, probability, and statistical inference basics.

**What you will do next:** train baseline models, compare families, and make defensible model choices.

## Bridge to Lesson 4
Lesson 4 scales these principles into deep learning: neural networks, optimization stability, CNNs, and transformer foundations.
