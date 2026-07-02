# Overview

Linear algebra is foundational for AI/ML because models represent inputs, features, embeddings, and weights as vectors and matrices. From recommendation ranking to neural network forward passes, matrix operations are at the core.

# Core Concepts

- Scalars, vectors, matrices, and tensors.
- Matrix operations: addition, multiplication, transpose.
- Dot product, vector norm, and cosine similarity.
- Eigenvalues/eigenvectors (intuitive): directions that keep orientation under transformation.
- SVD (intuitive): factorizing a matrix into components that capture dominant structure.

# Linear Algebra in ML/AI

- Linear regression can be written in matrix form for compact training/prediction logic.
- Embeddings rely on vector spaces where similarity is computed with dot/cosine metrics.
- Neural network layers compute matrix multiplications with biases and nonlinear activations.

# Common Pitfalls

- Shape mismatches such as `(n, m)` multiplied against incompatible vectors.
- Mixing row/column assumptions and getting silent broadcast errors.
- Numerical instability with poorly scaled features or near-singular matrices.

# Business Use Cases

- Recommendation systems with user/item embeddings.
- Semantic search via vector similarity.
- Dimensionality reduction for analytics and feature compression.

# Interview Prep Checklist

- Define dot product and cosine similarity clearly.
- Explain matrix multiplication in linear models.
- Describe how embeddings rely on linear algebra operations.
- Give a high-level intuition for eigenvalues and SVD in ML workflows.
