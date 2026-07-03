# Solutions: 3.3 Model Evaluation & Selection

## Exercise 1: CV vs Single Split

```python
from sklearn.datasets import load_breast_cancer\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import accuracy_score\nfrom sklearn.model_selection import cross_val_score, train_test_split\n\nX, y = load_breast_cancer(return_X_y=True)\n\nX_train, X_test, y_train, y_test = train_test_split(\n    X, y, test_size=0.2, random_state=42, stratify=y\n)\n\nm = LogisticRegression(max_iter=4000)\nm.fit(X_train, y_train)\nprint(\"split acc\", accuracy_score(y_test, m.predict(X_test)))\n\nscores = cross_val_score(LogisticRegression(max_iter=4000), X, y, cv=5, scoring=\"accuracy\")\nprint(\"cv mean\", scores.mean(), \"std\", scores.std())\n```

## Exercise 2: Leakage-Safe Scaling in CV

```python
from sklearn.pipeline import Pipeline\nfrom sklearn.preprocessing import StandardScaler\n\n# Wrong pattern: scaler sees the full dataset (leakage)\nX_scaled = StandardScaler().fit_transform(X)\nwrong = cross_val_score(LogisticRegression(max_iter=4000), X_scaled, y, cv=5)\n\n# Correct pattern: scaler fit happens inside each CV fold\npipe = Pipeline([(\"scaler\", StandardScaler()), (\"clf\", LogisticRegression(max_iter=4000))])\nright = cross_val_score(pipe, X, y, cv=5)\n\nprint(wrong.mean(), right.mean())\n```

## Exercise 3: Simple Grid Search

```python
from sklearn.ensemble import RandomForestClassifier\nfrom sklearn.model_selection import GridSearchCV\n\nparam_grid = {\n    \"n_estimators\": [100, 300],\n    \"max_depth\": [None, 3, 6],\n}\n\nsearch = GridSearchCV(\n    RandomForestClassifier(random_state=42),\n    param_grid=param_grid,\n    cv=5,\n    scoring=\"accuracy\",\n    n_jobs=-1,\n)\nsearch.fit(X, y)\nprint(search.best_params_)\nprint(search.best_score_)\n```

## Exercise 4: Metric Choice (Imbalanced)

```python
from sklearn.datasets import make_classification\nfrom sklearn.metrics import accuracy_score, f1_score, roc_auc_score\n\nX2, y2 = make_classification(\n    n_samples=6000,\n    n_features=20,\n    n_informative=6,\n    n_redundant=2,\n    weights=[0.97, 0.03],\n    random_state=42,\n)\n\nX_train, X_test, y_train, y_test = train_test_split(\n    X2, y2, test_size=0.2, random_state=42, stratify=y2\n)\n\nm = LogisticRegression(max_iter=4000)\nm.fit(X_train, y_train)\nproba = m.predict_proba(X_test)[:, 1]\npred = (proba >= 0.5).astype(int)\n\nprint(\"acc\", accuracy_score(y_test, pred))\nprint(\"f1\", f1_score(y_test, pred, zero_division=0))\nprint(\"auc\", roc_auc_score(y_test, proba))\n```

## Exercise 5: Model Selection Decision Note

Example structure:

- Baseline: logistic regression, split AUC=..., CV mean=...
- Tried: random forest grid search, improved CV by ...
- Ship: model X because it meets metric + complexity/cost constraints.
- Monitor: data drift, recall on positives, latency/cost, calibration.

