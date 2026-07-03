# Solutions: 2.4 Applied Stats for ML

## Exercise 1: Split Discipline (No Leakage)

```python
from sklearn.datasets import load_iris\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import accuracy_score\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\n\niris = load_iris(as_frame=True)\nX = iris.data\ny = iris.target\n\nX_train, X_test, y_train, y_test = train_test_split(\n    X, y, test_size=0.2, random_state=42, stratify=y\n)\n\nscaler = StandardScaler()\nX_train_s = scaler.fit_transform(X_train)\nX_test_s = scaler.transform(X_test)\n\nclf = LogisticRegression(max_iter=2000)\nclf.fit(X_train_s, y_train)\n\npred = clf.predict(X_test_s)\nprint(accuracy_score(y_test, pred))\n```

## Exercise 2: Accuracy vs F1 on Imbalanced Data

```python
from sklearn.datasets import make_classification\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score\nfrom sklearn.model_selection import train_test_split\n\nX, y = make_classification(\n    n_samples=5000,\n    n_features=20,\n    n_informative=5,\n    n_redundant=2,\n    weights=[0.95, 0.05],\n    random_state=42,\n)\n\nX_train, X_test, y_train, y_test = train_test_split(\n    X, y, test_size=0.2, random_state=42, stratify=y\n)\n\nclf = LogisticRegression(max_iter=2000)\nclf.fit(X_train, y_train)\n\npred = clf.predict(X_test)\nprint(\"acc\", accuracy_score(y_test, pred))\nprint(\"prec\", precision_score(y_test, pred, zero_division=0))\nprint(\"rec\", recall_score(y_test, pred, zero_division=0))\nprint(\"f1\", f1_score(y_test, pred, zero_division=0))\n```

## Exercise 3: Cross-Validation Comparison

```python
from sklearn.datasets import load_breast_cancer\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.model_selection import cross_validate\n\nX, y = load_breast_cancer(return_X_y=True)\n\nmodels = {\n    \"log_reg\": LogisticRegression(max_iter=2000),\n    \"rf\": RandomForestClassifier(n_estimators=300, random_state=42),\n}\n\nfor name, m in models.items():\n    res = cross_validate(m, X, y, cv=5, scoring=\"accuracy\")\n    print(name, res[\"test_score\"].mean(), res[\"test_score\"].std())\n```

## Exercise 4: Confidence Interval for Mean (Bootstrap)

```python
import numpy as np\n\nrng = np.random.default_rng(42)\n\nx = rng.normal(loc=10.0, scale=2.0, size=200)\n\nB = 5000\nmeans = []\nfor _ in range(B):\n    sample = rng.choice(x, size=len(x), replace=True)\n    means.append(sample.mean())\n\nlo, hi = np.percentile(means, [2.5, 97.5])\nprint((float(lo), float(hi)))\n```

## Exercise 5: Threshold Tradeoff Note

Key points:

- Increasing threshold typically increases precision and decreases recall.
- The “best” threshold depends on the relative cost of false positives vs false negatives (risk, money, safety).

