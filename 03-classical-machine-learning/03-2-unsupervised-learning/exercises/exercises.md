# Exercises: 3.2 Unsupervised Learning

## Exercise 1: KMeans + Silhouette

Generate synthetic clusters with `make_blobs` and run KMeans for `k=2..6`.

Compute silhouette score for each `k`.

Expected outcome:
- you can pick a reasonable `k` and explain why silhouette helps.

## Exercise 2: PCA Visualization

On the same dataset:

- apply PCA to 2D,
- plot the 2D points colored by KMeans cluster id.

Expected outcome:
- you can explain what PCA does and what it does not guarantee.

## Exercise 3: DBSCAN Noise Points

Run DBSCAN with a few `eps` values and report:
- number of clusters,
- number of noise points.

Expected outcome:
- you can explain what “noise” means operationally.

## Exercise 4: Anomaly Detection (IsolationForest)

Create a dataset with outliers and run IsolationForest.

Expected outcome:
- you can show top 10 anomalies and explain the risk of false positives.

## Exercise 5: Clustering Failure Modes Note

Write a short note (6–10 lines):
- when clustering is useful,
- when it is misleading,
- one evaluation strategy when you have no labels.

