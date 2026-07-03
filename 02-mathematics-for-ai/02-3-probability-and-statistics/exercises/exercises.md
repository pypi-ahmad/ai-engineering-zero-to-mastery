# Exercises: 2.3 Probability & Statistics

## Exercise 1: Bernoulli Simulation

Simulate `n=10_000` Bernoulli trials with `p=0.3` and compute:

- empirical mean,
- empirical variance.

Expected outcome:
- mean close to `0.3`,
- variance close to `p(1-p)=0.21`.

## Exercise 2: Conditional Probability From Data

Create a small pandas DataFrame with columns:

- `segment` in `{\"A\", \"B\"}`,
- `converted` in `{0,1}`.

Compute:
- `P(converted=1)`,
- `P(converted=1 | segment=\"A\")`,
- `P(segment=\"A\" | converted=1)`.

Expected outcome:
- you can explain which is “precision-like” vs “recall-like” framing.

## Exercise 3: Bayes Rule (Medical Test)

Given:

- prevalence: `P(disease)=0.01`,
- sensitivity: `P(pos|disease)=0.99`,
- false positive rate: `P(pos|no disease)=0.05`,

Compute `P(disease|pos)`.

Expected outcome:
- you can explain why the posterior is not close to 0.99.

## Exercise 4: Confidence Interval for a Proportion

You observe `k=42` successes out of `n=100`.

Compute an approximate 95% CI using:

$$
\\hat p \\pm 1.96 \\sqrt{\\hat p (1-\\hat p)/n}
$$

Expected outcome:
- CI bounds are in `[0,1]`.

## Exercise 5: Independence Check Intuition

Write a short paragraph answering:

- what it means for two events to be independent,
- one way independence can be violated in real datasets (example),
- why “correlation is not causation” matters operationally.

