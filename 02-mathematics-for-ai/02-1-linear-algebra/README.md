# 2.1 Linear Algebra

This lesson covers vectors, matrices, similarity, and linear transformations used throughout ML and deep learning systems.

## Why This Matters

Linear algebra shows up everywhere in AI engineering: feature matrices, embeddings, similarity search, and neural network layers. If you can reason about shapes and similarity, you can debug many “mystery” model issues quickly.

## Learning Goals
- Work with vector/matrix operations and dimensional reasoning.
- Understand dot products, norms, cosine similarity, and matrix multiplication.
- Relate linear algebra to regression, embeddings, and representation learning.

## How It Fits in the Curriculum
Linear algebra is foundational for model architectures, gradient-based training, and retrieval systems in later lessons.

## Key Terms (Plain English)

- **Vector**: an ordered list of numbers (a point or representation).
- **Matrix**: a table of numbers (often `n_samples x n_features` in ML).
- **Dot product**: a similarity-like operation between vectors.
- **Cosine similarity**: similarity based on angle (common for embeddings).

## Start Here
1. Theory: `theory/02-1-linear-algebra-for-ml-and-ai.md`
2. Notebook: `notebooks/02-1-linear-algebra-for-ml-and-ai.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## Expected Outcomes

- You can compute and interpret dot product and cosine similarity.
- You can sanity-check matrix shapes before coding.
- You can explain why embeddings enable retrieval/search.

## Verify Your Work

- Run the notebook from a clean kernel.
- Complete the exercises and compute similarity between two short text embeddings (toy vectors are fine).

## Common Mistakes

- Mixing up rows vs columns (samples vs features).
- Applying cosine similarity without normalizing vectors (or misunderstanding what it measures).
