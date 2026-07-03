# 2.3 Probability & Statistics

This lesson builds probabilistic reasoning for uncertainty, inference, and data-driven decision making.

## Why This Matters

Probability and statistics prevent “false confidence”: bad metrics, invalid comparisons, and wrong conclusions from noisy data. This discipline matters even more for LLM evaluation and monitoring, where non-determinism and shifting distributions are common.

## Learning Goals
- Use marginal, joint, and conditional probability correctly.
- Distinguish dependence vs independence and common distribution assumptions.
- Apply descriptive and inferential statistics to practical datasets.

## How It Fits in the Curriculum
Probability/statistics supports model evaluation, risk-aware metrics, and uncertainty handling in ML, LLMOps, and safety lessons.

## Key Terms (Plain English)

- **Conditional probability**: probability of A given B (`P(A|B)`).
- **Distribution**: how values are spread (normal, binomial, etc.).
- **Inference**: drawing conclusions from samples (with uncertainty).

## Start Here
1. Theory: `theory/02-3-probability-and-statistics-titanic.md`
2. Notebook: `notebooks/02-3-probability-and-statistics-titanic.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## Expected Outcomes

- You can compute basic conditional probabilities correctly.
- You can interpret summary statistics and variability.
- You can spot common statistical pitfalls (selection bias, base rates).

## Verify Your Work

- Run the notebook from a clean kernel.
- Complete exercises involving conditional probability and simple inference.

## Common Mistakes

- Confusing correlation with causation.
- Ignoring base rates (especially in rare event classification).
