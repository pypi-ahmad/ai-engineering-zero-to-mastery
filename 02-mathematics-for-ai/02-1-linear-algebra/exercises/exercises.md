# Exercises: 2.1 Linear Algebra

## Exercise 1: Cosine Similarity (Correctness)

Implement `cosine_similarity(a: np.ndarray, b: np.ndarray) -> float`.

Rules:
- validate that `a` and `b` are 1D and have the same length,
- return a Python `float`,
- handle zero vectors by raising a clear `ValueError`.

Expected outcome:
- `cosine_similarity(x, x) == 1.0` for non-zero `x`.

## Exercise 2: Shape Reasoning

For each pair, write whether multiplication is valid, and if valid, the output shape:

1. `(3, 5) @ (5, 2)`
2. `(10,) @ (10,)`
3. `(4, 4) @ (4,)`
4. `(4,) @ (4, 4)`

Expected outcome:
- you can explain the rule in one sentence.

## Exercise 3: Least Squares From Scratch

Using a small synthetic dataset:

- generate `X` with shape `(n, d)`,
- generate `y = X @ w_true + noise`,
- estimate `w_hat` using the normal equation.

Expected outcome:
- `w_hat` is close to `w_true` (up to noise).

## Exercise 4: Projection Error

Write code that:

- creates two vectors `u` and `v`,
- projects `v` onto `u`,
- computes the residual `r = v - proj_u(v)`.

Expected outcome:
- `u` is orthogonal to `r` (dot product close to 0).

## Exercise 5: Nearest Neighbor by Dot Product

Given an embedding matrix `E` of shape `(n, d)` and a query `q` of shape `(d,)`, return the index of the best match using:

1. raw dot product
2. cosine similarity

Expected outcome:
- you can explain when these give the same ranking.

