# Solutions: 3.2 Unsupervised Learning

## Exercise 1: KMeans + Silhouette

```python
from sklearn.cluster import KMeans\nfrom sklearn.datasets import make_blobs\nfrom sklearn.metrics import silhouette_score\n\nX, _ = make_blobs(n_samples=1200, centers=4, cluster_std=1.2, random_state=42)\n\nfor k in range(2, 7):\n    km = KMeans(n_clusters=k, n_init=10, random_state=42)\n    labels = km.fit_predict(X)\n    print(k, silhouette_score(X, labels))\n```

## Exercise 2: PCA Visualization

```python
import matplotlib.pyplot as plt\nfrom sklearn.decomposition import PCA\n\nkm = KMeans(n_clusters=4, n_init=10, random_state=42)\nlabels = km.fit_predict(X)\n\nX2 = PCA(n_components=2, random_state=42).fit_transform(X)\nplt.scatter(X2[:, 0], X2[:, 1], c=labels, s=10)\nplt.title(\"PCA(2D) colored by KMeans cluster\")\nplt.show()\n```

## Exercise 3: DBSCAN Noise Points

```python
from sklearn.cluster import DBSCAN\n\nfor eps in [0.3, 0.5, 0.8, 1.2]:\n    db = DBSCAN(eps=eps, min_samples=10)\n    labels = db.fit_predict(X)\n    n_noise = int((labels == -1).sum())\n    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)\n    print(eps, \"clusters\", n_clusters, \"noise\", n_noise)\n```

## Exercise 4: Anomaly Detection (IsolationForest)

```python
import numpy as np\nfrom sklearn.ensemble import IsolationForest\n\nrng = np.random.default_rng(42)\nX_in = rng.normal(size=(1000, 2))\nX_out = rng.normal(loc=8.0, scale=0.5, size=(30, 2))\nX_all = np.vstack([X_in, X_out])\n\niso = IsolationForest(contamination=0.03, random_state=42)\nscore = iso.fit_predict(X_all)  # -1 is outlier\noutliers = np.where(score == -1)[0]\nprint(\"n outliers:\", len(outliers))\nprint(\"example indices:\", outliers[:10])\n```

## Exercise 5: Clustering Failure Modes Note

Reasonable points:

- Useful: segmentation, exploration, retrieval indexing, anomaly triage.
- Misleading: non-spherical clusters, different density, high dimensional distance issues, scaling problems.
- No-label evaluation: stability under resampling, silhouette-like metrics, human-in-the-loop review, downstream task utility.

