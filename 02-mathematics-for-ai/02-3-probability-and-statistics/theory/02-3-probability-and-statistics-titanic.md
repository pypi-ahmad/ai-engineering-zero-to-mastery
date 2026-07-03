# Overview

Probability models uncertainty; statistics summarizes and infers structure from data. ML systems rely on both to produce calibrated decisions under incomplete information.

This chapter uses Titanic-style analysis to connect formal concepts with practical intuition.

# Core Probability Concepts

Let sample space be $\Omega$ and event $A \subseteq \Omega$.

- Probability: $P(A) \in [0,1]$
- Complement: $P(A^c) = 1 - P(A)$

## Random Variables and Events

A random variable maps outcomes to numbers:
$$
X: \Omega \rightarrow \mathbb{R}
$$

Types:
- Discrete (countable outcomes)
- Continuous (range of real values)

## Marginal, Joint, Conditional Probability

- Marginal: $P(A)$
- Joint: $P(A \cap B)$
- Conditional:
$$
P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0
$$

Bayes' rule:
$$
P(A|B) = \frac{P(B|A)P(A)}{P(B)}
$$

## Independence vs Dependence

Events are independent if:
$$
P(A \cap B) = P(A)P(B)
$$

In real business data, true independence is rare; dependencies are common and often segment-specific.

# Core Statistics Concepts

## Summary Statistics

- Mean:
$$
\mu = \frac{1}{n}\sum_{i=1}^{n} x_i
$$
- Variance:
$$
\sigma^2 = \frac{1}{n}\sum_{i=1}^{n}(x_i-\mu)^2
$$
- Standard deviation: $\sigma = \sqrt{\sigma^2}$
- Median/quantiles: robust central tendency and spread

## Common Distributions (High-Level)

- Bernoulli: binary outcome
- Binomial: count of successes in fixed trials
- Normal: symmetric bell-shaped distribution
- Poisson: event counts over interval

# Probability & Statistics on Titanic-Style Data

Typical questions:
- Baseline survival probability $P(\text{survived})$
- Conditional probabilities by subgroup
- Distribution shifts across classes/genders/age bands

Example conditional interpretation:
$P(\text{survived}|\text{class}=1)$ is not causal proof that class caused survival; it quantifies association in observed data.

Diagram in words:
Imagine two bar charts of survival rates by subgroup. Large differences suggest dependence between subgroup and outcome, but causality still requires stronger assumptions.

# Worked Titanic-Style Calculation

Suppose a sample has:
- 500 passengers total
- 200 survived
- 120 first-class passengers
- 84 first-class survivors

Then:
$$
P(\text{survived}) = \frac{200}{500} = 0.4
$$
$$
P(\text{class}=1) = \frac{120}{500} = 0.24
$$
$$
P(\text{survived} \mid \text{class}=1) = \frac{84}{120} = 0.7
$$

Interpretation:
First-class survival rate is higher in this sample, but this does not prove a causal mechanism without controlling for confounders.

# Edge Cases in Probability and Statistics Workflows

1. **Rare subgroups**
- Conditional rates become unstable with tiny denominators.
- Use confidence intervals or smoothing before operational decisions.

2. **Class imbalance**
- Accuracy may look good while minority-class risk is poorly handled.
- Prefer class-aware metrics and subgroup reporting.

3. **Simpson’s paradox**
- Aggregate trend can reverse within subgroups.
- Always inspect key segment-level statistics.

4. **Missing-not-at-random**
- Dropping records can bias both descriptive and inferential results.
- Analyze missingness mechanism explicitly.

# Common Pitfalls

- Confusing association with causation.
- Ignoring denominator size for subgroup rates.
- Dropping missing values without checking bias.
- Reporting only averages while ignoring tail risk.

# Business Use Cases

- Risk triage and prioritization queues.
- Capacity planning under uncertain demand.
- Alert thresholds driven by conditional event rates.

# Business Case Studies & Exceptions

## Case 1: Risk-Based Review Queue

Scenario:
Limited manual-review capacity allocated using global event rates only.

Impact:
High-risk cohorts under-prioritized.

Fix pattern:
- Use conditional probabilities by segment.
- Calibrate segment-level thresholds.
- Monitor subgroup performance drift.

Exception:
When subgroup data is very sparse, naive conditional estimates are unstable; apply smoothing or hierarchical pooling.

## Case 2: Tail-Risk Blindness in Cost Forecasting

Scenario:
Team planned using mean costs only.

Impact:
Frequent budget overruns due to ignored upper quantiles.

Fix pattern:
- Track p90/p95/p99.
- Stress-test scenarios for tail events.

## Case 3: Missingness-Induced Bias

Scenario:
Rows with missing age were dropped; resulting sample skewed to certain groups.

Fix pattern:
- Analyze missingness mechanism.
- Compare imputation strategies and subgroup impacts.

# Interview Questions & Answers

1. **Q: Define conditional probability.**
   **A:** Probability of event A after restricting sample space to event B: $P(A|B)=P(A\cap B)/P(B)$.

2. **Q: What does independence mean?**
   **A:** Observing one event does not change probability of the other.

3. **Q: Mean vs median when outliers exist?**
   **A:** Median is typically more robust to outliers.

4. **Q: Why are quantiles useful in business systems?**
   **A:** They reflect tail behavior critical for risk and capacity planning.

5. **Q: What is one danger of subgroup analysis?**
   **A:** Small sample sizes can produce noisy, misleading rates.

6. **Q: Why does missing data handling matter for inference?**
   **A:** Different missingness treatments can change estimated probabilities and conclusions.

7. **Q: What is Bayes' rule used for in ML contexts?**
   **A:** Updating beliefs/probabilities when new evidence arrives.

8. **Q: Is high conditional survival in one group proof of causality?**
   **A:** No, it is an association unless confounding is addressed.

9. **Q: Why does base rate matter?**
   **A:** Rare-event prevalence strongly affects interpretation of model outputs and metrics.

10. **Q: Give one practical output of descriptive statistics before modeling.**
    **A:** Data quality and segment diagnostics that guide preprocessing and metric design.

11. **Q: Why can high subgroup survival rate still be misleading?**
    **A:** It may reflect confounding variables rather than direct causal effect.

12. **Q: What is a practical safeguard against unstable subgroup estimates?**
    **A:** Minimum sample-size thresholds and confidence intervals before actioning rates.

13. **Q: What is Simpson’s paradox in plain terms?**
    **A:** A trend seen in aggregate data reverses when data is split by meaningful groups.

14. **Q: Why is denominator awareness critical in conditional probability dashboards?**
    **A:** Small denominators can create large, noisy rate swings.

15. **Q: When is median preferred over mean in reporting?**
    **A:** In skewed distributions or outlier-heavy settings where robustness matters.

# References

- Khan Academy probability/statistics: https://www.khanacademy.org/math/statistics-probability
- ISLR official site: https://www.statlearning.com/
- SciPy stats docs: https://docs.scipy.org/doc/scipy/reference/stats.html
