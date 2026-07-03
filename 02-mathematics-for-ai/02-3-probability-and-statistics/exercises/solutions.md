# Solutions: 2.3 Probability & Statistics

## Exercise 1: Bernoulli Simulation

```python
import numpy as np\n\nrng = np.random.default_rng(42)\n\nn = 10_000\np = 0.3\nx = rng.binomial(n=1, p=p, size=n)\n\nprint(\"mean:\", float(x.mean()))\nprint(\"var :\", float(x.var()))\nprint(\"theory var:\", p * (1 - p))\n```

## Exercise 2: Conditional Probability From Data

```python
import pandas as pd\n\n\ndf = pd.DataFrame(\n    {\n        \"segment\": [\"A\", \"A\", \"A\", \"B\", \"B\", \"B\", \"B\"],\n        \"converted\": [1, 0, 1, 0, 0, 1, 0],\n    }\n)\n\np_conv = df[\"converted\"].mean()\n\np_conv_a = df.loc[df[\"segment\"] == \"A\", \"converted\"].mean()\n\np_a_given_conv = (df[(df[\"segment\"] == \"A\") & (df[\"converted\"] == 1)].shape[0]) / (\n    df[df[\"converted\"] == 1].shape[0]\n)\n\nprint(\"P(converted=1):\", float(p_conv))\nprint(\"P(converted=1|A):\", float(p_conv_a))\nprint(\"P(A|converted=1):\", float(p_a_given_conv))\n```

## Exercise 3: Bayes Rule (Medical Test)

```python
p_d = 0.01\np_pos_given_d = 0.99\np_pos_given_not = 0.05\n\np_not = 1 - p_d\np_pos = p_pos_given_d * p_d + p_pos_given_not * p_not\np_d_given_pos = (p_pos_given_d * p_d) / p_pos\n\nprint(p_d_given_pos)\n```

This is the base-rate effect: when prevalence is low, false positives dominate.

## Exercise 4: Confidence Interval for a Proportion

```python
import math\n\nk = 42\nn = 100\np_hat = k / n\nse = math.sqrt(p_hat * (1 - p_hat) / n)\nlo = p_hat - 1.96 * se\nhi = p_hat + 1.96 * se\nprint((max(0.0, lo), min(1.0, hi)))\n```

## Exercise 5: Independence Check Intuition

Key points:

- Independence: `P(A and B) = P(A)P(B)` and `P(A|B)=P(A)` (if `P(B)>0`).
- Violations: selection bias, confounding, time leakage, non-stationarity, cohort drift.
- Operationally: a correlated feature can break under distribution shift; causal thinking helps you choose robust signals.

