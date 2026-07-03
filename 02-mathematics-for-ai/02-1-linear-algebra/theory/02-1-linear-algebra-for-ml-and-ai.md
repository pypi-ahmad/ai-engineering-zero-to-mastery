# Overview

Linear algebra is the language of ML. Feature vectors, embedding spaces, neural network layers, and many optimization routines are matrix operations.

Core idea:
Represent data and transformations in vector spaces so that learning becomes a problem of geometric and algebraic optimization.

Why this matters operationally: almost every performance-critical path in modern ML is batched linear algebra. Training loops, embedding retrieval, attention projections, and feature transforms all depend on shape-safe, numerically stable matrix operations. When teams misunderstand dimensions or conditioning, they often ship models with hidden instability or expensive runtime errors.

Practical engineering pattern:
- Treat shapes as contracts (`[batch, features]`, `[features, hidden]`).
- Add explicit assertions at data and model boundaries.
- Prefer stable numerical routines (SVD/QR/solve) over naive inversion.
- Track vector normalization strategy when using similarity search.

# Core Concepts

## Scalars, Vectors, Matrices, Tensors

- Scalar: single value in $\mathbb{R}$.
- Vector: ordered 1-D element in $\mathbb{R}^n$.
- Matrix: 2-D linear map representation in $\mathbb{R}^{m \times n}$.
- Tensor: higher-dimensional generalization.

Interpretation for AI:
- A row in a tabular dataset is often a feature vector.
- A weight matrix transforms one representation into another.

## Matrix Operations

For $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{n \times p}$:
$$
C = AB \in \mathbb{R}^{m \times p}
$$

Matrix multiplication is not elementwise multiplication; it composes linear transformations.

Transpose:
$$
(A^T)_{ij} = A_{ji}
$$

Identity matrix $I$ is neutral element:
$$
AI = IA = A
$$

## Dot Product, Norm, Cosine Similarity

Dot product:
$$
a \cdot b = \sum_i a_i b_i
$$

Euclidean norm:
$$
\|a\|_2 = \sqrt{\sum_i a_i^2}
$$

Cosine similarity:
$$
\cos(\theta) = \frac{a \cdot b}{\|a\|_2\|b\|_2}
$$

Interpretation:
- Dot product combines direction and magnitude.
- Cosine similarity emphasizes angle (directional similarity), common in embedding retrieval.

## Eigenvalues, Eigenvectors, SVD (Intuition)

Eigen relation:
$$
Av = \lambda v
$$

Meaning: vector $v$ keeps direction under transformation by $A$, scaled by $\lambda$.

SVD factorization:
$$
A = U\Sigma V^T
$$

Why SVD matters:
- Dimensionality reduction
- Denoising
- Latent factor extraction

Diagram in words:
Imagine a cloud of points. SVD finds rotated axes aligned with the directions of maximum spread. Keeping top axes compresses data while preserving major structure.

# Linear Algebra in ML/AI

## Linear Regression in Matrix Form

Model:
$$
\hat{y} = X\theta
$$

Least-squares objective:
$$
\min_{\theta} \|X\theta - y\|_2^2
$$

Closed-form (normal equation when invertible):
$$
\theta = (X^T X)^{-1}X^T y
$$

Numerically safer practice:
- Prefer pseudo-inverse or QR/SVD-based solvers over raw matrix inverse for ill-conditioned problems.

## Embeddings and Similarity Search

Represent text/users/items as vectors. Retrieval often ranks candidates by cosine similarity or inner product.

Practical caveat:
- Similarity metric choice affects retrieval behavior.
- Normalization and index strategy matter for quality and latency.

## Neural Network Layers

Dense layer:
$$
h = \sigma(Wx + b)
$$

Batched form:
$$
H = \sigma(XW + b)
$$
where broadcasting adds bias to each row.

# Common Pitfalls

- Shape mismatch and accidental broadcasting.
- Confusing row-vectors with column-vectors.
- Using matrix inverse directly on unstable matrices.
- Ignoring feature scaling before optimization.

