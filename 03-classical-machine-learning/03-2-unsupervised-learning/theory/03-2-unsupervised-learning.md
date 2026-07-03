# Overview

Unsupervised learning finds structure in unlabeled data. Instead of predicting known targets, models infer patterns such as clusters, latent factors, or anomalous behavior.

# Core Definitions

- **Unsupervised learning:** learning patterns from $X$ without explicit $y$ labels.
- **Clustering:** grouping points with high within-group similarity and low between-group similarity.
- **Dimensionality reduction:** mapping high-dimensional data to a lower-dimensional representation while preserving useful structure.

# Clustering Methods

## k-Means

Objective:
$$
\min_{\{C_k\}_{k=1}^{K}} \sum_{k=1}^{K}\sum_{x_i\in C_k} \|x_i - \mu_k\|_2^2
$$

Algorithm steps:
1. Initialize $K$ centroids.
2. Assign each point to nearest centroid.
3. Recompute centroids.
4. Repeat until convergence.

Strengths:
- Fast and scalable

Limitations:
- Must choose $K$ in advance
- Assumes roughly spherical/equal-variance clusters

## Hierarchical Clustering

Builds nested clusters (dendrogram) via agglomerative merges or divisive splits.

Strengths:
- No strict need for a single global $K$ during construction
- Interpretable tree of merges

Limitations:
- Computationally heavier for large datasets

## DBSCAN

Density-based clustering using `eps` and `min_samples`.

Per scikit-learn docs, DBSCAN identifies core points, expands clusters from dense regions, can find arbitrary shapes, and labels outliers as noise.

Strengths:
- Handles non-spherical clusters
- Naturally detects noise points

Limitations:
- Sensitive to density parameter choices
- Performance can degrade with varying density scales

# Dimensionality Reduction

## PCA

Linear projection maximizing explained variance.

Use-cases:
- Compression
- Denoising
- Visualization pre-processing

## t-SNE and UMAP (High-Level)

Nonlinear manifold visualization methods emphasizing local neighborhood structure.

Caution:
Use mainly for exploration/visualization, not as sole quantitative evidence for business decisions.

# Distance and Similarity

Distance metrics influence clustering outcomes:
- Euclidean
- Manhattan
- Cosine distance

Feature scaling is usually required before distance-based clustering.

Diagram in words:
Imagine points drawn on paper. Changing metric is like changing the ruler geometry; nearest neighbors can change even if points stay fixed.

# Model Selection Cheat Sheet (Unsupervised)

Use this practical heuristic:

- **k-means** when clusters are roughly compact/spherical and scale is large.
- **Hierarchical** when interpretability of merge structure matters.
- **DBSCAN** when noise handling and arbitrary cluster shapes are important.
- **PCA + clustering** when high dimensionality introduces noise and redundancy.

Decision questions:
1. Do you know expected number of groups?
2. Are clusters density-based or centroid-like?
3. Is outlier detection part of the requirement?
4. Must results be explainable to non-technical stakeholders?

# Common Pitfalls

- Forcing k-means on arbitrary-shape clusters.
- Choosing $K$ by aesthetics only.
- Treating t-SNE geometry as globally accurate.
- Ignoring feature scaling and outlier effects.

# Edge Cases and Failure Modes

1. **High-dimensional sparse vectors**
- Distance concentration can reduce cluster separation.
- Apply dimensionality reduction or metric learning before clustering.

2. **Mixed feature types (numeric + categorical)**
- Euclidean distance can be inappropriate.
- Use suitable encoding and possibly mixed-distance alternatives.

3. **Business-required fixed segment counts**
- Statistical optimum and operational constraints may diverge.
- Document trade-off explicitly and validate downstream impact.

# Business Case Studies & Exceptions

## Case 1: Customer Segmentation

Scenario:
A retailer clusters customers for campaign targeting.

Pattern:
- Standardize behavior variables.
- Compare k-means and hierarchical clusters.
- Validate segments using silhouette score and business interpretability.

Exception:
If segments are operationally constrained (e.g., exactly 4 marketing programs), business constraints may override pure metric optimum.

## Case 2: Anomaly Detection via Cluster Distance

Scenario:
Distance-to-centroid used for anomaly flagging.

Pattern:
- Compute distance distribution per segment.
- Set segment-aware thresholds.
- Add human review loop for high-impact alerts.

Exception:
For safety-critical contexts, density/model-based anomaly methods may be required beyond simple distance thresholds.

## Case 3: Varying Density Data and DBSCAN Instability

Scenario:
Single global `eps` fails across dense and sparse regions.

Pattern:
- Tune with k-distance diagnostics.
- Evaluate alternate methods (HDBSCAN-like approaches) if density varies strongly.

# Interview Questions & Answers

1. **Q: Clustering vs classification?**
   **A:** Clustering discovers groups without labels; classification predicts predefined labeled classes.

2. **Q: How does k-means work?**
   **A:** Alternate assignment to nearest centroid and centroid recomputation to minimize within-cluster SSE.

3. **Q: How choose k for k-means?**
   **A:** Combine silhouette/elbow/stability checks with domain and operational constraints.

4. **Q: Why might DBSCAN outperform k-means?**
   **A:** It can capture arbitrary-shape clusters and detect outliers without pre-setting number of clusters.

5. **Q: Why scale features before clustering?**
   **A:** Distance calculations are scale-sensitive; large-scale features otherwise dominate.

6. **Q: What does silhouette score measure?**
   **A:** Relative cohesion vs separation of clusters (higher generally better).

7. **Q: What is one limitation of t-SNE?**
   **A:** Global distances and cluster sizes may not reflect true high-dimensional geometry.

8. **Q: Why is unsupervised validation hard?**
   **A:** There are no labels; quality must be inferred from internal metrics and business utility.

9. **Q: When use PCA before clustering?**
   **A:** To reduce noise/redundancy and potentially improve cluster separability.

10. **Q: What is a practical failure mode in segmentation projects?**
    **A:** Segments that look statistically distinct but are not actionable for business operations.

11. **Q: Why can high-dimensional data break distance-based intuition?**
    **A:** Distances become less discriminative, making neighbor relationships unstable.

12. **Q: When should you prefer DBSCAN over k-means?**
    **A:** When data has non-spherical cluster structure and meaningful noise points.

13. **Q: Why is cluster “actionability” as important as silhouette score?**
    **A:** Clusters must map to decisions/workflows, not only mathematical separation.

14. **Q: What is one robust way to validate unsupervised segments?**
    **A:** Check stability across resamples and interpretability with domain experts.

15. **Q: Why is t-SNE risky for business decisions on its own?**
    **A:** It is primarily visualization-oriented and may distort global structure.

# References

- scikit-learn clustering guide: https://scikit-learn.org/stable/modules/clustering.html
- KMeans docs: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
- DBSCAN docs: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html
- Silhouette example: https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html
