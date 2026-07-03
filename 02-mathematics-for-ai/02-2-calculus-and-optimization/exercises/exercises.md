# Exercises: 2.2 Calculus & Optimization

## Exercise 1: Numerical Derivative

Write `numerical_derivative(f, x: float, eps: float) -> float` using a central difference:

$$
f'(x) \\approx \\frac{f(x+\\epsilon) - f(x-\\epsilon)}{2\\epsilon}
$$

Expected outcome:
- for `f(x)=x**3`, the derivative near `x=2` is close to `12`.

## Exercise 2: Gradient Descent on a Quadratic

Minimize:

$$
f(w) = (w - 3)^2
$$

Implement gradient descent with:
- multiple learning rates (e.g., `0.01`, `0.1`, `1.1`),
- a fixed number of steps.

Expected outcome:
- you can explain which learning rates converge vs diverge and why.

## Exercise 3: Vector Gradient Check

Let:

$$
f(w) = \\|Aw - b\\|^2
$$

Implement:
- the analytic gradient,
- a numerical gradient check for a random `w`.

Expected outcome:
- analytic and numerical gradients match closely.

## Exercise 4: Autograd Sanity Check (PyTorch)

Use PyTorch to compute the gradient of:

$$
f(w) = \\sum_i (w_i^2)
$$

Expected outcome:
- gradient equals `2w`.

## Exercise 5: “Bad Learning Rate” Diagnosis Note

Write a short note (5–8 lines) answering:
- what symptoms indicate learning rate too high,
- what symptoms indicate learning rate too low,
- one safe mitigation strategy for each.

