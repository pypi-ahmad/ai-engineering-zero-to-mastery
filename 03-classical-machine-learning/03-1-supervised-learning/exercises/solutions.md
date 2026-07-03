# Solutions: 3.1 Supervised Learning

## Exercise 1: Baseline Classifier (Breast Cancer)

```python
from sklearn.datasets import load_breast_cancer\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import accuracy_score, roc_auc_score\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\n\nbc = load_breast_cancer(as_frame=True)\nX = bc.data\ny = bc.target\n\nX_train, X_test, y_train, y_test = train_test_split(\n    X, y, test_size=0.2, random_state=42, stratify=y\n)\n\nscaler = StandardScaler()\nX_train_s = scaler.fit_transform(X_train)\nX_test_s = scaler.transform(X_test)\n\nclf = LogisticRegression(max_iter=4000)\nclf.fit(X_train_s, y_train)\n\nproba = clf.predict_proba(X_test_s)[:, 1]\npred = (proba >= 0.5).astype(int)\n\nprint(\"acc\", accuracy_score(y_test, pred))\nprint(\"auc\", roc_auc_score(y_test, proba))\n```

## Exercise 2: Model Comparison (Simple)

```python
from sklearn.ensemble import RandomForestClassifier\nfrom sklearn.metrics import precision_recall_fscore_support\n\nrf = RandomForestClassifier(n_estimators=300, random_state=42)\nrf.fit(X_train, y_train)\nrf_proba = rf.predict_proba(X_test)[:, 1]\nrf_pred = (rf_proba >= 0.5).astype(int)\n\np, r, f1, _ = precision_recall_fscore_support(y_test, rf_pred, average=\"binary\", zero_division=0)\nprint(\"rf acc\", accuracy_score(y_test, rf_pred))\nprint(\"rf p/r/f1\", p, r, f1)\n```

## Exercise 3: Pipeline (No Leakage)

```python
from sklearn.pipeline import Pipeline\n\npipe = Pipeline(\n    [\n        (\"scaler\", StandardScaler()),\n        (\"clf\", LogisticRegression(max_iter=4000)),\n    ]\n)\npipe.fit(X_train, y_train)\nproba = pipe.predict_proba(X_test)[:, 1]\nprint(\"auc\", roc_auc_score(y_test, proba))\n```

## Exercise 4: Missing Values Handling

```python
import numpy as np\nfrom sklearn.impute import SimpleImputer\n\nrng = np.random.default_rng(42)\nX_miss = X.copy()\nmask = rng.random(size=X_miss.shape) < 0.05\nX_miss = X_miss.mask(mask)\n\nX_train, X_test, y_train, y_test = train_test_split(\n    X_miss, y, test_size=0.2, random_state=42, stratify=y\n)\n\npipe = Pipeline(\n    [\n        (\"imputer\", SimpleImputer(strategy=\"median\")),\n        (\"scaler\", StandardScaler()),\n        (\"clf\", LogisticRegression(max_iter=4000)),\n    ]\n)\npipe.fit(X_train, y_train)\nproba = pipe.predict_proba(X_test)[:, 1]\nprint(\"auc\", roc_auc_score(y_test, proba))\n```

## Exercise 5: Feature Importance (Permutation)

```python
from sklearn.inspection import permutation_importance\n\nres = permutation_importance(pipe, X_test, y_test, n_repeats=10, random_state=42)\norder = res.importances_mean.argsort()[::-1]\n\nnames = list(X.columns)\nfor i in order[:3]:\n    print(names[i], float(res.importances_mean[i]))\n```

