# 3.2 Unsupervised Learning

This lesson introduces pattern discovery when labels are unavailable: clustering, dimensionality reduction, and exploratory analysis.

## Why This Matters

Many real datasets don’t have clean labels. Unsupervised methods help you explore structure (segments, anomalies) and build intuition before you commit to supervised labels or expensive annotation.

## Learning Goals
- Explain unsupervised learning use-cases and limitations.
- Apply clustering methods and evaluate cluster quality.
- Use representation methods (for example PCA) to simplify high-dimensional data.

## How It Fits in the Curriculum
Unsupervised techniques feed customer segmentation, anomaly detection, and retrieval/indexing foundations for later AI systems.

## Key Terms (Plain English)

- **Clustering**: grouping similar points without labels.
- **Dimensionality reduction**: compressing features while keeping useful structure (e.g., PCA).
- **Silhouette score**: a rough clustering quality measure (not the whole story).

## Start Here
1. Theory: `theory/03-2-unsupervised-learning.md`
2. Notebook: `notebooks/03-2-unsupervised-learning.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## Expected Outcomes

- You can run a clustering method and interpret outputs with caution.
- You can explain why “clusters” are not ground truth.
- You can use PCA to visualize high-dimensional data.

## Verify Your Work

- Run the notebook from a clean kernel.
- Complete the exercises and try a second clustering method to compare behavior.

## Common Mistakes

- Treating clusters as real categories without validation.
- Selecting `k` only by a metric without checking stability/meaning.
- Overinterpreting 2D PCA plots as the full story.