# Business Use Cases

- Recommender systems via user/item embeddings.
- Semantic search in RAG pipelines.
- Dimensionality reduction for monitoring dashboards.
- Matrix factorization for sparse interaction data.

Real-world example: in customer-support retrieval, sentence embeddings are indexed in a vector store. If vectors are not normalized consistently between indexing and query time, ranking quality can degrade even when the model is unchanged. Teams often misdiagnose this as "model drift" when it is actually a linear-algebra contract mismatch.

# Business Case Studies & Exceptions

## Case 1: Embedding Search Quality Drop

Scenario:
Domain vocabulary shifts after product launch; embedding retrieval starts returning semantically weak neighbors.

Fix pattern:
- Re-embed corpus with domain-adapted model.
- Normalize vectors consistently.
- Add reranking and metadata filters.
- Track precision@k by segment.

Exception:
When legal/compliance requires deterministic lexical match, pure embedding similarity may be insufficient; combine vector and rules-based retrieval.

## Case 2: Linear Solve Instability in Forecasting Model

Scenario:
Highly collinear features make $X^TX$ near-singular.

Fix pattern:
- Standardize features.
- Use regularization (ridge) or pseudo-inverse.
- Monitor condition number.

## Case 3: Matrix Shape Bug in Inference Service

Scenario:
Single-sample requests lose batch dimension and silently broadcast wrong outputs.

Fix pattern:
- Explicit shape assertions at API boundary.
- Contract tests for single and batch inference.

# Interview Questions & Answers

1. **Q: Why is matrix multiplication central to ML?**
   **A:** Most model computations are linear transforms over feature vectors/batches.

2. **Q: Dot product vs cosine similarity?**
   **A:** Dot product includes magnitude; cosine normalizes magnitude and compares direction.

3. **Q: When is cosine preferred in embeddings?**
   **A:** When direction matters more than vector norm.

4. **Q: Why can direct matrix inverse be risky?**
   **A:** Near-singular matrices amplify numerical error and destabilize estimates.

5. **Q: What is SVD intuition?**
   **A:** Decompose a matrix into rotation-scaling-rotation; top singular directions capture dominant structure.

6. **Q: What does an eigenvalue represent?**
   **A:** Scaling factor along its corresponding eigenvector direction.

7. **Q: Why should shape checks be explicit in production code?**
   **A:** Broadcasting can produce silent wrong results instead of loud failures.

8. **Q: How does linear algebra connect to neural nets?**
   **A:** Every dense/attention projection is matrix multiplication plus nonlinearity.

9. **Q: Why normalize vectors before similarity search?**
   **A:** Prevent large norms from dominating ranking when semantic direction is the target.

10. **Q: Give one business metric impacted by linear algebra quality.**
    **A:** Retrieval precision@k in search/recommendation systems.

11. **Q: Why is shape discipline important for production ML APIs?**
    **A:** It prevents silent broadcasting bugs and guarantees consistent behavior for single vs batch requests.

12. **Q: When should you prefer `solve`/SVD over explicit inverse?**
    **A:** For better numerical stability on ill-conditioned or near-singular systems.

13. **Q: How does normalization affect vector retrieval?**
    **A:** It changes whether magnitude dominates ranking; cosine-style retrieval typically expects normalized vectors.

14. **Q: What is one sign of linear-algebra contract drift in production?**
    **A:** Sudden quality regression without model-weight changes, often due to preprocessing/shape mismatch.

15. **Q: Why do batched operations matter beyond speed?**
    **A:** They also enforce consistent tensor shapes and reduce per-request logic variance.

# References

- NumPy linear algebra docs: https://numpy.org/doc/stable/reference/routines.linalg.html
- scikit-learn decomposition guide: https://scikit-learn.org/stable/modules/decomposition.html
- Dive into Deep Learning (linear algebra): https://d2l.ai/chapter_preliminaries/linear-algebra.html
