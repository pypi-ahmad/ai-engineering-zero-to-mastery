# 2.2 Calculus & Optimization

This lesson explains derivatives, gradients, and optimization dynamics that drive model training.

## Why This Matters

Training deep models is optimization. If you understand gradients and stability, you can diagnose common training failures (divergence, slow learning, exploding/vanishing gradients) instead of guessing.

## Learning Goals
- Compute and interpret derivatives/gradients in ML settings.
- Understand chain rule intuition behind backpropagation.
- Reason about learning rates, convergence, and optimization stability.

## How It Fits in the Curriculum
These concepts directly power deep learning training workflows in Lesson 4 and optimization choices throughout the curriculum.

## Key Terms (Plain English)

- **Derivative/gradient**: how much the loss changes when parameters change.
- **Learning rate**: step size for updates (too high diverges, too low crawls).
- **Convergence**: when training stops improving meaningfully.

## Start Here
1. Theory: `theory/02-2-calculus-and-optimization.md`
2. Notebook: `notebooks/02-2-calculus-and-optimization.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## Expected Outcomes

- You can explain gradient descent with an example.
- You can reason about learning rate effects.
- You can connect the chain rule intuition to backprop at a high level.

## Verify Your Work

- Run the notebook from a clean kernel.
- Complete the gradient-check style exercises (numeric vs analytic).

## Common Mistakes

- Treating learning rate as a magic knob without understanding stability.
- Confusing “loss decreasing” with “model generalizing”.
