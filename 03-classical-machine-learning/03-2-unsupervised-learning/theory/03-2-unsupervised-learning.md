# Overview

Unsupervised learning discovers structure in unlabeled data. Instead of predicting known targets, models infer clusters, latent dimensions, or anomaly patterns.

# Core Definitions

- **Clustering:** group samples with high intra-group similarity and low inter-group similarity.
- **Dimensionality reduction:** map high-dimensional data to lower-dimensional representation while preserving useful structure.

# Clustering Methods

## k-Means
Optimizes within-cluster sum of squares:
$$\min_{\{C_k\}} \sum_{k=1}^{K}\sum_{x_i\in C_k} \|x_i-\mu_k\|^2$$
Fast and popular, but assumes roughly spherical clusters.

## Hierarchical Clustering
Builds cluster tree (dendrogram) via agglomerative merges or divisive splits.

## DBSCAN
Density-based clustering with parameters `eps` and `min_samples`. Finds arbitrary-shaped clusters and labels noise.

# Dimensionality Reduction

## PCA
Linear projection maximizing explained variance.

## t-SNE and UMAP (High-Level)
Non-linear methods for visualization and neighborhood preservation; useful exploratory tools, not always stable for downstream numeric decisions.

# Distance and Similarity

Choice of metric (Euclidean, cosine, Manhattan) changes clustering behavior. Standardization usually required before distance-based methods.

# Common Pitfalls

- Forcing k-means on non-spherical data.
- Choosing `k` only by visual preference.
- Misusing t-SNE map distances as true global geometry.

# Business Case Studies & Exceptions

## Case 1: Customer Segmentation
Retail team clustered purchase behavior to tailor campaigns. Segment quality degraded when seasonal behavior changed.

Mitigation:
- Refit clusters periodically.
- Track silhouette and segment drift metrics.

## Case 2: Anomaly Detection via Clustering Distance
Using distance-to-centroid flagged anomalies, but scaling changes caused false alarms.

Mitigation:
- Feature scaling pipeline lock.
- Segment-aware thresholds and human review loop.

# Interview Questions & Answers

1. **Q: Difference between clustering and classification?**  
   **A:** Clustering discovers groups without labels; classification predicts predefined labels.

2. **Q: How does k-means work?**  
   **A:** Alternate assignment to nearest centroid and centroid recomputation until convergence.

3. **Q: How choose k?**  
   **A:** Use elbow/silhouette/domain constraints and stability checks.

4. **Q: When use DBSCAN?**  
   **A:** When clusters are arbitrary-shaped and noise detection matters.

5. **Q: Why standardize features before clustering?**  
   **A:** Prevent high-scale features from dominating distance calculations.

6. **Q: PCA purpose in ML workflow?**  
   **A:** Compress features, remove redundancy, and aid visualization.

7. **Q: Limitation of t-SNE?**  
   **A:** Great for visualization but poor for preserving global distances/cluster sizes.

8. **Q: Silhouette score interpretation?**  
   **A:** Higher means better separation/cohesion, but not sole truth metric.

9. **Q: Unsupervised output validation challenge?**  
   **A:** No labels, so rely on internal metrics and business usefulness tests.

10. **Q: Business risk in unsupervised segmentation?**  
    **A:** Spurious clusters can drive bad targeting or pricing decisions.
