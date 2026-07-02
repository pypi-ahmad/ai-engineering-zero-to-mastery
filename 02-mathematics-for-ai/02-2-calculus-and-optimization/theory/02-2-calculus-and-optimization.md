# Overview

Training ML models is optimization. Calculus gives local slope information used to update parameters and reduce loss.

# Core Calculus Concepts

## Derivative
For scalar function $f(x)$:
$$
f'(x) = \lim_{h \to 0}\frac{f(x+h)-f(x)}{h}
$$
Derivative measures local rate of change.

## Partial Derivatives and Gradient
For multivariate function $f(w_1,\dots,w_n)$:
$$
\nabla f = \left[\frac{\partial f}{\partial w_1}, \dots, \frac{\partial f}{\partial w_n}\right]
$$
Gradient points toward steepest increase.

## Chain Rule
If $y=f(g(x))$:
$$
\frac{dy}{dx}=\frac{dy}{dg}\cdot\frac{dg}{dx}
$$
Backpropagation in neural networks is repeated chain-rule application.

# Optimization Basics

## Gradient Descent
Parameter update rule:
$$
\theta_{t+1} = \theta_t - \eta \nabla_{\theta} L(\theta_t)
$$
where $\eta$ is learning rate.

## Learning Rate Tradeoff
- Too high: oscillation/divergence.
- Too low: slow convergence and high compute cost.

## Convex vs Non-Convex
- Convex losses: easier global optimization.
- Non-convex losses: local minima/saddles; require careful tuning and diagnostics.

# Calculus & Optimization in ML

- Linear regression minimizes MSE.
- Classification often minimizes cross-entropy.
- Deep models use SGD variants (Adam, RMSProp, etc.) for large parameter spaces.

Think of loss surface as terrain and optimizer as path planner.

# Common Pitfalls

- No feature scaling: elongated loss geometry and unstable updates.
- Missing convergence diagnostics.
- Fixed learning rate where scheduler is needed.
- Ignoring exploding/vanishing gradients in deep models.

# Business Use Cases

- Faster stable convergence reduces training cost.
- Better optimization choices shorten iteration loops and release cycles.
- Stable training lowers risk of degraded nightly retrain jobs.

# Business Case Studies & Exceptions

## Case 1: Divergent Nightly Retrain
Credit model retraining diverged after config change to aggressive learning rate.

Mitigation:
- Lower LR and add scheduler.
- Gradient clipping.
- Alert on NaN/exploding loss.

## Case 2: Slow Convergence Against SLA
Demand model training exceeded daily deadline.

Mitigation:
- Standardize features.
- Warm-start from prior parameters.
- Early stopping on validation plateau.

# Interview Questions & Answers

1. **Q: Explain gradient descent simply.**  
   **A:** Move parameters opposite slope direction to reduce loss step by step.

2. **Q: Why chain rule critical in deep learning?**  
   **A:** It propagates output error influence back to each layer’s parameters.

3. **Q: What if learning rate is too high?**  
   **A:** Training loss can oscillate or diverge.

4. **Q: What if learning rate is too low?**  
   **A:** Convergence is very slow and expensive.

5. **Q: Why normalize features before optimization?**  
   **A:** Better conditioning yields faster, more stable training.

6. **Q: Numerical gradient use case?**  
   **A:** Validate analytic gradient implementation during debugging.

7. **Q: What is gradient clipping?**  
   **A:** Limiting gradient norm/magnitude to stabilize updates.

8. **Q: How monitor convergence?**  
   **A:** Track train/validation loss curves and gradient statistics.

9. **Q: Why can training fail despite correct code?**  
   **A:** Hyperparameters, noisy labels, bad scaling, or data drift.

10. **Q: Business impact of optimization quality?**  
    **A:** Affects cost, reliability, and time-to-production.
