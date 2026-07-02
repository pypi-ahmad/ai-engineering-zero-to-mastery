# Overview

Probability models uncertainty; statistics summarizes and interprets data behavior. AI systems depend on both for risk-aware decision making, evaluation, and monitoring.

Titanic dataset is compact, interpretable, and useful for conditional probability practice.

# Core Probability Concepts

- **Sample space** $\Omega$: all possible outcomes.
- **Event** $A$: subset of outcomes.
- **Probability** $P(A)$: value in $[0,1]$.

## Marginal, Joint, Conditional Probability
- Marginal: $P(A)$
- Joint: $P(A \cap B)$
- Conditional:
$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B)>0
$$

## Independence vs Dependence
Events are independent if:
$$
P(A \cap B)=P(A)P(B)
$$
Otherwise, observing one event changes belief about the other.

# Core Statistics Concepts

- Mean:
$$
\mu = \frac{1}{n}\sum_i x_i
$$
- Variance:
$$
\sigma^2 = \frac{1}{n}\sum_i (x_i - \mu)^2
$$
- Standard deviation: $\sigma = \sqrt{\sigma^2}$
- Median and quantiles for robust center/spread.

Common distributions (high-level): Bernoulli, Binomial, Normal.

# Probability & Statistics on Titanic

Questions:
- Baseline survival probability $P(\text{survived})$.
- Conditional survival:
  - $P(\text{survived} \mid \text{sex=female})$
  - $P(\text{survived} \mid \text{pclass}=1)$
- Distribution shifts in `age` and `fare` between groups.

# Common Pitfalls

- Confusing correlation with causation.
- Ignoring missing values and denominator size.
- Reporting global averages without subgroup context.

# Business Use Cases

- Risk scoring and triage.
- Resource allocation under uncertainty.
- Prioritization queues based on conditional probabilities.

# Business Case Studies & Exceptions

## Case 1: Risk-Based Review Queue
Manual review team has limited capacity. Using unconditional event rate under-prioritized high-risk subgroups.

Mitigation:
- Use conditional probabilities by cohort.
- Calibrate and monitor subgroup rates.

## Case 2: Tail-Risk Blindness
Planning based on average costs ignored upper-tail behavior and caused budget overruns.

Mitigation:
- Track quantiles and tail metrics.
- Segment analysis by population type.

# Interview Questions & Answers

1. **Q: Define conditional probability.**  
   **A:** Probability of event $A$ given $B$ occurred, equal to $P(A \cap B)/P(B)$ when $P(B)>0$.

2. **Q: Independence meaning?**  
   **A:** Occurrence of one event does not change probability of the other.

3. **Q: Mean vs median with outliers?**  
   **A:** Median is more robust; mean is more sensitive to extreme values.

4. **Q: Why variance important in ML?**  
   **A:** It quantifies spread/uncertainty affecting model confidence and calibration.

5. **Q: Titanic conditional example?**  
   **A:** Compare survival probability by passenger class or sex.

6. **Q: Why avoid causal claims from observational data?**  
   **A:** Confounding variables can create spurious associations.

7. **Q: When use quantiles?**  
   **A:** For tail-risk thresholds and robust business cutoffs.

8. **Q: How handle missing data in probability estimates?**  
   **A:** Inspect missingness mechanism, impute/drop thoughtfully, and report impact.

9. **Q: Value of probabilistic outputs in business systems?**  
   **A:** Enables ranking and risk-based decisions instead of binary-only rules.

10. **Q: Effect of class imbalance?**  
    **A:** Base-rate skew can distort naive interpretation of metrics and probabilities.
