# Overview

Calculus and optimization drive model training by quantifying how loss changes with respect to parameters. Derivatives and gradients tell us which direction reduces error.

# Core Calculus Concepts

- Derivative: local rate of change for single-variable functions.
- Gradient: vector of partial derivatives for multivariable functions.
- Partial derivative: change in one direction while holding others fixed.
- Chain rule (intuitive): compose local sensitivities across nested computations.

# Optimization Basics

- Gradient descent updates parameters opposite the gradient direction.
- Learning rate controls update size.
- Convex vs non-convex: convex surfaces are easier to optimize globally; non-convex landscapes can have local minima/saddles.

# Calculus & Optimization in ML

- Loss minimization in regression/classification uses gradient-based updates.
- Example: minimizing MSE in linear regression with iterative parameter updates.
- Neural network training uses backpropagation (chain rule + gradients).

# Common Pitfalls

- Learning rate too high: divergence/oscillation.
- Learning rate too low: slow convergence.
- Non-convex objectives can stall around poor local regions.

# Business Use Cases

- Faster stable optimization shortens training cycles and compute cost.
- Proper optimization choices improve model quality and reduce deployment delays.

# Interview Prep Checklist

- Explain gradient descent in simple terms.
- Walk through chain rule intuition for loss w.r.t. model weight.
- Distinguish convex and non-convex optimization behavior.
