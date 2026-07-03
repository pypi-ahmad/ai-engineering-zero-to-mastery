# AI Engineering Zero to Mastery Handbook

This handbook consolidates the complete curriculum into a single reference guide. It synthesizes theory from each lesson and embeds **real output excerpts** pulled from executed notebooks in this repository.

## How to Use This Handbook

1. Read each chapter in order to build foundations before advanced engineering and production topics.
2. Use the linked lesson and sub-lesson folders for full notebook walkthroughs, extended exercises, and implementation details.
3. Re-run the notebooks locally when you want to modify experiments, model choices, or deployment settings.
4. Treat Lesson 15 as your end-to-end integration capstone and portfolio anchor.

## Handbook Structure

This handbook follows a consistent chapter pattern inspired by documentation best practices (Diátaxis, GitHub Docs, and technical-writing style guides):
- Objectives first
- Theory synthesis second
- Practical code/output excerpts third
- Case-study and interview-ready framing throughout

## Table of Contents

- [1. Lesson 1: Foundations of Computing and Programming](#lesson-1-foundations-of-computing-and-programming)
- [2. Lesson 2: Mathematics for AI](#lesson-2-mathematics-for-ai)
- [3. Lesson 3: Classical Machine Learning](#lesson-3-classical-machine-learning)
- [4. Lesson 4: Deep Learning Fundamentals](#lesson-4-deep-learning-fundamentals)
- [5. Lesson 5: Generative Models & LLMs](#lesson-5-generative-models-llms)
- [6. Lesson 6: MLOps & LLMOps: Production AI Systems](#lesson-6-mlops-llmops-production-ai-systems)
- [7. Lesson 7: Agentic AI & Applied AI Systems Design](#lesson-7-agentic-ai-applied-ai-systems-design)
- [8. Lesson 8: Responsible AI, Ethics, Policy & Career Readiness](#lesson-8-responsible-ai-ethics-policy-career-readiness)
- [9. Lesson 9: Advanced AI Specializations (RL, CV, NLP, Domain AI)](#lesson-9-advanced-ai-specializations-rl-cv-nlp-domain-ai)
- [10. Lesson 10: Robotics, Edge AI & TinyML](#lesson-10-robotics-edge-ai-tinyml)
- [11. Lesson 11: AI Product Management, Entrepreneurship & Research Methods](#lesson-11-ai-product-management-entrepreneurship-research-methods)
- [12. Lesson 12: MLOps & LLMOps: Production AI & Operations](#lesson-12-mlops-llmops-production-ai-operations)
- [13. Lesson 13: AI Safety, Security & Trustworthy AI](#lesson-13-ai-safety-security-trustworthy-ai)
- [14. Lesson 14: Frontier & Emerging Directions in AI](#lesson-14-frontier-emerging-directions-in-ai)
- [15. Lesson 15: AI Engineering Capstone & Professional Practice](#lesson-15-ai-engineering-capstone-professional-practice)

## Lesson 1: Foundations of Computing and Programming

### Chapter Objectives
- Understand the key concepts and where they fit in production AI engineering.
- Apply one practical pattern from this lesson in code or system design.
- Connect this lesson to your capstone or portfolio narrative.

### How to Work Through This Chapter
1. Read each sub-lesson theory section in order.
2. Run the representative notebook examples and inspect outputs.
3. Capture one reusable artifact (template/checklist/snippet) for future projects.


### What You Cover in This Lesson
- **1.1 Programming Basics**
- **1.2 Data Structures & Algorithms**
- **1.3 Software Engineering Practices**

### 1.1 Programming Basics

**Core concepts:** Variables and Types; Control Flow; Functions and Reuse; Modules and Imports; Error Handling; Input/Output

Programming basics are the reliability layer under every AI system. Models can be state-of-the-art and still fail in production because of weak input checks, hidden notebook state, file-path bugs, or unhandled runtime exceptions.

In this chapter, "programming basics" means building deterministic, testable, reusable logic that behaves well under real-world data conditions.

Theory source: [`01-foundations-of-computing-and-programming/01-1-programming-basics/theory/01-1-programming-basics.md`](01-foundations-of-computing-and-programming/01-1-programming-basics/theory/01-1-programming-basics.md)

**Representative notebook:** [`01-foundations-of-computing-and-programming/01-1-programming-basics/notebooks/01-1-programming-basics.ipynb`](01-foundations-of-computing-and-programming/01-1-programming-basics/notebooks/01-1-programming-basics.ipynb)

```python
@dataclass
class BatchQualityReport:
    total_rows: int
    valid_rows: int
    invalid_rows: int

    @property
    def invalid_ratio(self) -> float:
        if self.total_rows == 0:
            return 0.0
        return self.invalid_rows / self.total_rows


def quality_gate(values: Iterable[float], min_value: float = 0.0) -> BatchQualityReport:
    values = list(values)
    valid = [v for v in values if v >= min_value]
...
```

```text
BatchQualityReport(total_rows=5, valid_rows=4, invalid_rows=1)
invalid_ratio: 0.2
```

### 1.2 Data Structures & Algorithms

**Core concepts:** Arrays & Lists; Tuples; Sets; Hash Maps (Dictionaries); Stacks & Queues; Trees & Graphs (High-Level)

Data structures and algorithms are performance architecture. In AI systems, latency and cost often depend more on data movement and lookup patterns than on model inference itself.

Formal objective: Given a computational problem, choose a representation and procedure that optimize time, space, and operational reliability for expected workloads.

Theory source: [`01-foundations-of-computing-and-programming/01-2-data-structures-and-algorithms/theory/01-2-data-structures-and-algorithms.md`](01-foundations-of-computing-and-programming/01-2-data-structures-and-algorithms/theory/01-2-data-structures-and-algorithms.md)

**Representative notebook:** [`01-foundations-of-computing-and-programming/01-2-data-structures-and-algorithms/notebooks/01-2-data-structures-and-algorithms.ipynb`](01-foundations-of-computing-and-programming/01-2-data-structures-and-algorithms/notebooks/01-2-data-structures-and-algorithms.ipynb)

```python
numbers = list(range(8))
immutable_pair = ("user_12", 0.83)
seen = set(["evt_1", "evt_2", "evt_2"])
counts = {"click": 10, "purchase": 2}

stack = []
queue = deque()

for x in [1, 2, 3]:
    stack.append(x)
    queue.append(x)

print("list slice:", numbers[2:6])
print("tuple:", immutable_pair)
print("set:", seen)
print("dict:", counts)
...
```

```text
list slice: [2, 3, 4, 5]
tuple: ('user_12', 0.83)
set: {'evt_1', 'evt_2'}
dict: {'click': 10, 'purchase': 2}
stack LIFO: [3, 2, 1]
queue FIFO: [1, 2, 3]
```

### 1.3 Software Engineering Practices

**Core concepts:** Experiment Branch Strategy; PR for Pipeline Contract Changes; Release Hotfix Under Incident; Case 1: Secret Leaked in Commit; Case 2: Broken Merge Before Release; Case 3: Long-Lived Branch Drift

Version control is the source of truth for software evolution. In AI engineering, reproducibility, auditability, and rollback are critical because data pipelines and models change frequently.

This chapter covers Git concepts, branching workflows, pull-request quality, and CI/CD integration for production-safe delivery.

Theory source: [`01-foundations-of-computing-and-programming/01-3-software-engineering-practices/theory/01-3-1-version-control-git-branching-prs.md`](01-foundations-of-computing-and-programming/01-3-software-engineering-practices/theory/01-3-1-version-control-git-branching-prs.md)

**Representative notebook:** [`01-foundations-of-computing-and-programming/01-3-software-engineering-practices/notebooks/01-3-1-version-control-git-branching-prs.ipynb`](01-foundations-of-computing-and-programming/01-3-software-engineering-practices/notebooks/01-3-1-version-control-git-branching-prs.ipynb)

```python
from dataclasses import dataclass
from typing import List


@dataclass
class FileChange:
    path: str
    lines_changed: int


def risk_score(changes: List[FileChange]) -> int:
    """Very small heuristic to prioritize PR review depth."""
    score = 0
    for ch in changes:
        if ch.path.startswith('infra/') or ch.path.startswith('serve/'):
            score += 4
...
```

```text
{'risk_score': 11, 'review_tier': 'high'}
```


### Bridge to Next Lesson
You now have the core concepts and practical patterns from this lesson. Next, you will build on them in the following lesson with deeper abstraction, larger system scope, and stronger production tradeoff analysis.

[Back to Table of Contents](#table-of-contents)

## Lesson 2: Mathematics for AI

### Chapter Objectives
- Understand the key concepts and where they fit in production AI engineering.
- Apply one practical pattern from this lesson in code or system design.
- Connect this lesson to your capstone or portfolio narrative.

### How to Work Through This Chapter
1. Read each sub-lesson theory section in order.
2. Run the representative notebook examples and inspect outputs.
3. Capture one reusable artifact (template/checklist/snippet) for future projects.


### What You Cover in This Lesson
- **2.1 Linear Algebra**
- **2.2 Calculus & Optimization**
- **2.3 Probability & Statistics**
- **2.4 Applied Stats for ML**

### 2.1 Linear Algebra

**Core concepts:** Scalars, Vectors, Matrices, Tensors; Matrix Operations; Dot Product, Norm, Cosine Similarity; Eigenvalues, Eigenvectors, SVD (Intuition); Linear Regression in Matrix Form; Embeddings and Similarity Search

Linear algebra is the language of ML. Feature vectors, embedding spaces, neural network layers, and many optimization routines are matrix operations.

Core idea: Represent data and transformations in vector spaces so that learning becomes a problem of geometric and algebraic optimization.

Theory source: [`02-mathematics-for-ai/02-1-linear-algebra/theory/02-1-linear-algebra-for-ml-and-ai.md`](02-mathematics-for-ai/02-1-linear-algebra/theory/02-1-linear-algebra-for-ml-and-ai.md)

**Representative notebook:** [`02-mathematics-for-ai/02-1-linear-algebra/notebooks/02-1-linear-algebra-for-ml-and-ai.ipynb`](02-mathematics-for-ai/02-1-linear-algebra/notebooks/02-1-linear-algebra-for-ml-and-ai.ipynb)

```python
a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 5.0, 6.0])
A = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])

print("a shape:", a.shape)
print("A shape:", A.shape)
print("dot(a,b):", float(a @ b))
print("A^T A:\n", A.T @ A)
```

```text
a shape: (3,)
A shape: (3, 2)
dot(a,b): 32.0
A^T A:
 [[35. 44.]
 [44. 56.]]
```

### 2.2 Calculus & Optimization

**Core concepts:** Derivative; Partial Derivatives and Gradient; Chain Rule; Gradient Descent; Learning Rate Tradeoff; Convex vs Non-Convex

Optimization is the engine of learning. Calculus provides the local geometry (slopes and curvature) that algorithms use to update parameters and reduce loss.

In ML, training is typically framed as: $$ \theta^* = \arg\min_{\theta} L(\theta) $$

Theory source: [`02-mathematics-for-ai/02-2-calculus-and-optimization/theory/02-2-calculus-and-optimization.md`](02-mathematics-for-ai/02-2-calculus-and-optimization/theory/02-2-calculus-and-optimization.md)

**Representative notebook:** [`02-mathematics-for-ai/02-2-calculus-and-optimization/notebooks/02-2-calculus-and-optimization.ipynb`](02-mathematics-for-ai/02-2-calculus-and-optimization/notebooks/02-2-calculus-and-optimization.ipynb)

```python
def f(x: np.ndarray | float):
    return x**2 + 0.5 * x


def grad_f(x: np.ndarray | float):
    return 2 * x + 0.5


def numerical_grad(func, x: float, eps: float = 1e-6) -> float:
    return float((func(x + eps) - func(x - eps)) / (2 * eps))


for p in [-2.0, 0.0, 3.0]:
    print(p, "analytic:", grad_f(p), "numeric:", round(numerical_grad(f, p), 6))
```

```text
-2.0 analytic: -3.5 numeric: -3.5
0.0 analytic: 0.5 numeric: 0.5
3.0 analytic: 6.5 numeric: 6.5
```

### 2.3 Probability & Statistics

**Core concepts:** Random Variables and Events; Marginal, Joint, Conditional Probability; Independence vs Dependence; Summary Statistics; Common Distributions (High-Level); Case 1: Risk-Based Review Queue

Probability models uncertainty; statistics summarizes and infers structure from data. ML systems rely on both to produce calibrated decisions under incomplete information.

This chapter uses Titanic-style analysis to connect formal concepts with practical intuition.

Theory source: [`02-mathematics-for-ai/02-3-probability-and-statistics/theory/02-3-probability-and-statistics-titanic.md`](02-mathematics-for-ai/02-3-probability-and-statistics/theory/02-3-probability-and-statistics-titanic.md)

**Representative notebook:** [`02-mathematics-for-ai/02-3-probability-and-statistics/notebooks/02-3-probability-and-statistics-titanic.ipynb`](02-mathematics-for-ai/02-3-probability-and-statistics/notebooks/02-3-probability-and-statistics-titanic.ipynb)

```python
def load_titanic_like(n: int = 800) -> pd.DataFrame:
    try:
        import seaborn as sns

        df = sns.load_dataset("titanic")
        cols = ["survived", "sex", "pclass", "age", "fare"]
        return df[cols].copy()
    except Exception:
        sex = np.random.choice(["male", "female"], size=n, p=[0.62, 0.38])
        pclass = np.random.choice([1, 2, 3], size=n, p=[0.24, 0.23, 0.53])
        age = np.clip(np.random.normal(30, 14, size=n), 1, 80)
        fare = np.clip(np.random.lognormal(mean=3.1, sigma=0.7, size=n), 5, 300)

        base = 0.35 + 0.25 * (sex == "female") + 0.12 * (pclass == 1) - 0.10 * (pclass == 3)
        base -= 0.06 * (age > 55)
        prob = np.clip(base, 0.03, 0.97)
...
```

```text
shape: (891, 5)
```

### 2.4 Applied Stats for ML

**Core concepts:** Classification; Regression; Case 1: Accuracy-Led Decision Failure; Case 2: Poor Calibration in Risk Scores; Case 3: Data Leakage via Preprocessing; Bridge to Next Lesson

Applied statistics for ML is about decision quality: selecting metrics, diagnosing error patterns, and avoiding evaluation traps.

A model is useful only when its measured performance maps to business outcomes under realistic constraints.

Theory source: [`02-mathematics-for-ai/02-4-applied-stats-for-ml/theory/02-4-applied-stats-for-ml-iris.md`](02-mathematics-for-ai/02-4-applied-stats-for-ml/theory/02-4-applied-stats-for-ml-iris.md)

**Representative notebook:** [`02-mathematics-for-ai/02-4-applied-stats-for-ml/notebooks/02-4-applied-stats-for-ml-iris.ipynb`](02-mathematics-for-ai/02-4-applied-stats-for-ml/notebooks/02-4-applied-stats-for-ml-iris.ipynb)

```python
metrics = {
    "accuracy": accuracy_score(y_test, pred),
    "precision": precision_score(y_test, pred),
    "recall": recall_score(y_test, pred),
    "f1": f1_score(y_test, pred),
    "roc_auc": roc_auc_score(y_test, proba),
}

print({k: round(v, 4) for k, v in metrics.items()})
print("confusion_matrix:\n", confusion_matrix(y_test, pred))
```

```text
{'accuracy': 0.986, 'precision': 0.9889, 'recall': 0.9889, 'f1': 0.9889, 'roc_auc': 0.9977}
confusion_matrix:
 [[52  1]
 [ 1 89]]
```


### Bridge to Next Lesson
You now have the core concepts and practical patterns from this lesson. Next, you will build on them in the following lesson with deeper abstraction, larger system scope, and stronger production tradeoff analysis.

[Back to Table of Contents](#table-of-contents)

## Lesson 3: Classical Machine Learning

### Chapter Objectives
- Understand the key concepts and where they fit in production AI engineering.
- Apply one practical pattern from this lesson in code or system design.
- Connect this lesson to your capstone or portfolio narrative.

### How to Work Through This Chapter
1. Read each sub-lesson theory section in order.
2. Run the representative notebook examples and inspect outputs.
3. Capture one reusable artifact (template/checklist/snippet) for future projects.


### What You Cover in This Lesson
- **3.1 Supervised Learning**
- **3.2 Unsupervised Learning**
- **3.3 Model Evaluation & Selection**

### 3.1 Supervised Learning

**Core concepts:** Formal Definitions; Regression; Classification; Linear Regression; Logistic Regression; k-Nearest Neighbors (k-NN)

Supervised learning fits a mapping from inputs to known targets using labeled data: $$ D = \{(x_i, y_i)\}_{i=1}^{n} $$ The objective is to learn a function $f_\theta(x)$ that generalizes to unseen samples by minimizing expected loss.

In production terms, supervised learning is a contract between historical labeled outcomes and future decision quality. The challenge is not just fitting the training set; it is preserving performance when data shifts, business rules evolve, and inference latency constraints apply. This is why model family selection should include operational characteristics (interpretability, retraining cost, stability) in addition to offline metrics.

Theory source: [`03-classical-machine-learning/03-1-supervised-learning/theory/03-1-supervised-learning.md`](03-classical-machine-learning/03-1-supervised-learning/theory/03-1-supervised-learning.md)

**Representative notebook:** [`03-classical-machine-learning/03-1-supervised-learning/notebooks/03-1-supervised-learning.ipynb`](03-classical-machine-learning/03-1-supervised-learning/notebooks/03-1-supervised-learning.ipynb)

```python
import numpy as np
import pandas as pd

from sklearn.datasets import load_breast_cancer, load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    roc_auc_score,
    mean_squared_error,
    mean_absolute_error,
    r2_score,
)
from sklearn.linear_model import LogisticRegression, LinearRegression
...
```

```text
xgboost_available: True
```

### 3.2 Unsupervised Learning

**Core concepts:** k-Means; Hierarchical Clustering; DBSCAN; PCA; t-SNE and UMAP (High-Level); Case 1: Customer Segmentation

Unsupervised learning finds structure in unlabeled data. Instead of predicting known targets, models infer patterns such as clusters, latent factors, or anomalous behavior.

Objective: $$ \min_{\{C_k\}_{k=1}^{K}} \sum_{k=1}^{K}\sum_{x_i\in C_k} \|x_i - \mu_k\|_2^2 $$

Theory source: [`03-classical-machine-learning/03-2-unsupervised-learning/theory/03-2-unsupervised-learning.md`](03-classical-machine-learning/03-2-unsupervised-learning/theory/03-2-unsupervised-learning.md)

**Representative notebook:** [`03-classical-machine-learning/03-2-unsupervised-learning/notebooks/03-2-unsupervised-learning.ipynb`](03-classical-machine-learning/03-2-unsupervised-learning/notebooks/03-2-unsupervised-learning.ipynb)

```python
iris = load_iris(as_frame=True)
X = iris.data
y_true = iris.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("shape:", X_scaled.shape)
```

```text
shape: (150, 4)
```

### 3.3 Model Evaluation & Selection

**Core concepts:** k-Fold CV; Stratified CV; Grid Search; Random Search; Bayesian Optimization (High-Level); Case 1: Fraud Detection Model Choice

Model evaluation determines whether performance is real or an artifact of leakage, overfitting, or metric mismatch. Selection determines which model is best under business constraints, not just benchmark scores.

Per scikit-learn guidance, evaluating on training data is a methodological mistake because memorization can appear as high performance but fails on unseen data.

Theory source: [`03-classical-machine-learning/03-3-model-evaluation-and-selection/theory/03-3-model-evaluation-and-selection.md`](03-classical-machine-learning/03-3-model-evaluation-and-selection/theory/03-3-model-evaluation-and-selection.md)

**Representative notebook:** [`03-classical-machine-learning/03-3-model-evaluation-and-selection/notebooks/03-3-model-evaluation-and-selection.ipynb`](03-classical-machine-learning/03-3-model-evaluation-and-selection/notebooks/03-3-model-evaluation-and-selection.ipynb)

```python
import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import (
    train_test_split,
    StratifiedKFold,
    cross_validate,
    GridSearchCV,
    RandomizedSearchCV,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, f1_score, accuracy_score, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

...
```

```text
xgboost_available: True
```


### Bridge to Next Lesson
You now have the core concepts and practical patterns from this lesson. Next, you will build on them in the following lesson with deeper abstraction, larger system scope, and stronger production tradeoff analysis.

[Back to Table of Contents](#table-of-contents)

## Lesson 4: Deep Learning Fundamentals

### Chapter Objectives
- Understand the key concepts and where they fit in production AI engineering.
- Apply one practical pattern from this lesson in code or system design.
- Connect this lesson to your capstone or portfolio narrative.

### How to Work Through This Chapter
1. Read each sub-lesson theory section in order.
2. Run the representative notebook examples and inspect outputs.
3. Capture one reusable artifact (template/checklist/snippet) for future projects.


### What You Cover in This Lesson
- **4.1 Neural Networks & Backpropagation**
- **4.2 Training Deep Neural Networks**
- **4.3 Convolutional Neural Networks & Computer Vision**
- **4.4 Sequence Models, Attention & Transformers**

### 4.1 Neural Networks & Backpropagation

**Core concepts:** Overview; From Linear Models to Neural Networks; Neurons, Layers, and Activation Functions; Forward Pass and Loss Functions; Backpropagation Intuition; Optimization Loop in Practice

Deep learning starts with a simple idea: stack nonlinear transformations so models can learn complex patterns from raw inputs. This chapter builds first-principles understanding of neural networks and backpropagation, so later modules (CNNs, transformers, LLMs) feel like extensions, not black boxes.

It works when the relationship between input and target is approximately linear (or can be linearized by feature engineering). Neural networks generalize this by composing multiple linear layers with nonlinear activations:

Theory source: [`04-deep-learning-fundamentals/04-1-neural-networks-and-backpropagation/theory/04-1-neural-networks-and-backpropagation.md`](04-deep-learning-fundamentals/04-1-neural-networks-and-backpropagation/theory/04-1-neural-networks-and-backpropagation.md)

**Representative notebook:** [`04-deep-learning-fundamentals/04-1-neural-networks-and-backpropagation/notebooks/04-1-neural-networks-and-backpropagation.ipynb`](04-deep-learning-fundamentals/04-1-neural-networks-and-backpropagation/notebooks/04-1-neural-networks-and-backpropagation.ipynb)

```python
X, y = make_moons(n_samples=1200, noise=0.25, random_state=SEED)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=SEED, stratify=y
)

log_reg = LogisticRegression(max_iter=1000, random_state=SEED)
mlp = MLPClassifier(hidden_layer_sizes=(16, 8), activation='relu', max_iter=1200, random_state=SEED)

log_reg.fit(X_train, y_train)
mlp.fit(X_train, y_train)

pred_lr = log_reg.predict(X_test)
pred_mlp = mlp.predict(X_test)

metrics = {
    'log_reg_acc': accuracy_score(y_test, pred_lr),
...
```

```text
{'log_reg_acc': 0.8766666666666667, 'log_reg_f1': 0.872852233676976, 'mlp_acc': 0.95, 'mlp_f1': 0.9498327759197325}
```

### 4.2 Training Deep Neural Networks

**Core concepts:** Overview; Optimization Landscape and Training Dynamics; Initialization and Normalization; Regularization and Generalization; Optimizers and Learning-Rate Strategy; Instrumentation and Training Diagnostics

Most deep learning failures are training failures, not architecture failures. This chapter focuses on practical training mechanics that separate unstable experiments from production-credible models.

Deep networks optimize non-convex objectives. In practice, useful minima are common, but path to them depends heavily on optimization setup.

Theory source: [`04-deep-learning-fundamentals/04-2-training-deep-neural-networks/theory/04-2-training-deep-neural-networks.md`](04-deep-learning-fundamentals/04-2-training-deep-neural-networks/theory/04-2-training-deep-neural-networks.md)

**Representative notebook:** [`04-deep-learning-fundamentals/04-2-training-deep-neural-networks/notebooks/04-2-training-deep-neural-networks.ipynb`](04-deep-learning-fundamentals/04-2-training-deep-neural-networks/notebooks/04-2-training-deep-neural-networks.ipynb)

```python
configs = [
    {'name': 'conservative', 'lr': 0.001, 'alpha': 0.0001},
    {'name': 'aggressive_lr', 'lr': 0.05, 'alpha': 0.0001},
    {'name': 'regularized', 'lr': 0.005, 'alpha': 0.01},
]

results = []
curves = {}

for cfg in configs:
    model = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        learning_rate_init=cfg['lr'],
        alpha=cfg['alpha'],
        max_iter=250,
        random_state=SEED,
...
```

```text
/home/ahmad/AI/Github/ai-engineering-zero-to-mastery/.venv/lib/python3.14/site-packages/sklearn/neural_network/_multilayer_perceptron.py:785: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (250) reached and the optimization hasn't converged yet.
  warnings.warn(
```

### 4.3 Convolutional Neural Networks & Computer Vision

**Core concepts:** Overview; CNN Building Blocks; Canonical Architecture Progression; Transfer Learning for Practical Teams; Evaluation and Error Analysis; Deployment Considerations

Computer vision became practical at scale because CNNs encode spatial inductive bias: nearby pixels interact strongly, patterns repeat across positions, and hierarchical features emerge from simple edges to complex objects.

Convolution applies learnable filters across local receptive fields. Weight sharing reduces parameters and improves translation tolerance.

Theory source: [`04-deep-learning-fundamentals/04-3-convolutional-neural-networks-and-computer-vision/theory/04-3-convolutional-neural-networks-and-computer-vision.md`](04-deep-learning-fundamentals/04-3-convolutional-neural-networks-and-computer-vision/theory/04-3-convolutional-neural-networks-and-computer-vision.md)

**Representative notebook:** [`04-deep-learning-fundamentals/04-3-convolutional-neural-networks-and-computer-vision/notebooks/04-3-convolutional-neural-networks-and-computer-vision.ipynb`](04-deep-learning-fundamentals/04-3-convolutional-neural-networks-and-computer-vision/notebooks/04-3-convolutional-neural-networks-and-computer-vision.ipynb)

```python
import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

SEED = 42
random.seed(SEED)
np.random.seed(SEED)

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=SEED, stratify=y
)
...
```

```text
train_shape: (1347, 64) test_shape: (450, 64)
```

### 4.4 Sequence Models, Attention & Transformers

**Core concepts:** Overview; Sequence Modeling Challenges; RNN and LSTM Intuition; Attention Mechanism; Transformer Fundamentals; Practical Model Family Trade-offs

Many AI tasks are sequential: language, code, logs, time series, user sessions, biological sequences. This chapter explains how sequence modeling evolved from recurrent networks to attention and transformers.

Gates control information flow and retention, improving long-range learning compared to vanilla RNNs.

Theory source: [`04-deep-learning-fundamentals/04-4-sequence-models-attention-and-transformers/theory/04-4-sequence-models-attention-and-transformers.md`](04-deep-learning-fundamentals/04-4-sequence-models-attention-and-transformers/theory/04-4-sequence-models-attention-and-transformers.md)

**Representative notebook:** [`04-deep-learning-fundamentals/04-4-sequence-models-attention-and-transformers/notebooks/04-4-sequence-models-attention-and-transformers.ipynb`](04-deep-learning-fundamentals/04-4-sequence-models-attention-and-transformers/notebooks/04-4-sequence-models-attention-and-transformers.ipynb)

```python
text = 'the model learns from context and the model predicts from context'
tokens = text.split()

bigram_counts = {}
for a, b in zip(tokens[:-1], tokens[1:]):
    bigram_counts.setdefault(a, {})
    bigram_counts[a][b] = bigram_counts[a].get(b, 0) + 1

bigram_probs = {}
for token, nxt in bigram_counts.items():
    total = sum(nxt.values())
    bigram_probs[token] = {k: v / total for k, v in nxt.items()}

print('bigram_probs for "model":', bigram_probs.get('model', {}))
```

```text
bigram_probs for "model": {'learns': 0.5, 'predicts': 0.5}
```


### Bridge to Next Lesson
You now have the core concepts and practical patterns from this lesson. Next, you will build on them in the following lesson with deeper abstraction, larger system scope, and stronger production tradeoff analysis.

[Back to Table of Contents](#table-of-contents)

## Lesson 5: Generative Models & LLMs

### Chapter Objectives
- Understand the key concepts and where they fit in production AI engineering.
- Apply one practical pattern from this lesson in code or system design.
- Connect this lesson to your capstone or portfolio narrative.

### How to Work Through This Chapter
1. Read each sub-lesson theory section in order.
2. Run the representative notebook examples and inspect outputs.
3. Capture one reusable artifact (template/checklist/snippet) for future projects.


### What You Cover in This Lesson
- **5.1 Classical Deep Generative Models**
- **5.2 Autoregressive & Diffusion Models**
- **5.3 LLM Foundations & Prompt Engineering**
- **5.4 RAG, Tools, and AI Agents**
- **5.5 LLM Post-Training & Fine-Tuning**

### 5.1 Classical Deep Generative Models

**Core concepts:** Density Models vs Implicit Models in Practice; Why This Matters for AI Engineers; Probabilistic View and ELBO; Reparameterization Trick; Strengths and Weaknesses; Intuition

Generative modeling asks a different question than classical predictive modeling. In supervised learning, we typically learn a mapping from input to label, such as $f(x) \rightarrow y$. In generative modeling, we try to learn the data-generating process itself, i.e., a model that can produce realistic samples from the same distribution as the training data.

Formally, if real data comes from an unknown distribution $p_{\text{data}}(x)$, a generative model aims to approximate either:

Theory source: [`05-generative-models-and-llms/05-1-classical-deep-generative-models/theory/05-1-classical-deep-generative-models.md`](05-generative-models-and-llms/05-1-classical-deep-generative-models/theory/05-1-classical-deep-generative-models.md)

**Representative notebook:** [`05-generative-models-and-llms/05-1-classical-deep-generative-models/notebooks/05-1-classical-deep-generative-models-vae-gan.ipynb`](05-generative-models-and-llms/05-1-classical-deep-generative-models/notebooks/05-1-classical-deep-generative-models-vae-gan.ipynb)

```python
from __future__ import annotations

import random
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Subset
from torchvision import datasets, transforms
from torchvision.utils import make_grid

SEED = 42
random.seed(SEED)
...
```

```text
device(type='cuda')
```

### 5.2 Autoregressive & Diffusion Models

**Core concepts:** Why this distinction matters; Core Intuition; Examples; Sampling One Step at a Time; Practical Strengths and Limits; Forward Process (DDPM-style)

Autoregressive and diffusion models are two dominant paradigms in modern generative AI.

Both can model highly complex distributions, but they differ in objective, sampling behavior, and deployment trade-offs.

Theory source: [`05-generative-models-and-llms/05-2-autoregressive-and-diffusion-models/theory/05-2-autoregressive-and-diffusion-models.md`](05-generative-models-and-llms/05-2-autoregressive-and-diffusion-models/theory/05-2-autoregressive-and-diffusion-models.md)

**Representative notebook:** [`05-generative-models-and-llms/05-2-autoregressive-and-diffusion-models/notebooks/05-2-autoregressive-and-diffusion-models-demo.ipynb`](05-generative-models-and-llms/05-2-autoregressive-and-diffusion-models/notebooks/05-2-autoregressive-and-diffusion-models-demo.ipynb)

```python
from __future__ import annotations

import math
import random
from collections import Counter, defaultdict
from typing import Iterable

import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.datasets import make_moons

SEED = 42
random.seed(SEED)
...
```

```text
device(type='cuda')
```

### 5.3 LLM Foundations & Prompt Engineering

**Core concepts:** Pre-training vs Fine-tuning; Capabilities; Limitations; Core Patterns; Controlling Style, Format, and Reliability; Instruction Tuning

A **Large Language Model (LLM)** is a neural sequence model, usually Transformer-based, trained on large text corpora to predict tokens and learn broad linguistic/statistical structure.

This simple objective, scaled with data/compute/model size, leads to emergent capabilities such as summarization, translation, coding assistance, and instruction following when combined with alignment methods.

Theory source: [`05-generative-models-and-llms/05-3-llm-foundations-and-prompt-engineering/theory/05-3-llm-foundations-and-prompt-engineering.md`](05-generative-models-and-llms/05-3-llm-foundations-and-prompt-engineering/theory/05-3-llm-foundations-and-prompt-engineering.md)

**Representative notebook:** [`05-generative-models-and-llms/05-3-llm-foundations-and-prompt-engineering/notebooks/05-3-llm-foundations-and-prompt-engineering-demo.ipynb`](05-generative-models-and-llms/05-3-llm-foundations-and-prompt-engineering/notebooks/05-3-llm-foundations-and-prompt-engineering-demo.ipynb)

```python
from __future__ import annotations

import os
import random

import torch

SEED = 42
random.seed(SEED)
torch.manual_seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)

device = "cuda" if torch.cuda.is_available() else "cpu"
device
```

```text
'cuda'
```

### 5.4 RAG, Tools, and AI Agents

**Core concepts:** 1) Document Processing and Chunking; 2) Embeddings and Indexing; 3) Retriever and Reranker; 4) Augmentation and Prompt Construction; 5) Generator; Retrieval -> Augmentation -> Generation Pipeline

Large language models are strong at language generation but weak at guaranteed factual grounding and freshness. **Retrieval-Augmented Generation (RAG)** addresses this by retrieving relevant external knowledge at inference time and injecting it into the model context.

Industry consensus from major cloud/enterprise references (IBM, Microsoft, Google Cloud, NVIDIA) converges on the same rationale:

Theory source: [`05-generative-models-and-llms/05-4-rag-tools-and-ai-agents/theory/05-4-rag-tools-and-ai-agents.md`](05-generative-models-and-llms/05-4-rag-tools-and-ai-agents/theory/05-4-rag-tools-and-ai-agents.md)

**Representative notebook:** [`05-generative-models-and-llms/05-4-rag-tools-and-ai-agents/notebooks/05-4-rag-tools-and-ai-agents-demo.ipynb`](05-generative-models-and-llms/05-4-rag-tools-and-ai-agents/notebooks/05-4-rag-tools-and-ai-agents-demo.ipynb)

```python
raw_docs = {
    "policy_1": (
        "The incident response policy requires acknowledging critical incidents within 15 minutes, "
        "assigning an incident commander, and publishing status updates every 30 minutes. "
        "After resolution, teams must run a post-incident review within 5 business days."
    ),
    "policy_2": (
        "Customer data retention is 24 months by default unless legal hold applies. "
        "Personally identifiable information must be masked in analytics dashboards. "
        "Access to production data requires approved role-based permissions."
    ),
    "playbook_1": (
        "For model quality regressions, first compare retrieval recall@k and grounding metrics, "
        "then inspect prompt templates and context truncation. Roll back to last stable prompt "
        "version if hallucination rate exceeds threshold."
    ),
...
```

```text
       doc_id      chunk_id                                               text
0    policy_1    policy_1_0  The incident response policy requires acknowle...
1    policy_2    policy_2_0  Customer data retention is 24 months by defaul...
2  playbook_1  playbook_1_0  For model quality regressions, first compare r...
3  playbook_2  playbook_2_0  On-call escalation matrix: Severity 1 pages im...
```

### 5.5 LLM Post-Training & Fine-Tuning

**Core concepts:** Why post-training exists; Supervised Fine-Tuning (SFT); Parameter-Efficient Fine-Tuning (PEFT); LoRA (Low-Rank Adaptation); QLoRA (Quantized LoRA); SFT dataset patterns

Post-training is the stage where a pretrained language model is adapted for a concrete product context. In practice, this means improving instruction following, output format consistency, domain language behavior, and safety style while controlling compute cost.

This chapter focuses on post-training workflows used by modern AI engineering teams: supervised fine-tuning (SFT), parameter-efficient fine-tuning (PEFT), LoRA, QLoRA, and the bridge to preference optimization methods (DPO/RLHF).

Theory source: [`05-generative-models-and-llms/05-5-llm-post-training-and-fine-tuning/theory/05-5-llm-post-training-and-fine-tuning.md`](05-generative-models-and-llms/05-5-llm-post-training-and-fine-tuning/theory/05-5-llm-post-training-and-fine-tuning.md)

**Representative notebook:** [`05-generative-models-and-llms/05-5-llm-post-training-and-fine-tuning/notebooks/05-5-llm-post-training-and-fine-tuning-peft-lora-qlora.ipynb`](05-generative-models-and-llms/05-5-llm-post-training-and-fine-tuning/notebooks/05-5-llm-post-training-and-fine-tuning-peft-lora-qlora.ipynb)

```python
from __future__ import annotations

import inspect
import random
from dataclasses import fields
from pathlib import Path

import numpy as np
import torch
from datasets import Dataset
from peft import LoraConfig
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import SFTConfig, SFTTrainer

SEED = 42
random.seed(SEED)
...
```

```text
{'torch': '2.12.1+cu130', 'device': 'cuda'}
```


### Bridge to Next Lesson
You now have the core concepts and practical patterns from this lesson. Next, you will build on them in the following lesson with deeper abstraction, larger system scope, and stronger production tradeoff analysis.

[Back to Table of Contents](#table-of-contents)

## Lesson 6: MLOps & LLMOps: Production AI Systems

### Chapter Objectives
- Understand the key concepts and where they fit in production AI engineering.
- Apply one practical pattern from this lesson in code or system design.
- Connect this lesson to your capstone or portfolio narrative.

### How to Work Through This Chapter
1. Read each sub-lesson theory section in order.
2. Run the representative notebook examples and inspect outputs.
3. Capture one reusable artifact (template/checklist/snippet) for future projects.


### What You Cover in This Lesson
- **6.1 MLOps Fundamentals & Lifecycle**
- **6.2 Data & Feature Pipelines**
- **6.3 Model Deployment & Serving**
- **6.4 Monitoring, Drift & Governance**
- **6.5 LLMOps: Operationalizing LLMs, RAG & Agents**

### 6.1 MLOps Fundamentals & Lifecycle

**Core concepts:** Why MLOps exists; MLOps vs DevOps vs DataOps; 1) Data ingestion and versioning; 2) Training and experiment tracking; 3) Model packaging and deployment; 4) Monitoring and feedback loops

MLOps (Machine Learning Operations) is the engineering discipline that makes machine learning systems reliable in production. A model that performs well in a notebook is only the start. Production systems must remain reproducible, observable, secure, and cost-effective as data, code, infrastructure, and user behavior change.

A practical definition, aligned with industry guidance from Google Cloud and Azure, is:

Theory source: [`06-mlops-and-llmops-production-ai-systems/06-1-mlops-fundamentals-and-lifecycle/theory/06-1-mlops-fundamentals-and-lifecycle.md`](06-mlops-and-llmops-production-ai-systems/06-1-mlops-fundamentals-and-lifecycle/theory/06-1-mlops-fundamentals-and-lifecycle.md)

**Representative notebook:** [`06-mlops-and-llmops-production-ai-systems/06-1-mlops-fundamentals-and-lifecycle/notebooks/06-1-mlops-fundamentals-and-lifecycle-demo.ipynb`](06-mlops-and-llmops-production-ai-systems/06-1-mlops-fundamentals-and-lifecycle/notebooks/06-1-mlops-fundamentals-and-lifecycle-demo.ipynb)

```python
raw = load_breast_cancer(as_frame=True)
df = raw.frame.copy()

snapshot_path = ARTIFACT_DIR / "data_snapshot.csv"
df.to_csv(snapshot_path, index=False)

X = df.drop(columns=["target"])
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=SEED, stratify=y
)

{"rows": len(df), "features": X.shape[1], "snapshot": str(snapshot_path)}
```

```text
{'rows': 569,
 'features': 30,
 'snapshot': 'artifacts/lesson6_1/data_snapshot.csv'}
```

### 6.2 Data & Feature Pipelines

**Core concepts:** Batch vs streaming; ETL and ELT patterns; Data validation and quality checks; Feature extraction, transformation, selection; Offline vs online features; Feature store concept

In production ML, data and features are usually the highest leverage reliability layer. Models fail less often because of architecture choice than because of broken data assumptions.

When these contracts drift apart, teams observe silent quality degradation, unstable retraining, and hard-to-debug incidents.

Theory source: [`06-mlops-and-llmops-production-ai-systems/06-2-data-and-feature-pipelines/theory/06-2-data-and-feature-pipelines.md`](06-mlops-and-llmops-production-ai-systems/06-2-data-and-feature-pipelines/theory/06-2-data-and-feature-pipelines.md)

**Representative notebook:** [`06-mlops-and-llmops-production-ai-systems/06-2-data-and-feature-pipelines/notebooks/06-2-data-and-feature-pipelines-demo.ipynb`](06-mlops-and-llmops-production-ai-systems/06-2-data-and-feature-pipelines/notebooks/06-2-data-and-feature-pipelines-demo.ipynb)

```python
n = 2000
base_date = pd.Timestamp("2026-01-01")

raw_df = pd.DataFrame(
    {
        "customer_id": np.arange(1, n + 1),
        "snapshot_date": base_date + pd.to_timedelta(rng.integers(0, 90, size=n), unit="D"),
        "tenure_days": rng.integers(1, 1200, size=n),
        "monthly_spend": np.clip(rng.normal(45, 15, size=n), 2, None),
        "support_tickets_30d": rng.poisson(1.2, size=n),
        "last_login_days_ago": rng.integers(0, 90, size=n),
        "region": rng.choice(["north", "south", "east", "west"], size=n),
    }
)

raw_df["churn_label"] = (
...
```

```text
   customer_id snapshot_date  tenure_days  monthly_spend  support_tickets_30d  \
0            1    2026-01-09         1053      29.632066                    3   
1            2    2026-03-11           75      58.620943                    3   
2            3    2026-02-28          477      26.959551                    3   
3            4    2026-02-09          550      40.704508                    1   
4            5    2026-02-08          957      36.209225                    1   

   last_login_days_ago region  churn_label  
0                   12   east            1  
1                   45  south            1  
2                   32  north            1  
3                   57  north            1  
4                   57   east            1  
```

### 6.3 Model Deployment & Serving

**Core concepts:** Online / real-time serving; Batch scoring; Streaming inference; Docker for reproducible inference; Kubernetes fundamentals for serving; GPU scheduling for ML/LLM workloads

Deploying a model means operationalizing predictions as a reliable service or job, not just exporting a `.pkl` file.

Containerization packages model + dependencies + serving runtime in an immutable artifact.

Theory source: [`06-mlops-and-llmops-production-ai-systems/06-3-model-deployment-and-serving/theory/06-3-model-deployment-and-serving.md`](06-mlops-and-llmops-production-ai-systems/06-3-model-deployment-and-serving/theory/06-3-model-deployment-and-serving.md)

**Representative notebook:** [`06-mlops-and-llmops-production-ai-systems/06-3-model-deployment-and-serving/notebooks/06-3-model-deployment-and-serving-fastapi-demo.ipynb`](06-mlops-and-llmops-production-ai-systems/06-3-model-deployment-and-serving/notebooks/06-3-model-deployment-and-serving-fastapi-demo.ipynb)

```python
iris = load_iris(as_frame=True)
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=SEED, stratify=y
)

model = RandomForestClassifier(n_estimators=200, random_state=SEED)
model.fit(X_train, y_train)

acc = accuracy_score(y_test, model.predict(X_test))

model_path = ARTIFACT_DIR / "iris_rf.joblib"
meta_path = ARTIFACT_DIR / "model_metadata.json"
joblib.dump(model, model_path)
...
```

```text
{'model_type': 'RandomForestClassifier',
 'feature_names': ['sepal length (cm)',
  'sepal width (cm)',
  'petal length (cm)',
  'petal width (cm)'],
 'class_names': ['setosa', 'versicolor', 'virginica'],
 'accuracy_test': 0.9}
```

### 6.4 Monitoring, Drift & Governance

**Core concepts:** Data drift (covariate shift); Label drift and concept drift; Prediction drift; Performance metrics over time; Managed monitoring examples; Custom monitoring stack

Deployment is not the finish line for ML systems. It is the start of operational accountability.

Production monitoring and governance exist because model behavior changes over time. Data distributions shift, user behavior evolves, adversaries adapt, and infrastructure conditions vary. Without monitoring, teams discover failures late through customer impact.

Theory source: [`06-mlops-and-llmops-production-ai-systems/06-4-monitoring-drift-and-governance/theory/06-4-monitoring-drift-and-governance.md`](06-mlops-and-llmops-production-ai-systems/06-4-monitoring-drift-and-governance/theory/06-4-monitoring-drift-and-governance.md)

**Representative notebook:** [`06-mlops-and-llmops-production-ai-systems/06-4-monitoring-drift-and-governance/notebooks/06-4-monitoring-drift-and-governance-demo.ipynb`](06-mlops-and-llmops-production-ai-systems/06-4-monitoring-drift-and-governance/notebooks/06-4-monitoring-drift-and-governance-demo.ipynb)

```python
n_ref = 5000
n_prod = 2500

ref = pd.DataFrame(
    {
        "transaction_amount": np.clip(rng.normal(70, 25, size=n_ref), 1, None),
        "num_prev_txn_24h": rng.poisson(2.2, size=n_ref),
        "device_risk_score": np.clip(rng.beta(2.2, 6.5, size=n_ref), 0, 1),
    }
)

prod = pd.DataFrame(
    {
        "transaction_amount": np.clip(rng.normal(88, 33, size=n_prod), 1, None),
        "num_prev_txn_24h": rng.poisson(3.1, size=n_prod),
        "device_risk_score": np.clip(rng.beta(3.4, 5.0, size=n_prod), 0, 1),
...
```

```text
(                         mean        std
 transaction_amount  69.520757  24.934082
 num_prev_txn_24h     2.215800   1.492674
 device_risk_score    0.254707   0.141685,
                          mean        std
 transaction_amount  86.884087  32.718431
 num_prev_txn_24h     3.132000   1.753570
 device_risk_score    0.409642   0.160600)
```

### 6.5 LLMOps: Operationalizing LLMs, RAG & Agents

**Core concepts:** Context management and token limits; Cost, latency, and throughput; Safety and policy controls; API-based vs local/self-hosted models; Orchestration patterns; RAG architecture recap

LLMOps is the operational discipline for large language model systems in production. It builds on MLOps principles but introduces new constraints:

LLMOps curricula (e.g., Duke/Coursera specialization) reflect this shift by covering cloud/local deployments, prompt patterns, RAG, and lifecycle controls as mandatory production skills.

Theory source: [`06-mlops-and-llmops-production-ai-systems/06-5-llmops-operationalizing-llms-rag-and-agents/theory/06-5-llmops-operationalizing-llms-rag-and-agents.md`](06-mlops-and-llmops-production-ai-systems/06-5-llmops-operationalizing-llms-rag-and-agents/theory/06-5-llmops-operationalizing-llms-rag-and-agents.md)

**Representative notebook:** [`06-mlops-and-llmops-production-ai-systems/06-5-llmops-operationalizing-llms-rag-and-agents/notebooks/06-5-llmops-operationalizing-llms-rag-and-agents-demo.ipynb`](06-mlops-and-llmops-production-ai-systems/06-5-llmops-operationalizing-llms-rag-and-agents/notebooks/06-5-llmops-operationalizing-llms-rag-and-agents-demo.ipynb)

```python
docs = {
    "mlops_guide": "MLOps lifecycle includes data ingestion, training, deployment, monitoring, and feedback loops.",
    "monitoring_guide": "Data drift and prediction drift monitoring are essential for maintaining model quality in production.",
    "rag_guide": "RAG combines retrieval with generation. High-quality retrieval improves grounded answers and reduces hallucinations.",
    "deployment_guide": "Blue-green and canary deployments reduce risk when releasing new model versions.",
    "llmops_guide": "LLMOps adds prompt versioning, retrieval observability, cost controls, and safety policies to MLOps.",
}

chunks = []
for doc_id, text in docs.items():
    sentences = [s.strip() for s in text.split(".") if s.strip()]
    for idx, sent in enumerate(sentences):
        chunks.append({"doc_id": doc_id, "chunk_id": f"{doc_id}_{idx}", "text": sent})

chunks_df = pd.DataFrame(chunks)
chunks_df
```

```text
             doc_id            chunk_id  \
0       mlops_guide       mlops_guide_0   
1  monitoring_guide  monitoring_guide_0   
2         rag_guide         rag_guide_0   
3         rag_guide         rag_guide_1   
4  deployment_guide  deployment_guide_0   
5      llmops_guide      llmops_guide_0   

                                                text  
0  MLOps lifecycle includes data ingestion, train...  
1  Data drift and prediction drift monitoring are...  
2             RAG combines retrieval with generation  
3  High-quality retrieval improves grounded answe...  
4  Blue-green and canary deployments reduce risk ...  
5  LLMOps adds prompt versioning, retrieval obser...  
```


### Bridge to Next Lesson
You now have the core concepts and practical patterns from this lesson. Next, you will build on them in the following lesson with deeper abstraction, larger system scope, and stronger production tradeoff analysis.

[Back to Table of Contents](#table-of-contents)

## Lesson 7: Agentic AI & Applied AI Systems Design

### Chapter Objectives
- Understand the key concepts and where they fit in production AI engineering.
- Apply one practical pattern from this lesson in code or system design.
- Connect this lesson to your capstone or portfolio narrative.

### How to Work Through This Chapter
1. Read each sub-lesson theory section in order.
2. Run the representative notebook examples and inspect outputs.
3. Capture one reusable artifact (template/checklist/snippet) for future projects.


### What You Cover in This Lesson
- **7.1 Agentic AI Foundations & Architectures**
- **7.2 Multi-Agent Workflows & Orchestration**
- **7.3 Context Engineering, Memory & Planning**
- **7.4 AI Product & System Design**
- **7.5 Capstone: End-to-End Agentic AI System**
- **7.6 MCP and Agent2Agent Interoperability**

### 7.1 Agentic AI Foundations & Architectures

**Core concepts:** Agentic AI vs LLM Chat vs Traditional ML; Classical Agent Model; Types of Agents; Single-Agent vs Multi-Agent; Chatbot vs Agent; Pattern 1: Plan-Act-Observe Loop

Agentic AI refers to AI systems that do not only generate text but also pursue goals over multiple steps by selecting actions, using tools, and adapting based on observations. A practical definition used across recent courses and industry docs is: an agentic system receives a goal, decomposes it into subproblems, executes actions in an environment, and updates behavior from feedback.

$$ \mathcal{A} = (\mathcal{O}, \mathcal{S}, \mathcal{T}, \mathcal{P}, \mathcal{U}) $$

Theory source: [`07-agentic-ai-and-applied-ai-systems-design/07-1-agentic-ai-foundations-and-architectures/theory/07-1-agentic-ai-foundations-and-architectures.md`](07-agentic-ai-and-applied-ai-systems-design/07-1-agentic-ai-foundations-and-architectures/theory/07-1-agentic-ai-foundations-and-architectures.md)

**Representative notebook:** [`07-agentic-ai-and-applied-ai-systems-design/07-1-agentic-ai-foundations-and-architectures/notebooks/07-1-agentic-ai-foundations-and-architectures-demo.ipynb`](07-agentic-ai-and-applied-ai-systems-design/07-1-agentic-ai-foundations-and-architectures/notebooks/07-1-agentic-ai-foundations-and-architectures-demo.ipynb)

```python
ACTION_MAP = {
    "classify_intent": classify_intent_tool,
    "propose_slots": propose_slots_tool,
    "escalate": escalate_tool,
    "draft_response": draft_response_tool,
    "close": close_tool,
}


def run_agent(email: Dict[str, Any], max_steps: int = 6) -> AgentState:
    state = AgentState(email=email)
    for _ in range(max_steps):
        action = decide_next_action(state)
        ACTION_MAP[action](state)
        if state.done:
            break
...
```

```text
E-100 meeting False closed
  actions: ['intent=meeting', 'slot_proposed', 'closed']
  draft: Thanks for reaching out. Available slot: Wed 16:30. Please confirm if this works for you.
E-101 issue True closed
  actions: ['intent=issue', 'escalated_to_human', 'closed']
  draft: I have escalated this to our billing specialist and marked it urgent. You will receive an update shortly.
E-102 faq False closed
  actions: ['intent=faq', 'faq_response_drafted', 'closed']
  draft: Thanks for your message. You can find API docs at /docs/api.
```

### 7.2 Multi-Agent Workflows & Orchestration

**Core concepts:** Coordinator-Worker Pattern; Peer-to-Peer Collaboration; Hierarchical Teams; Critic-Generator Pattern; Task and Dependency Modeling; Orchestration vs Choreography

Multi-agent systems partition complex tasks across specialized agents. Instead of one generalist agent doing everything, a team of agents handles decomposition, execution, critique, and synthesis.

Each task node can be assigned to an agent role. The orchestration layer enforces order, retries, and merge behavior.

Theory source: [`07-agentic-ai-and-applied-ai-systems-design/07-2-multi-agent-workflows-and-orchestration/theory/07-2-multi-agent-workflows-and-orchestration.md`](07-agentic-ai-and-applied-ai-systems-design/07-2-multi-agent-workflows-and-orchestration/theory/07-2-multi-agent-workflows-and-orchestration.md)

**Representative notebook:** [`07-agentic-ai-and-applied-ai-systems-design/07-2-multi-agent-workflows-and-orchestration/notebooks/07-2-multi-agent-workflows-and-orchestration-demo.ipynb`](07-agentic-ai-and-applied-ai-systems-design/07-2-multi-agent-workflows-and-orchestration/notebooks/07-2-multi-agent-workflows-and-orchestration-demo.ipynb)

```python
@dataclass
class OrchestrationResult:
    ticket_id: str
    intent: str
    priority: str
    response: str


def coordinator_sequential(ticket: Dict[str, str]) -> OrchestrationResult:
    triage = triage_agent(ticket)
    kb = knowledge_agent(triage["intent"])
    response = response_agent(ticket, triage, kb)
    return OrchestrationResult(
        ticket_id=ticket["ticket_id"],
        intent=triage["intent"],
        priority=triage["priority"],
...
```

```text
OrchestrationResult(ticket_id='T-200', intent='billing', priority='high', response='Ticket T-200 classified as billing. If charged twice, verify transaction id and initiate reversal workflow. Escalating to priority queue.')
OrchestrationResult(ticket_id='T-201', intent='api', priority='low', response='Ticket T-201 classified as api. API limits documented at /docs/rate-limits with tier-specific quotas.')
OrchestrationResult(ticket_id='T-202', intent='cancel', priority='medium', response='Ticket T-202 classified as cancel. Cancellation policy requires identity verification and retention offer step.')
```

### 7.3 Context Engineering, Memory & Planning

**Core concepts:** Formal Definition; Core Techniques; Context Quality Heuristics; Short-Term Memory; Long-Term Memory; Episodic vs Semantic Memory

Context is the working memory of LLM-based systems. Poor context design causes hallucinations, contradiction, and rising cost. Context engineering is the discipline of selecting, structuring, and refreshing the right information at the right time.

Where total token budget $B$ must stay below model limits while preserving relevant facts.

Theory source: [`07-agentic-ai-and-applied-ai-systems-design/07-3-context-engineering-memory-and-planning/theory/07-3-context-engineering-memory-and-planning.md`](07-agentic-ai-and-applied-ai-systems-design/07-3-context-engineering-memory-and-planning/theory/07-3-context-engineering-memory-and-planning.md)

**Representative notebook:** [`07-agentic-ai-and-applied-ai-systems-design/07-3-context-engineering-memory-and-planning/notebooks/07-3-context-engineering-memory-and-planning-demo.ipynb`](07-agentic-ai-and-applied-ai-systems-design/07-3-context-engineering-memory-and-planning/notebooks/07-3-context-engineering-memory-and-planning-demo.ipynb)

```python
vectorizer = TfidfVectorizer()
kb_matrix = vectorizer.fit_transform(DOCS)


def retrieve(query: str, top_k: int = 2) -> List[str]:
    q = vectorizer.transform([query])
    sims = cosine_similarity(q, kb_matrix).flatten()
    idx = np.argsort(-sims)[:top_k]
    return [DOCS[i] for i in idx]


retrieve("What are ACME SLA obligations and blockers?")
```

```text
['Customer ACME uses region ap-south and prefers email communication.',
 'ACME had outage incident on June 2 and requested root-cause summary format.']
```

### 7.4 AI Product & System Design

**Core concepts:** Problem Framing; ROI-Oriented Decision Gate; When AI is the Wrong Tool; Canonical AI Product Architecture; Monolith vs Microservices; Latency and Reliability Budgets

An AI model is a component. An AI product is a socio-technical system that delivers value repeatedly under constraints. Teams fail when they optimize model quality in isolation and underinvest in system design, UX, reliability, and governance.

$$ \text{Expected Value} = (\text{Benefit} \times \text{Adoption}) - (\text{Build Cost} + \text{Run Cost} + \text{Risk Cost}) $$

Theory source: [`07-agentic-ai-and-applied-ai-systems-design/07-4-ai-product-and-system-design/theory/07-4-ai-product-and-system-design.md`](07-agentic-ai-and-applied-ai-systems-design/07-4-ai-product-and-system-design/theory/07-4-ai-product-and-system-design.md)

**Representative notebook:** [`07-agentic-ai-and-applied-ai-systems-design/07-4-ai-product-and-system-design/notebooks/07-4-ai-product-and-system-design-architecture-notes.ipynb`](07-agentic-ai-and-applied-ai-systems-design/07-4-ai-product-and-system-design/notebooks/07-4-ai-product-and-system-design-architecture-notes.ipynb)

```python
@dataclass
class RequestContext:
    user_id: str
    tenant_id: str
    intent: str
    risk_level: str


class RetrievalService:
    def fetch(self, query: str) -> str:
        return f"Retrieved context for: {query}"


class AgentRuntime:
    def run(self, prompt: str, context: str) -> str:
        return f"Agent output based on [{prompt}] with [{context}]"
...
```

```text
INFO:ai_system:request=u-1 allowed=False
```

### 7.5 Capstone: End-to-End Agentic AI System

**Core concepts:** Option 1: Enterprise Document Assistant (RAG + Agents); Option 2: Agentic Customer Support Orchestrator; Option 3: AI Operations Assistant; Technical Robustness; User and Product Quality; Governance and Safety

The capstone consolidates the curriculum into an end-to-end system that can be demonstrated, evaluated, and explained in interviews. The goal is not maximum complexity; the goal is credible production-style design with measurable value.

User/App -> API -> Orchestrator -> {Retriever, Planner, Worker Agents, Tool Gateway} -> Output + Trace Store

Theory source: [`07-agentic-ai-and-applied-ai-systems-design/07-5-capstone-end-to-end-agentic-ai-system/theory/07-5-capstone-end-to-end-agentic-ai-system.md`](07-agentic-ai-and-applied-ai-systems-design/07-5-capstone-end-to-end-agentic-ai-system/theory/07-5-capstone-end-to-end-agentic-ai-system.md)

**Representative notebook:** [`07-agentic-ai-and-applied-ai-systems-design/07-5-capstone-end-to-end-agentic-ai-system/notebooks/07-5-capstone-agentic-ai-system-template.ipynb`](07-agentic-ai-and-applied-ai-systems-design/07-5-capstone-end-to-end-agentic-ai-system/notebooks/07-5-capstone-agentic-ai-system-template.ipynb)

```python
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class CapstonePlan:
    problem: str
    kpi: str
    tools: List[str]
    risks: List[str]


def score_plan(plan: CapstonePlan) -> Dict[str, int]:
    return {
        'clarity': 2 if len(plan.problem) > 30 else 1,
        'measurability': 2 if '%' in plan.kpi or 'rate' in plan.kpi.lower() else 1,
...
```

```text
{'clarity': 2, 'measurability': 2, 'operational_risk': 1, 'tooling_coverage': 2}
```

### 7.6 MCP and Agent2Agent Interoperability

**Core concepts:** What MCP standardizes; MCP architecture; MCP operation flow; MCP safety implications; What A2A standardizes; A2A collaboration model

As agentic AI systems grow, interoperability becomes a first-class engineering problem. Teams increasingly need:

MCP standardizes how an AI host/client discovers and invokes capabilities exposed by servers.

Theory source: [`07-agentic-ai-and-applied-ai-systems-design/07-6-mcp-and-agent2agent-interoperability/theory/07-6-mcp-and-agent2agent-interoperability.md`](07-agentic-ai-and-applied-ai-systems-design/07-6-mcp-and-agent2agent-interoperability/theory/07-6-mcp-and-agent2agent-interoperability.md)

**Representative notebook:** [`07-agentic-ai-and-applied-ai-systems-design/07-6-mcp-and-agent2agent-interoperability/notebooks/07-6-mcp-and-a2a-protocol-demo.ipynb`](07-agentic-ai-and-applied-ai-systems-design/07-6-mcp-and-agent2agent-interoperability/notebooks/07-6-mcp-and-a2a-protocol-demo.ipynb)

```python
@dataclass
class MCPTool:
    name: str
    description: str
    func: Callable[[Dict[str, Any]], Dict[str, Any]]
    sensitive: bool = False

@dataclass
class MCPServer:
    name: str
    tools: Dict[str, MCPTool]

    def list_tools(self) -> List[Dict[str, Any]]:
        return [{'name': t.name, 'description': t.description, 'sensitive': t.sensitive} for t in self.tools.values()]

    def call_tool(self, tool_name: str, args: Dict[str, Any], approved: bool = False) -> Dict[str, Any]:
...
```

```text
[{'name': 'get_weather',
  'description': 'Fetch weather by city',
  'sensitive': False},
 {'name': 'close_ticket',
  'description': 'Close support ticket',
  'sensitive': True}]
```


### Bridge to Next Lesson
You now have the core concepts and practical patterns from this lesson. Next, you will build on them in the following lesson with deeper abstraction, larger system scope, and stronger production tradeoff analysis.

[Back to Table of Contents](#table-of-contents)

## Lesson 8: Responsible AI, Ethics, Policy & Career Readiness

### Chapter Objectives
- Understand the key concepts and where they fit in production AI engineering.
- Apply one practical pattern from this lesson in code or system design.
- Connect this lesson to your capstone or portfolio narrative.

### How to Work Through This Chapter
1. Read each sub-lesson theory section in order.
2. Run the representative notebook examples and inspect outputs.
3. Capture one reusable artifact (template/checklist/snippet) for future projects.


### What You Cover in This Lesson
- **8.1 Foundations of AI Ethics**
- **8.2 Responsible AI in Practice**
- **8.3 AI Law, Policy & Governance**
- **8.4 AI Career Roadmap, Portfolio & Interviews**

### 8.1 Foundations of AI Ethics

**Core concepts:** Consequentialism (Outcome-Based Ethics); Deontology (Duty- and Rights-Based Ethics); Virtue Ethics (Character and Practice); AI-Relevant Ethical Concepts; Bias and Discrimination; Privacy and Surveillance

AI ethics is not an optional add-on to technical work. It is the discipline of analyzing and governing how AI systems affect people, institutions, and society at scale. University syllabi in AI ethics and governance (Georgia Tech PHIL 3101, UChicago Harris PPHA 38850, Luiss Ethics for AI) consistently frame ethics as a core competency because modern AI systems influence employment, policing, finance, health, education, and political discourse.

$$ \text{AI Impact} = f(\text{Model Behavior}, \text{Data Quality}, \text{Deployment Context}, \text{Power Relations}) $$

Theory source: [`08-responsible-ai-ethics-policy-and-career-readiness/08-1-foundations-of-ai-ethics/theory/08-1-foundations-of-ai-ethics.md`](08-responsible-ai-ethics-policy-and-career-readiness/08-1-foundations-of-ai-ethics/theory/08-1-foundations-of-ai-ethics.md)

**Representative notebook:** [`08-responsible-ai-ethics-policy-and-career-readiness/08-1-foundations-of-ai-ethics/notebooks/08-1-foundations-of-ai-ethics-case-study-notebook.ipynb`](08-responsible-ai-ethics-policy-and-career-readiness/08-1-foundations-of-ai-ethics/notebooks/08-1-foundations-of-ai-ethics-case-study-notebook.ipynb)

```python
df = pd.DataFrame(
    {
        "group": ["A", "A", "A", "B", "B", "B", "B"],
        "approved": [1, 0, 1, 1, 0, 0, 0],
    }
)

acceptance = df.groupby("group")["approved"].mean().rename("acceptance_rate")
acceptance
```

```text
group
A    0.666667
B    0.250000
Name: acceptance_rate, dtype: float64
```

### 8.2 Responsible AI in Practice

**Core concepts:** Data-Level Practices; Model-Level Practices; System-Level Practices; Risk Assessment Template; Pre-Launch Responsible AI Checklist; Post-Launch Monitoring Checklist

Responsible AI in practice means converting values (fairness, privacy, accountability, safety) into concrete engineering controls across the full lifecycle. Principles alone do not prevent harm; operational mechanisms do.

$$ \text{RAI Maturity} = f(\text{Data Controls}, \text{Model Controls}, \text{System Controls}, \text{Org Controls}) $$

Theory source: [`08-responsible-ai-ethics-policy-and-career-readiness/08-2-responsible-ai-in-practice/theory/08-2-responsible-ai-in-practice.md`](08-responsible-ai-ethics-policy-and-career-readiness/08-2-responsible-ai-in-practice/theory/08-2-responsible-ai-in-practice.md)

**Representative notebook:** [`08-responsible-ai-ethics-policy-and-career-readiness/08-2-responsible-ai-in-practice/notebooks/08-2-responsible-ai-in-practice-checklists-and-tools.ipynb`](08-responsible-ai-ethics-policy-and-career-readiness/08-2-responsible-ai-in-practice/notebooks/08-2-responsible-ai-in-practice-checklists-and-tools.ipynb)

```python
toy = pd.DataFrame(
    {
        "group": ["A","A","A","A","B","B","B","B"],
        "y_true": [1,0,1,0,1,1,0,0],
        "y_pred": [1,0,0,0,1,0,0,0],
    }
)

group_fairness_report(toy, "group", "y_true", "y_pred")
```

```text
  group  n  approval_rate  accuracy  false_positive_rate  false_negative_rate  \
0     A  4           0.25      0.75                  0.0                 0.25   
1     B  4           0.25      0.75                  0.0                 0.25   

   selection_rate_ratio_vs_best_group  
0                                 1.0  
1                                 1.0  
```

### 8.3 AI Law, Policy & Governance

**Core concepts:** EU AI Act (Risk-Based Approach); Data Protection Regimes; Sectoral Regulations; Accountability; Transparency and Explainability; Audits and Impact Assessments

AI law and policy now directly shape engineering decisions. Product teams can no longer treat legal compliance as an end-stage review. Requirements for documentation, risk management, transparency, and post-market monitoring increasingly need to be built into design and delivery workflows from day one.

The EU AI Act (Regulation (EU) 2024/1689) applies a risk-based model. At a high level, categories include:

Theory source: [`08-responsible-ai-ethics-policy-and-career-readiness/08-3-ai-law-policy-and-governance/theory/08-3-ai-law-policy-and-governance.md`](08-responsible-ai-ethics-policy-and-career-readiness/08-3-ai-law-policy-and-governance/theory/08-3-ai-law-policy-and-governance.md)

**Representative notebook:** [`08-responsible-ai-ethics-policy-and-career-readiness/08-3-ai-law-policy-and-governance/notebooks/08-3-ai-law-policy-and-governance-notes.ipynb`](08-responsible-ai-ethics-policy-and-career-readiness/08-3-ai-law-policy-and-governance/notebooks/08-3-ai-law-policy-and-governance-notes.ipynb)

```python
from __future__ import annotations

REQUIRED_METADATA = {
    "model_name",
    "version",
    "intended_use",
    "risk_tier",
    "data_lineage",
    "owner",
    "last_review_date",
}


def governance_gate(metadata: dict) -> tuple[bool, list[str]]:
    missing = sorted(list(REQUIRED_METADATA - set(metadata.keys())))
    if missing:
...
```

```text
(True, [])
```

### 8.4 AI Career Roadmap, Portfolio & Interviews

**Core concepts:** 1) ML Engineer; 2) Data Scientist; 3) GenAI Engineer; 4) MLOps / LLMOps Engineer; 5) AI Product Manager; 6) Agentic AI Architect

A strong AI career is built through demonstrable execution, not course completion alone. Hiring teams look for evidence that you can define problems, build reliable systems, evaluate trade-offs, and communicate business impact.

A structured roadmap matters because the field is broad and fast-moving. Without a plan, learners over-index on tools and under-invest in foundations, deployment quality, and portfolio storytelling.

Theory source: [`08-responsible-ai-ethics-policy-and-career-readiness/08-4-ai-career-roadmap-portfolio-and-interviews/theory/08-4-ai-career-roadmap-portfolio-and-interviews.md`](08-responsible-ai-ethics-policy-and-career-readiness/08-4-ai-career-roadmap-portfolio-and-interviews/theory/08-4-ai-career-roadmap-portfolio-and-interviews.md)

**Representative notebook:** [`08-responsible-ai-ethics-policy-and-career-readiness/08-4-ai-career-roadmap-portfolio-and-interviews/notebooks/08-4-ai-career-roadmap-portfolio-and-interviews-planner.ipynb`](08-responsible-ai-ethics-policy-and-career-readiness/08-4-ai-career-roadmap-portfolio-and-interviews/notebooks/08-4-ai-career-roadmap-portfolio-and-interviews-planner.ipynb)

```python
@dataclass
class TrackPreference:
    role_target: str
    months: int
    weekly_hours: int
    focus_areas: List[str]


def generate_roadmap(pref: TrackPreference) -> Dict[str, object]:
    phases = [
        {"phase": "Foundations", "duration_months": 2, "outcome": "Strong coding/math + baseline ML project"},
        {"phase": "Modeling", "duration_months": 2, "outcome": "Classical ML + robust evaluation"},
        {"phase": "GenAI", "duration_months": 2, "outcome": "RAG/LLM app with eval"},
        {"phase": "Production", "duration_months": 2, "outcome": "Deployment, monitoring, governance"},
        {"phase": "Portfolio & Interviews", "duration_months": 2, "outcome": "Top projects polished + interview readiness"},
    ]
...
```

```text
{
  "target_role": "GenAI Engineer",
  "timeline_months": 10,
  "weekly_hours": 12,
  "focus_areas": [
    "RAG",
    "evaluation",
    "agentic workflows",
    "LLMOps"
  ],
  "phases": [
    {
      "phase": "Foundations",
      "duration_months": 2,
      "outcome": "Strong coding/math + baseline ML project"
    },
    {
      "phase": "Modeling",
...
```


### Bridge to Next Lesson
You now have the core concepts and practical patterns from this lesson. Next, you will build on them in the following lesson with deeper abstraction, larger system scope, and stronger production tradeoff analysis.

[Back to Table of Contents](#table-of-contents)

## Lesson 9: Advanced AI Specializations (RL, CV, NLP, Domain AI)

### Chapter Objectives
- Understand the key concepts and where they fit in production AI engineering.
- Apply one practical pattern from this lesson in code or system design.
- Connect this lesson to your capstone or portfolio narrative.

### How to Work Through This Chapter
1. Read each sub-lesson theory section in order.
2. Run the representative notebook examples and inspect outputs.
3. Capture one reusable artifact (template/checklist/snippet) for future projects.


### What You Cover in This Lesson
- **9.1 Deep Reinforcement Learning (RL)**
- **9.2 Advanced Computer Vision**
- **9.3 Advanced NLP & LLM Applications**
- **9.4 Domain AI: Applied AI in Key Industries**
- **9.5 Graph AI and GraphRAG Knowledge-Graph Pipelines**
- **9.6 Speech/Audio AI and Voice Agents**

### 9.1 Deep Reinforcement Learning (RL)

**Core concepts:** Policy and Value Functions; Bellman Equations; Tabular Methods; Policy Gradient Basics; Deep Q-Networks (DQN); $\epsilon$-greedy

Reinforcement Learning (RL) is the study of agents that learn behavior by interacting with an environment and optimizing long-term cumulative reward. Unlike supervised learning, RL does not usually receive a labeled "correct action" for each state. Unlike unsupervised learning, RL is explicitly goal-directed through rewards tied to sequential decisions.

where $\tau$ is a trajectory, $r_t$ rewards, and $\gamma\in[0,1)$ the discount factor.

Theory source: [`09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-1-deep-reinforcement-learning/theory/09-1-deep-reinforcement-learning.md`](09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-1-deep-reinforcement-learning/theory/09-1-deep-reinforcement-learning.md)

**Representative notebook:** [`09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-1-deep-reinforcement-learning/notebooks/09-1-deep-reinforcement-learning-gym-demo.ipynb`](09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-1-deep-reinforcement-learning/notebooks/09-1-deep-reinforcement-learning-gym-demo.ipynb)

```python
env = gym.make("FrozenLake-v1", is_slippery=True)

n_states = env.observation_space.n
n_actions = env.action_space.n

print(f"states={n_states}, actions={n_actions}")
```

```text
states=16, actions=4
```

### 9.2 Advanced Computer Vision

**Core concepts:** Object Detection; Semantic Segmentation; Instance Segmentation; Vision Transformers (ViT); CLIP-Style Models; Vision-Language Tasks

Modern computer vision has moved far beyond image classification. Production systems now require object detection, semantic/instance segmentation, multimodal understanding, and deployment-aware design for real-time and edge constraints.

$$ \text{Quality} \leftrightarrow \text{Latency} \leftrightarrow \text{Cost} \leftrightarrow \text{Robustness} $$

Theory source: [`09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-2-advanced-computer-vision/theory/09-2-advanced-computer-vision.md`](09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-2-advanced-computer-vision/theory/09-2-advanced-computer-vision.md)

**Representative notebook:** [`09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-2-advanced-computer-vision/notebooks/09-2-advanced-computer-vision-demo.ipynb`](09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-2-advanced-computer-vision/notebooks/09-2-advanced-computer-vision-demo.ipynb)

```python
from __future__ import annotations

import torch
from PIL import Image, ImageDraw
import torchvision
from torchvision.transforms import functional as F
import matplotlib.pyplot as plt

print('torch', torch.__version__)
print('torchvision', torchvision.__version__)
```

```text
torch 2.12.1+cu130
torchvision 0.27.1+cu130
```

### 9.3 Advanced NLP & LLM Applications

**Core concepts:** Sequence-to-Sequence Modeling; Pretraining Objectives; Adaptation Methods; Structured Outputs; Tools and Function Calling; Multi-Step Workflows

Advanced NLP today is dominated by transformer-based language models, large-scale pretraining, alignment techniques, and application-layer orchestration. Beyond basic prompting, production NLP/LLM systems require robust conditioning, retrieval, tool integration, and safety/evaluation loops.

Transformer encoder-decoder models (for example T5-like) are common in this setting.

Theory source: [`09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-3-advanced-nlp-and-llm-applications/theory/09-3-advanced-nlp-and-llm-applications.md`](09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-3-advanced-nlp-and-llm-applications/theory/09-3-advanced-nlp-and-llm-applications.md)

**Representative notebook:** [`09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-3-advanced-nlp-and-llm-applications/notebooks/09-3-advanced-nlp-and-llm-applications-demo.ipynb`](09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-3-advanced-nlp-and-llm-applications/notebooks/09-3-advanced-nlp-and-llm-applications-demo.ipynb)

```python
generator = pipeline("text-generation", model="distilgpt2", device=-1)

text = (
    "Reinforcement learning is a machine learning paradigm where an agent learns to make decisions "
    "by interacting with an environment. The agent receives rewards and aims to maximize cumulative "
    "return over time. Practical RL often struggles with sample inefficiency and training instability, "
    "which motivates replay buffers, target networks, and robust evaluation protocols."
)

prompt = f"Summarize this in 2 concise sentences:\n\n{text}\n\nSummary:"
summary = generator(
    prompt,
    max_new_tokens=40,
    do_sample=False,
    pad_token_id=generator.tokenizer.eos_token_id,
)[0]["generated_text"]
...
```

```text
Loading weights:   0%|          | 0/76 [00:00<?, ?it/s]
```

### 9.4 Domain AI: Applied AI in Key Industries

**Core concepts:** Healthcare AI; Finance AI; Smart Cities AI; Robotics and Control; 1) Clinical Decision Support Architecture; 2) Fraud Detection Architecture

Domain specialization is where generic AI skill becomes business value. The same model family behaves very differently across industries because data quality, constraints, regulation, risk tolerance, and operational environments vary.

$$ \text{Domain AI Success} = \text{Model Quality} \times \text{Domain Fit} \times \text{Operational Readiness} $$

Theory source: [`09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-4-domain-ai-applied-ai-in-key-industries/theory/09-4-domain-ai-applied-ai-in-key-industries.md`](09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-4-domain-ai-applied-ai-in-key-industries/theory/09-4-domain-ai-applied-ai-in-key-industries.md)

**Representative notebook:** [`09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-4-domain-ai-applied-ai-in-key-industries/notebooks/09-4-domain-ai-applied-ai-in-key-industries-case-studies.ipynb`](09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-4-domain-ai-applied-ai-in-key-industries/notebooks/09-4-domain-ai-applied-ai-in-key-industries-case-studies.ipynb)

```python
n = 1500
df = pd.DataFrame({
    "amount": np.random.exponential(120, n),
    "velocity_1h": np.random.poisson(2, n),
    "is_new_device": np.random.binomial(1, 0.25, n),
    "geo_mismatch": np.random.binomial(1, 0.15, n),
})

logit = (
    0.01 * df["amount"]
    + 0.6 * df["velocity_1h"]
    + 1.1 * df["is_new_device"]
    + 1.5 * df["geo_mismatch"]
    - 4.0
)
prob = 1 / (1 + np.exp(-logit))
...
```

```text
AUC: 0.84
              precision    recall  f1-score   support

           0      0.827     0.915     0.869       271
           1      0.693     0.500     0.581       104

    accuracy                          0.800       375
   macro avg      0.760     0.708     0.725       375
weighted avg      0.790     0.800     0.789       375
```

### 9.5 Graph AI and GraphRAG Knowledge-Graph Pipelines

**Core concepts:** Graph fundamentals; Knowledge graph representation; Graph ML tasks; Indexing pipeline; Query pipeline; Retrieval fusion strategy

Graph AI is the specialization track for problems where relationships are first-class signals, not optional metadata. In classical tabular ML, rows are often treated as independent. In graph systems, value comes from dependencies across entities: transactions linked by shared devices, documents linked by citations, services linked by runtime calls, or users linked by interaction history.

GraphRAG extends retrieval-augmented generation by explicitly modeling entities and links before generation. Vector retrieval answers "what text looks similar?" Graph retrieval answers "what entities are connected, through which path, and with what provenance?" High-quality enterprise assistants usually need both.

Theory source: [`09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-5-graph-ai-and-graphrag-knowledge-graph-pipelines/theory/09-5-graph-ai-and-graphrag-knowledge-graph-pipelines.md`](09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-5-graph-ai-and-graphrag-knowledge-graph-pipelines/theory/09-5-graph-ai-and-graphrag-knowledge-graph-pipelines.md)

**Representative notebook:** [`09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-5-graph-ai-and-graphrag-knowledge-graph-pipelines/notebooks/09-5-graph-ai-and-graphrag-pipeline-demo.ipynb`](09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-5-graph-ai-and-graphrag-knowledge-graph-pipelines/notebooks/09-5-graph-ai-and-graphrag-pipeline-demo.ipynb)

```python
docs = [
    {"id": "d1", "text": "Payment API depends on Auth Service and Redis cache."},
    {"id": "d2", "text": "Auth Service writes sessions to Redis cache."},
    {"id": "d3", "text": "Checkout Service calls Payment API for charge authorization."},
    {"id": "d4", "text": "Fraud Engine monitors Checkout Service and Payment API events."},
]

relations = [
    ("Payment API", "depends_on", "Auth Service"),
    ("Payment API", "depends_on", "Redis cache"),
    ("Auth Service", "writes_to", "Redis cache"),
    ("Checkout Service", "calls", "Payment API"),
    ("Fraud Engine", "monitors", "Checkout Service"),
    ("Fraud Engine", "monitors", "Payment API"),
]

...
```

```text
{'nodes': 5, 'edges': 6}
```

### 9.6 Speech/Audio AI and Voice Agents

**Core concepts:** ASR objective; Spoken language understanding (SLU); TTS objective; Reference architecture; Real-time constraints; Safety and abuse model

Speech/audio AI converts sound into meaning and action, then returns value through spoken output or downstream workflow automation. Voice agents are multimodal systems with tight latency budgets, user-experience constraints, and safety requirements that differ from text-only assistants.

Production-grade voice systems are system-design problems, not only model problems.

Theory source: [`09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-6-speech-audio-ai-and-voice-agents/theory/09-6-speech-audio-ai-and-voice-agents.md`](09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-6-speech-audio-ai-and-voice-agents/theory/09-6-speech-audio-ai-and-voice-agents.md)

**Representative notebook:** [`09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-6-speech-audio-ai-and-voice-agents/notebooks/09-6-speech-audio-ai-and-voice-agents-demo.ipynb`](09-advanced-ai-specializations-rl-cv-nlp-and-domain-ai/09-6-speech-audio-ai-and-voice-agents/notebooks/09-6-speech-audio-ai-and-voice-agents-demo.ipynb)

```python
sample_rate = 16000
seconds = 2
wave = 0.1 * np.random.randn(sample_rate * seconds)
print({"samples": wave.shape[0], "duration_s": seconds})


def asr_stub(audio: np.ndarray) -> str:
    # In real systems this would be Whisper/wav2vec-style inference.
    return "schedule maintenance window for payment api at 2 am"

transcript = asr_stub(wave)
transcript
```

```text
{'samples': 32000, 'duration_s': 2}
```


### Bridge to Next Lesson
You now have the core concepts and practical patterns from this lesson. Next, you will build on them in the following lesson with deeper abstraction, larger system scope, and stronger production tradeoff analysis.

[Back to Table of Contents](#table-of-contents)

## Lesson 10: Robotics, Edge AI & TinyML

### Chapter Objectives
- Understand the key concepts and where they fit in production AI engineering.
- Apply one practical pattern from this lesson in code or system design.
- Connect this lesson to your capstone or portfolio narrative.

### How to Work Through This Chapter
1. Read each sub-lesson theory section in order.
2. Run the representative notebook examples and inspect outputs.
3. Capture one reusable artifact (template/checklist/snippet) for future projects.


### What You Cover in This Lesson
- **10.1 Robotics & Control Foundations**
- **10.2 Perception, Planning & Navigation**
- **10.3 Edge AI & TinyML**
- **10.4 Integrated Robotics/IoT Project (Capstone)**

### 10.1 Robotics & Control Foundations

**Core concepts:** Configuration Space, Joints, and Degrees of Freedom; Forward vs Inverse Kinematics; Dynamics Intuition; Feedback Control; PID Controllers; Stability and Response

A robot is a physical system that senses the environment, computes decisions, and acts through actuators. In applied engineering, robotics sits at the intersection of three disciplines:

Configuration space (C-space) represents all possible robot configurations. Each independent joint variable contributes one degree of freedom (DoF).

Theory source: [`10-robotics-edge-ai-and-tinyml/10-1-robotics-and-control-foundations/theory/10-1-robotics-and-control-foundations.md`](10-robotics-edge-ai-and-tinyml/10-1-robotics-and-control-foundations/theory/10-1-robotics-and-control-foundations.md)

**Representative notebook:** [`10-robotics-edge-ai-and-tinyml/10-1-robotics-and-control-foundations/notebooks/10-1-robotics-and-control-foundations-demo.ipynb`](10-robotics-edge-ai-and-tinyml/10-1-robotics-and-control-foundations/notebooks/10-1-robotics-and-control-foundations-demo.ipynb)

```python
configs = {
    "Conservative": (1.2, 0.05, 0.4),
    "Balanced": (2.0, 0.15, 0.7),
    "Aggressive": (3.5, 0.25, 0.5),
}

target = 1.0
results = {}
for name, (kp, ki, kd) in configs.items():
    results[name] = simulate_pid(kp, ki, kd, target=target)

plt.figure(figsize=(10, 5))
for name, (t, x, _, _) in results.items():
    plt.plot(t, x, label=name)
plt.axhline(target, color='black', linestyle='--', linewidth=1, label='Target')
plt.xlabel('Time (s)')
...
```

```text
<Figure size 1000x500 with 1 Axes>
```

### 10.2 Perception, Planning & Navigation

**Core concepts:** Sensor Modalities; Vision Tasks Reused from Lesson 9; SLAM (Intuition); Occupancy Grids and Localization; Graph-Based Search (A*); Reactive vs Deliberative Navigation

Perception, planning, and navigation form the autonomy stack for mobile robots. A robot must infer where it is, understand free/occupied space, plan a feasible path, and execute motion safely under uncertainty.

Practical autonomy uses sensor fusion because no single sensor is reliable in all conditions.

Theory source: [`10-robotics-edge-ai-and-tinyml/10-2-perception-planning-and-navigation/theory/10-2-perception-planning-and-navigation.md`](10-robotics-edge-ai-and-tinyml/10-2-perception-planning-and-navigation/theory/10-2-perception-planning-and-navigation.md)

**Representative notebook:** [`10-robotics-edge-ai-and-tinyml/10-2-perception-planning-and-navigation/notebooks/10-2-perception-planning-and-navigation-demo.ipynb`](10-robotics-edge-ai-and-tinyml/10-2-perception-planning-and-navigation/notebooks/10-2-perception-planning-and-navigation-demo.ipynb)

```python
def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])  # Manhattan distance


def astar(grid, start, goal):
    rows, cols = grid.shape
    neighbors = [(1,0), (-1,0), (0,1), (0,-1)]

    open_heap = [(0 + heuristic(start, goal), 0, start)]
    came_from = {start: None}
    g_score = {start: 0}

    while open_heap:
        _, g, current = heapq.heappop(open_heap)
        if current == goal:
            # reconstruct path
...
```

```text
Path length: 19
```

### 10.3 Edge AI & TinyML

**Core concepts:** Resource Constraints; Latency and Offline Requirements; Reliability and Fleet Operations; Quantization and Model Compression; Deployment Targets; Case Study 1: Industrial Predictive Maintenance

Edge AI means running inference close to where data is produced (phones, cameras, gateways, embedded devices). TinyML is a subset focused on very constrained hardware, especially microcontrollers.

In robotics and IoT, response time can be safety-critical. Edge inference reduces round-trip delay and dependency on network availability.

Theory source: [`10-robotics-edge-ai-and-tinyml/10-3-edge-ai-and-tinyml/theory/10-3-edge-ai-and-tinyml.md`](10-robotics-edge-ai-and-tinyml/10-3-edge-ai-and-tinyml/theory/10-3-edge-ai-and-tinyml.md)

**Representative notebook:** [`10-robotics-edge-ai-and-tinyml/10-3-edge-ai-and-tinyml/notebooks/10-3-edge-ai-and-tinyml-demo.ipynb`](10-robotics-edge-ai-and-tinyml/10-3-edge-ai-and-tinyml/notebooks/10-3-edge-ai-and-tinyml-demo.ipynb)

```python
class TinyMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(16, 24),
            nn.ReLU(),
            nn.Linear(24, 12),
            nn.ReLU(),
            nn.Linear(12, 1),
        )

    def forward(self, x):
        return self.net(x)


model_fp32 = TinyMLP()
...
```

```text
FP32 test accuracy: 0.8320
```

### 10.4 Integrated Robotics/IoT Project (Capstone)

**Core concepts:** Option 1: Smart Home TinyML Sensor Network; Option 2: Simulated Warehouse Robot; Option 3: IoT Vibration Monitor with Edge Anomaly Detection; Template A: Device -> Edge -> Cloud; Template B: Robotics Navigation Stack; Template C: TinyML Fleet Management

This capstone integrates robotics control, perception/planning, and edge AI deployment into a single applied system. The goal is not maximal complexity; the goal is a coherent, testable, and portfolio-ready engineering artifact.

A strong capstone here should demonstrate system thinking across the full loop, not isolated model scores. Reviewers should be able to see how sensing uncertainty propagates into planning/control decisions and how telemetry closes the loop for operations. Even in simulation, your design should reflect real deployment pressures: constrained compute, non-ideal sensors, intermittent connectivity, and safety fallbacks.

Theory source: [`10-robotics-edge-ai-and-tinyml/10-4-integrated-robotics-iot-project-capstone/theory/10-4-integrated-robotics-iot-project-capstone.md`](10-robotics-edge-ai-and-tinyml/10-4-integrated-robotics-iot-project-capstone/theory/10-4-integrated-robotics-iot-project-capstone.md)

**Representative notebook:** [`10-robotics-edge-ai-and-tinyml/10-4-integrated-robotics-iot-project-capstone/notebooks/10-4-capstone-robotics-iot-system-template.ipynb`](10-robotics-edge-ai-and-tinyml/10-4-integrated-robotics-iot-project-capstone/notebooks/10-4-capstone-robotics-iot-system-template.ipynb)

```python
sensor = Sensor()
model = EdgeModel()
controller = Controller()
logger = CloudLogger()

for step in range(5):
    observation = sensor.read()
    pred = model.infer(observation)
    action = controller.act(pred)

    logger.log(
        {
            "step": step,
            "observation": observation,
            "prediction": pred,
            "action": action,
...
```

```text
LOG: {'step': 0, 'observation': {'vibration': 0.6287182091201923, 'temperature': 23.729205163237882}, 'prediction': {'label': 'normal', 'risk_score': 0.44010274638413455}, 'action': 'continue', 'timestamp': 1783057565.9454699}
LOG: {'step': 1, 'observation': {'vibration': 0.8875831555984995, 'temperature': 36.80765002924855}, 'prediction': {'label': 'anomaly', 'risk_score': 0.7574612095039206}, 'action': 'slow_down_and_alert', 'timestamp': 1783057565.9455214}
LOG: {'step': 2, 'observation': {'vibration': 0.06797539343657, 'temperature': 24.559286078096562}, 'prediction': {'label': 'normal', 'risk_score': 0.04758277540559899}, 'action': 'continue', 'timestamp': 1783057565.9455378}
LOG: {'step': 3, 'observation': {'vibration': 0.5972732541515713, 'temperature': 25.929647483804537}, 'prediction': {'label': 'normal', 'risk_score': 0.4180912779060999}, 'action': 'continue', 'timestamp': 1783057565.945552}
LOG: {'step': 4, 'observation': {'vibration': 0.13211352025004708, 'temperature': 40.577658749075916}, 'prediction': {'label': 'normal', 'risk_score': 0.3040326391565512}, 'action': 'continue', 'timestamp': 1783057565.9455647}
```


### Bridge to Next Lesson
You now have the core concepts and practical patterns from this lesson. Next, you will build on them in the following lesson with deeper abstraction, larger system scope, and stronger production tradeoff analysis.

[Back to Table of Contents](#table-of-contents)

## Lesson 11: AI Product Management, Entrepreneurship & Research Methods

### Chapter Objectives
- Understand the key concepts and where they fit in production AI engineering.
- Apply one practical pattern from this lesson in code or system design.
- Connect this lesson to your capstone or portfolio narrative.

### How to Work Through This Chapter
1. Read each sub-lesson theory section in order.
2. Run the representative notebook examples and inspect outputs.
3. Capture one reusable artifact (template/checklist/snippet) for future projects.


### What You Cover in This Lesson
- **11.1 AI Product Management Foundations**
- **11.2 AI Entrepreneurship & Startup Design**
- **11.3 AI Research Methods & AI-for-Science**
- **11.4 Portfolio, Capstone & Publication / Launch**

### 11.1 AI Product Management Foundations

**Core concepts:** A practical mental model; What AI PMs own; AI PM vs data scientist vs ML engineer vs classic PM; AI feature lifecycle; Formal framing; Use case checklist

AI Product Management exists because AI systems do not behave like deterministic software components. In conventional product delivery, if a feature is coded correctly and receives valid inputs, output behavior is usually stable. In AI products, behavior depends on data quality, model uncertainty, drift, and probabilistic output distributions.

Recent AI PM curricula increasingly emphasize this integration. Udacity's 2026 AI Product Manager Nanodegree explicitly combines PRDs, roadmap work, dataset strategy, LLM feature planning, and bias-impact measurement in one lifecycle. HelloPM and InstitutePM similarly frame AI PM as cross-functional orchestration across ML, UX, analytics, and stakeholder communication.

Theory source: [`11-ai-product-entrepreneurship-and-research-methods/11-1-ai-product-management-foundations/theory/11-1-ai-product-management-foundations.md`](11-ai-product-entrepreneurship-and-research-methods/11-1-ai-product-management-foundations/theory/11-1-ai-product-management-foundations.md)

**Representative notebook:** [`11-ai-product-entrepreneurship-and-research-methods/11-1-ai-product-management-foundations/notebooks/11-1-ai-product-management-foundations-tools.ipynb`](11-ai-product-entrepreneurship-and-research-methods/11-1-ai-product-management-foundations/notebooks/11-1-ai-product-management-foundations-tools.ipynb)

```python
X, y = make_classification(
    n_samples=2500,
    n_features=20,
    n_informative=10,
    n_redundant=5,
    weights=[0.8, 0.2],
    class_sep=1.0,
    random_state=SEED,
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=SEED,
    stratify=y,
...
```

```text
accuracy     0.894400
f1           0.727273
precision    0.771930
recall       0.687500
roc_auc      0.914078
dtype: float64
```

### 11.2 AI Entrepreneurship & Startup Design

**Core concepts:** Enterprise AI vs startup AI; Opportunity quality framework; AI-enabled market discovery; Problem-solution fit vs model-solution fit; Common AI business model patterns; AI-specific unit economics

AI entrepreneurship is not simply "start a company with a model." It is the disciplined process of discovering a painful market problem, designing a repeatable value engine, and delivering outcomes with AI as a leverage mechanism.

University and professional curricula in AI entrepreneurship now emphasize the full business loop: market analysis, AI-enabled opportunity assessment, business model design, product execution, and ethical implications. This is visible in current course/module structures from Southampton, JHU EP, and applied AI innovation certificates that combine team projects with business implementation.

Theory source: [`11-ai-product-entrepreneurship-and-research-methods/11-2-ai-entrepreneurship-and-startup-design/theory/11-2-ai-entrepreneurship-and-startup-design.md`](11-ai-product-entrepreneurship-and-research-methods/11-2-ai-entrepreneurship-and-startup-design/theory/11-2-ai-entrepreneurship-and-startup-design.md)

**Representative notebook:** [`11-ai-product-entrepreneurship-and-research-methods/11-2-ai-entrepreneurship-and-startup-design/notebooks/11-2-ai-entrepreneurship-and-startup-design-idea-lab.ipynb`](11-ai-product-entrepreneurship-and-research-methods/11-2-ai-entrepreneurship-and-startup-design/notebooks/11-2-ai-entrepreneurship-and-startup-design-idea-lab.ipynb)

```python
@dataclass
class AIStartupIdea:
    name: str
    problem_severity: int      # 1-10
    ai_fit: int                # 1-10
    data_access: int           # 1-10
    moat_strength: int         # 1-10
    ethics_risk: int           # 1-10 (higher is worse)
    go_to_market_clarity: int  # 1-10


def score_idea(idea: AIStartupIdea) -> Dict[str, float]:
    # Weighted score with explicit ethics penalty.
    base = (
        0.24 * idea.problem_severity
        + 0.20 * idea.ai_fit
...
```

```text
                          idea  base_score  ethics_penalty  total_score
0          SMB Finance Copilot        7.10             0.4         6.70
2  Edge Predictive Maintenance        6.72             0.3         6.42
3  Healthcare Triage Assistant        6.18             0.8         5.38
1          Generic Writing Bot        4.50             0.5         4.00
```

### 11.3 AI Research Methods & AI-for-Science

**Core concepts:** Formal, probabilistic, and empirical traditions; Qualitative vs quantitative research in AI contexts; Empirical vs theoretical contributions; Hypothesis formulation; Baselines, controls, and ablations; Reproducibility checklist

AI engineers who can run experiments are useful; AI engineers who can design valid experiments are rare.

Research literacy matters in production and science settings because it helps you:

Theory source: [`11-ai-product-entrepreneurship-and-research-methods/11-3-ai-research-methods-and-ai-for-science/theory/11-3-ai-research-methods-and-ai-for-science.md`](11-ai-product-entrepreneurship-and-research-methods/11-3-ai-research-methods-and-ai-for-science/theory/11-3-ai-research-methods-and-ai-for-science.md)

**Representative notebook:** [`11-ai-product-entrepreneurship-and-research-methods/11-3-ai-research-methods-and-ai-for-science/notebooks/11-3-ai-research-methods-and-ai-for-science-experiment-template.ipynb`](11-ai-product-entrepreneurship-and-research-methods/11-3-ai-research-methods-and-ai-for-science/notebooks/11-3-ai-research-methods-and-ai-for-science-experiment-template.ipynb)

```python
data = load_breast_cancer(as_frame=True)
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=SEED, stratify=y
)

models = {
    "log_reg": LogisticRegression(max_iter=2000, random_state=SEED),
    "random_forest": RandomForestClassifier(n_estimators=300, random_state=SEED),
}

rows = []
for name, model in models.items():
    model.fit(X_train, y_train)
...
```

```text
/home/ahmad/AI/Github/ai-engineering-zero-to-mastery/.venv/lib/python3.14/site-packages/sklearn/linear_model/_logistic.py:599: ConvergenceWarning: lbfgs failed to converge after 2000 iteration(s) (status=1):
STOP: TOTAL NO. OF ITERATIONS REACHED LIMIT

Increase the number of iterations to improve the convergence (max_iter=2000).
You might also want to scale the data as shown in:
    https://scikit-learn.org/stable/modules/preprocessing.html
Please also refer to the documentation for alternative solver options:
    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
  n_iter_i = _check_optimize_result(
```

### 11.4 Portfolio, Capstone & Publication / Launch

**Core concepts:** Build a portfolio architecture, not a random project list; Storytelling framework; Pattern A: End-to-end AI product; Pattern B: Research-style capstone; Pattern C: Domain-focused solution; Portfolio and Capstone Scoring Rubric

By Lesson 11, the objective is no longer "learn one more model." The objective is evidence of end-to-end capability.

Capstones are the highest-signal artifact because they force trade-off decisions across model quality, UX, reliability, and impact.

Theory source: [`11-ai-product-entrepreneurship-and-research-methods/11-4-portfolio-capstone-and-publication-or-launch/theory/11-4-portfolio-capstone-and-publication-or-launch.md`](11-ai-product-entrepreneurship-and-research-methods/11-4-portfolio-capstone-and-publication-or-launch/theory/11-4-portfolio-capstone-and-publication-or-launch.md)

**Representative notebook:** [`11-ai-product-entrepreneurship-and-research-methods/11-4-portfolio-capstone-and-publication-or-launch/notebooks/11-4-portfolio-and-capstone-planner.ipynb`](11-ai-product-entrepreneurship-and-research-methods/11-4-portfolio-capstone-and-publication-or-launch/notebooks/11-4-portfolio-and-capstone-planner.ipynb)

```python
@dataclass
class ProjectProfile:
    name: str
    technical_depth: int
    product_thinking: int
    domain_relevance: int
    research_rigor: int
    communication_quality: int


def score_project(p: ProjectProfile) -> float:
    return round(
        0.30 * p.technical_depth
        + 0.25 * p.product_thinking
        + 0.15 * p.domain_relevance
        + 0.20 * p.research_rigor
...
```

```text
                      project  technical_depth  product_thinking  \
0       RAG Support Assistant                8                 8   
1     Credit Risk ML Pipeline                7                 7   
3  Agentic Workflow Prototype                8                 7   
2    CV Defect Detection Demo                7                 5   

   domain_relevance  research_rigor  communication_quality  score  
0                 7               6                      7   7.35  
1                 8               7                      6   7.05  
3                 6               6                      6   6.85  
2                 6               5                      5   5.75  
```


### Bridge to Next Lesson
You now have the core concepts and practical patterns from this lesson. Next, you will build on them in the following lesson with deeper abstraction, larger system scope, and stronger production tradeoff analysis.

[Back to Table of Contents](#table-of-contents)

## Lesson 12: MLOps & LLMOps: Production AI & Operations

### Chapter Objectives
- Understand the key concepts and where they fit in production AI engineering.
- Apply one practical pattern from this lesson in code or system design.
- Connect this lesson to your capstone or portfolio narrative.

### How to Work Through This Chapter
1. Read each sub-lesson theory section in order.
2. Run the representative notebook examples and inspect outputs.
3. Capture one reusable artifact (template/checklist/snippet) for future projects.


### What You Cover in This Lesson
- **12.1 MLOps Foundations & ML Lifecycle in Production**
- **12.2 ML Pipelines, Deployment & Monitoring**
- **12.3 LLMOps Foundations & LLM Lifecycle**
- **12.4 LLM Application Deployment, Observability & Governance**
- **12.5 LLM Inference Systems Engineering**
- **12.6 LLM Evaluation, Data Flywheel & Continuous Post-Training Ops**
- **12.7 Distributed LLM Training Systems**
- **12.8 Privacy-Preserving ML and LLM Ops**
- **12.9 Data-Centric Labeling Ops**

### 12.1 MLOps Foundations & ML Lifecycle in Production

**Core concepts:** DevOps; DataOps; MLOps; Stage 1: Problem framing and KPI definition; Stage 2: Data lifecycle and feature preparation; Stage 3: Training, evaluation, and experiment management

MLOps is the engineering discipline of making machine learning systems reliable, repeatable, observable, and governable in production. A model that scores well in a notebook is not a production ML system. Production ML requires data contracts, pipeline orchestration, model packaging, deployment safety, and post-deployment monitoring.

$$ \text{Production ML Value} = f(\text{Model Quality}, \text{Data Reliability}, \text{Operational Reliability}, \text{Business Alignment}) $$

Theory source: [`12-mlops-and-llmops-production-ai-and-operations/12-1-mlops-foundations-and-ml-lifecycle/theory/12-1-mlops-foundations-and-ml-lifecycle.md`](12-mlops-and-llmops-production-ai-and-operations/12-1-mlops-foundations-and-ml-lifecycle/theory/12-1-mlops-foundations-and-ml-lifecycle.md)

**Representative notebook:** [`12-mlops-and-llmops-production-ai-and-operations/12-1-mlops-foundations-and-ml-lifecycle/notebooks/12-1-mlops-foundations-lifecycle-demo.ipynb`](12-mlops-and-llmops-production-ai-and-operations/12-1-mlops-foundations-and-ml-lifecycle/notebooks/12-1-mlops-foundations-lifecycle-demo.ipynb)

```python
X, y = make_classification(
    n_samples=2200,
    n_features=18,
    n_informative=10,
    n_redundant=4,
    weights=[0.78, 0.22],
    random_state=SEED,
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=SEED
)

X_train.shape, X_test.shape
```

```text
((1650, 18), (550, 18))
```

### 12.2 ML Pipelines, Deployment & Monitoring

**Core concepts:** Core pipeline layers; Batch vs streaming pipelines; Batch scoring; Online serving (REST/gRPC); Canary and blue-green releases; Observability layers

After foundational MLOps concepts, the next challenge is operational execution: reproducible pipelines, predictable deployments, and actionable monitoring.

This chapter focuses on the practical architecture behind production ML services:

Theory source: [`12-mlops-and-llmops-production-ai-and-operations/12-2-ml-pipelines-deployment-and-monitoring/theory/12-2-ml-pipelines-deployment-and-monitoring.md`](12-mlops-and-llmops-production-ai-and-operations/12-2-ml-pipelines-deployment-and-monitoring/theory/12-2-ml-pipelines-deployment-and-monitoring.md)

**Representative notebook:** [`12-mlops-and-llmops-production-ai-and-operations/12-2-ml-pipelines-deployment-and-monitoring/notebooks/12-2-ml-pipelines-deployment-and-monitoring-demo.ipynb`](12-mlops-and-llmops-production-ai-and-operations/12-2-ml-pipelines-deployment-and-monitoring/notebooks/12-2-ml-pipelines-deployment-and-monitoring-demo.ipynb)

```python
model = GradientBoostingClassifier(random_state=SEED)
model.fit(X_train, y_train)

holdout_proba = model.predict_proba(X_holdout)[:, 1]
holdout_pred = (holdout_proba >= 0.5).astype(int)

validation_metrics = {
    "holdout_accuracy": float(accuracy_score(y_holdout, holdout_pred)),
    "holdout_auc": float(roc_auc_score(y_holdout, holdout_proba)),
}
validation_metrics
```

```text
{'holdout_accuracy': 0.8911111111111111, 'holdout_auc': 0.9173141499368336}
```

### 12.3 LLMOps Foundations & LLM Lifecycle

**Core concepts:** Shared foundations; Additional LLMOps dimensions; Stage 1: Use-case and architecture selection; Stage 2: Data and context strategy; Stage 3: Prompt/workflow engineering; Stage 4: Evaluation and validation

LLMOps extends MLOps for large language model systems with additional complexity:

LLMOps is the set of practices that makes LLM-powered systems reliable, cost-aware, observable, and governable from design to production operations.

Theory source: [`12-mlops-and-llmops-production-ai-and-operations/12-3-llmops-foundations-and-llm-lifecycle/theory/12-3-llmops-foundations-and-llm-lifecycle.md`](12-mlops-and-llmops-production-ai-and-operations/12-3-llmops-foundations-and-llm-lifecycle/theory/12-3-llmops-foundations-and-llm-lifecycle.md)

**Representative notebook:** [`12-mlops-and-llmops-production-ai-and-operations/12-3-llmops-foundations-and-llm-lifecycle/notebooks/12-3-llmops-foundations-lifecycle-architecture.ipynb`](12-mlops-and-llmops-production-ai-and-operations/12-3-llmops-foundations-and-llm-lifecycle/notebooks/12-3-llmops-foundations-lifecycle-architecture.ipynb)

```python
queries = [
    "What security features do you provide?",
    "What does the starter plan include?",
    "Do you support enterprise audit logs?",
]

runs: List[LLMRun] = []

for i, q in enumerate(queries, start=1):
    retrieved = simple_retrieve(q, top_k=2)
    for pv in ["v1", "v2"]:
        response = mock_llm_answer(PROMPT_REGISTRY[pv], q, retrieved)
        grounded = int(bool(retrieved) and "Based on context" in response)
        est_tokens = len(response.split()) + len(q.split())
        runs.append(
            LLMRun(
...
```

```text
     run_id prompt_version                                   query  \
0  run_1_v1             v1  What security features do you provide?   
1  run_1_v2             v2  What security features do you provide?   
2  run_2_v1             v1     What does the starter plan include?   
3  run_2_v2             v2     What does the starter plan include?   
4  run_3_v1             v1   Do you support enterprise audit logs?   

   retrieved_docs                                           response  \
0              []                      I don't have enough evidence.   
1              []                      I don't have enough evidence.   
2  [doc_2, doc_1]  Based on context: Starter plan includes up to ...   
3  [doc_2, doc_1]  Based on context: Starter plan includes up to ...   
4  [doc_1, doc_2]  Based on context: Our enterprise plan supports...   

   grounded  answer_length  estimated_tokens  
0         0             29                11  
1         0             29                11  
2         1            144                29  
...
```

### 12.4 LLM Application Deployment, Observability & Governance

**Core concepts:** Layered architecture; Release strategies; Incident-aware design; What to trace; Metrics layers; Standardization and trace semantics

Deploying LLM applications is not just shipping an API endpoint. Production success requires orchestration across serving infrastructure, observability signals, evaluation workflows, and governance controls.

`Client -> API Gateway -> Orchestrator -> (Retriever + Tools + LLM) -> Post-Processor -> Policy Guardrails -> Response`

Theory source: [`12-mlops-and-llmops-production-ai-and-operations/12-4-llm-application-deployment-observability-and-governance/theory/12-4-llm-application-deployment-observability-and-governance.md`](12-mlops-and-llmops-production-ai-and-operations/12-4-llm-application-deployment-observability-and-governance/theory/12-4-llm-application-deployment-observability-and-governance.md)

**Representative notebook:** [`12-mlops-and-llmops-production-ai-and-operations/12-4-llm-application-deployment-observability-and-governance/notebooks/12-4-llmops-observability-and-evaluation-demo.ipynb`](12-mlops-and-llmops-production-ai-and-operations/12-4-llm-application-deployment-observability-and-governance/notebooks/12-4-llmops-observability-and-evaluation-demo.ipynb)

```python
@dataclass
class TraceEvent:
    request_id: str
    model: str
    prompt_version: str
    latency_ms: float
    input_tokens: int
    output_tokens: int
    grounded_score: float
    safety_flag: int
    http_status: int


def generate_trace(i: int) -> TraceEvent:
    latency = np.random.normal(loc=650, scale=120)
    in_tok = int(max(50, np.random.normal(420, 80)))
...
```

```text
  request_id             model prompt_version  latency_ms  input_tokens  \
0   req_0001  gpt-4o-mini-like         v3.2.1  974.821981           470   
1   req_0002  gpt-4o-mini-like         v3.2.1  548.230762           468   
2   req_0003  gpt-4o-mini-like         v3.2.1  672.643437           359   
3   req_0004  gpt-4o-mini-like         v3.2.1  962.716074           474   
4   req_0005  gpt-4o-mini-like         v3.2.1  445.269688           327   

   output_tokens  grounded_score  safety_flag  http_status  
0            225        0.900459            0          200  
1             79        0.928815            0          200  
2            133        0.954607            0          200  
3            195        1.000000            0          200  
4            173        0.886863            0          200  
```

### 12.5 LLM Inference Systems Engineering

**Core concepts:** Prefill vs decode; Why latency feels worse than average metrics; Cache strategies; Static batching; Continuous (inflight) batching; Scheduling policies

Many LLM products fail in production because teams optimize prompts but ignore inference systems engineering. At scale, user experience and cloud spend are driven by queueing, batching, KV-cache behavior, and hardware utilization.

Prefill is usually compute-heavy for long prompts; decode is iterative and latency-sensitive.

Theory source: [`12-mlops-and-llmops-production-ai-and-operations/12-5-llm-inference-systems-engineering/theory/12-5-llm-inference-systems-engineering.md`](12-mlops-and-llmops-production-ai-and-operations/12-5-llm-inference-systems-engineering/theory/12-5-llm-inference-systems-engineering.md)

**Representative notebook:** [`12-mlops-and-llmops-production-ai-and-operations/12-5-llm-inference-systems-engineering/notebooks/12-5-llm-inference-systems-engineering-simulation.ipynb`](12-mlops-and-llmops-production-ai-and-operations/12-5-llm-inference-systems-engineering/notebooks/12-5-llm-inference-systems-engineering-simulation.ipynb)

```python
n = 300
traffic = pd.DataFrame({
    'arrival_ms': np.cumsum(np.random.exponential(scale=40, size=n)).astype(int),
    'prompt_tokens': np.random.randint(80, 2000, size=n),
    'gen_tokens': np.random.randint(40, 600, size=n),
})
traffic.head()
```

```text
   arrival_ms  prompt_tokens  gen_tokens
0           3            750         147
1          63            194         279
2          86           1936         258
3         138            242         189
4         290            164         278
```

### 12.6 LLM Evaluation, Data Flywheel & Continuous Post-Training Ops

**Core concepts:** Offline evaluation; Online evaluation; Human evaluation; Quality metrics; Safety metrics; Reliability metrics

LLM quality in production is not a one-time training outcome. It is a continuous loop of:

This chapter covers evaluation systems, data flywheel design, and operational controls for continuous post-training.

Theory source: [`12-mlops-and-llmops-production-ai-and-operations/12-6-llm-evaluation-data-flywheel-and-continuous-post-training-ops/theory/12-6-llm-evaluation-data-flywheel-and-continuous-post-training-ops.md`](12-mlops-and-llmops-production-ai-and-operations/12-6-llm-evaluation-data-flywheel-and-continuous-post-training-ops/theory/12-6-llm-evaluation-data-flywheel-and-continuous-post-training-ops.md)

**Representative notebook:** [`12-mlops-and-llmops-production-ai-and-operations/12-6-llm-evaluation-data-flywheel-and-continuous-post-training-ops/notebooks/12-6-llm-evaluation-and-post-training-ops-playbook.ipynb`](12-mlops-and-llmops-production-ai-and-operations/12-6-llm-evaluation-data-flywheel-and-continuous-post-training-ops/notebooks/12-6-llm-evaluation-and-post-training-ops-playbook.ipynb)

```python
eval_df = pd.DataFrame({
    'id': [1,2,3,4,5,6],
    'prompt': ['refund annual plan policy', 'generate SQL for active users', 'summarize incident RCA', 'reset MFA steps', 'PII policy for logs', 'onboarding checklist'],
    'reference': ['policy_v2', 'sql_correct', 'rca_summary_good', 'mfa_steps', 'pii_policy_v1', 'onboarding_v1'],
    'model_a': ['policy_v1', 'sql_correct', 'rca_summary_good', 'mfa_steps', 'pii_policy_v0', 'onboarding_v1'],
    'model_b': ['policy_v2', 'sql_correct', 'rca_summary_good', 'mfa_steps', 'pii_policy_v1', 'onboarding_v1'],
    'safety_flag_a': [0,0,0,1,0,0],
    'safety_flag_b': [0,0,0,0,0,0],
    'latency_ms_a': [820,760,990,870,920,700],
    'latency_ms_b': [860,780,1020,900,940,730],
    'user_rating_a': [3,4,4,2,3,4],
    'user_rating_b': [4,4,4,4,4,4],
})
eval_df
```

```text
   id                         prompt         reference           model_a  \
0   1      refund annual plan policy         policy_v2         policy_v1   
1   2  generate SQL for active users       sql_correct       sql_correct   
2   3         summarize incident RCA  rca_summary_good  rca_summary_good   
3   4                reset MFA steps         mfa_steps         mfa_steps   
4   5            PII policy for logs     pii_policy_v1     pii_policy_v0   
5   6           onboarding checklist     onboarding_v1     onboarding_v1   

            model_b  safety_flag_a  safety_flag_b  latency_ms_a  latency_ms_b  \
0         policy_v2              0              0           820           860   
1       sql_correct              0              0           760           780   
2  rca_summary_good              0              0           990          1020   
3         mfa_steps              1              0           870           900   
4     pii_policy_v1              0              0           920           940   
5     onboarding_v1              0              0           700           730   

   user_rating_a  user_rating_b  
0              3              4  
...
```

### 12.7 Distributed LLM Training Systems

**Core concepts:** Data parallelism (DDP baseline); Fully Sharded Data Parallel (FSDP); ZeRO (DeepSpeed); Tensor and pipeline parallelism; Stepwise decision path; Capacity sizing heuristic

Distributed LLM training becomes mandatory when model parameters, sequence length, or throughput targets exceed single-device limits. This chapter focuses on system-level decisions: how to partition memory and compute, how to keep runs stable, and how to reason about cost-performance trade-offs under real infrastructure constraints.

For most teams, the challenge is not "which buzzword parallelism to use?" but "what is the simplest strategy that fits memory, meets throughput, and remains operable by the team?"

Theory source: [`12-mlops-and-llmops-production-ai-and-operations/12-7-distributed-llm-training-systems/theory/12-7-distributed-llm-training-systems.md`](12-mlops-and-llmops-production-ai-and-operations/12-7-distributed-llm-training-systems/theory/12-7-distributed-llm-training-systems.md)

**Representative notebook:** [`12-mlops-and-llmops-production-ai-and-operations/12-7-distributed-llm-training-systems/notebooks/12-7-distributed-llm-training-systems-playbook.ipynb`](12-mlops-and-llmops-production-ai-and-operations/12-7-distributed-llm-training-systems/notebooks/12-7-distributed-llm-training-systems-playbook.ipynb)

```python
gpu_count = torch.cuda.device_count()
print({"cuda": torch.cuda.is_available(), "gpu_count": gpu_count})
if gpu_count:
    for i in range(gpu_count):
        print(i, torch.cuda.get_device_name(i))
```

```text
{'cuda': True, 'gpu_count': 1}
0 NVIDIA GeForce RTX 4060 Laptop GPU
```

### 12.8 Privacy-Preserving ML and LLM Ops

**Core concepts:** Federated learning; Differential privacy (DP); Secure aggregation; Threat categories; Control mapping; Data minimization and lifecycle controls

Privacy-preserving ML/LLMOps aims to generate model value while minimizing exposure of sensitive data. In healthcare, finance, and public-sector systems, privacy controls are not optional "add-ons"; they are design constraints that shape architecture, operations, and release criteria.

The practical question is rarely "privacy or performance?" It is "which privacy mechanism satisfies legal and risk requirements with acceptable utility and operational complexity?"

Theory source: [`12-mlops-and-llmops-production-ai-and-operations/12-8-privacy-preserving-ml-and-llm-ops/theory/12-8-privacy-preserving-ml-and-llm-ops.md`](12-mlops-and-llmops-production-ai-and-operations/12-8-privacy-preserving-ml-and-llm-ops/theory/12-8-privacy-preserving-ml-and-llm-ops.md)

**Representative notebook:** [`12-mlops-and-llmops-production-ai-and-operations/12-8-privacy-preserving-ml-and-llm-ops/notebooks/12-8-privacy-preserving-ml-and-llm-ops-demo.ipynb`](12-mlops-and-llmops-production-ai-and-operations/12-8-privacy-preserving-ml-and-llm-ops/notebooks/12-8-privacy-preserving-ml-and-llm-ops-demo.ipynb)

```python
X, y = make_classification(n_samples=1200, n_features=12, n_informative=7, random_state=42)
clients = 4
chunks = np.array_split(np.arange(len(X)), clients)
client_sets = [(X[idx], y[idx]) for idx in chunks]
print([c[0].shape for c in client_sets])
```

```text
[(300, 12), (300, 12), (300, 12), (300, 12)]
```

### 12.9 Data-Centric Labeling Ops

**Core concepts:** End-to-end lifecycle; Label quality dimensions; Data contracts for labeling; Governance controls; Ops telemetry; Queue design patterns

Data-centric labeling ops treats labels as production assets managed by engineering discipline. Many teams plateau not because model architecture is weak, but because label policy, coverage, and quality are inconsistent. This chapter focuses on building repeatable labeling flywheels that improve model performance with measurable ROI.

Active learning prioritizes examples that maximize model improvement per annotation dollar.

Theory source: [`12-mlops-and-llmops-production-ai-and-operations/12-9-data-centric-labeling-ops/theory/12-9-data-centric-labeling-ops.md`](12-mlops-and-llmops-production-ai-and-operations/12-9-data-centric-labeling-ops/theory/12-9-data-centric-labeling-ops.md)

**Representative notebook:** [`12-mlops-and-llmops-production-ai-and-operations/12-9-data-centric-labeling-ops/notebooks/12-9-data-centric-labeling-ops-workbench.ipynb`](12-mlops-and-llmops-production-ai-and-operations/12-9-data-centric-labeling-ops/notebooks/12-9-data-centric-labeling-ops-workbench.ipynb)

```python
X, y = make_classification(n_samples=1200, n_features=14, n_informative=8, random_state=42)
idx = np.arange(len(X))
np.random.shuffle(idx)

seed_n = 120
labeled_idx = idx[:seed_n]
unlabeled_idx = idx[seed_n:900]
test_idx = idx[900:]

X_l, y_l = X[labeled_idx], y[labeled_idx]
X_u, y_u_true = X[unlabeled_idx], y[unlabeled_idx]
X_test, y_test = X[test_idx], y[test_idx]

print({"labeled": len(X_l), "unlabeled": len(X_u), "test": len(X_test)})
```

```text
{'labeled': 120, 'unlabeled': 780, 'test': 300}
```


### Bridge to Next Lesson
You now have the core concepts and practical patterns from this lesson. Next, you will build on them in the following lesson with deeper abstraction, larger system scope, and stronger production tradeoff analysis.

[Back to Table of Contents](#table-of-contents)

## Lesson 13: AI Safety, Security & Trustworthy AI

### Chapter Objectives
- Understand the key concepts and where they fit in production AI engineering.
- Apply one practical pattern from this lesson in code or system design.
- Connect this lesson to your capstone or portfolio narrative.

### How to Work Through This Chapter
1. Read each sub-lesson theory section in order.
2. Run the representative notebook examples and inspect outputs.
3. Capture one reusable artifact (template/checklist/snippet) for future projects.


### What You Cover in This Lesson
- **13.1 AI Safety & Alignment Fundamentals**
- **13.2 Robustness, Adversarial ML & AI Security**
- **13.3 Trustworthy AI: Robust, Fair, Explainable & Governed Systems**
- **13.4 Practical Guardrails, Evaluations & Safe Agent Design**

### 13.1 AI Safety & Alignment Fundamentals

**Core concepts:** Overview; Key Concepts in AI Safety; Safety Streams; Safety Engineering Basics; Applied Framework: Alignment-by-Design Checklist; Safety Case Studies & Exceptions

AI safety studies how to design, deploy, and govern AI systems so they remain beneficial under real-world pressure: distribution shift, strategic misuse, scale effects, and automation of high-impact decisions. Alignment focuses on a narrower but central question: do system objectives and learned behaviors remain compatible with human intent and constraints?

Let a system optimize an operational objective $\hat{U}$ while stakeholders care about a true utility $U^*$. A core alignment risk is:

Theory source: [`13-ai-safety-security-and-trustworthy-ai/13-1-ai-safety-and-alignment-fundamentals/theory/13-1-ai-safety-and-alignment-fundamentals.md`](13-ai-safety-security-and-trustworthy-ai/13-1-ai-safety-and-alignment-fundamentals/theory/13-1-ai-safety-and-alignment-fundamentals.md)

**Representative notebook:** [`13-ai-safety-security-and-trustworthy-ai/13-1-ai-safety-and-alignment-fundamentals/notebooks/13-1-ai-safety-and-alignment-fundamentals-scenarios.ipynb`](13-ai-safety-security-and-trustworthy-ai/13-1-ai-safety-and-alignment-fundamentals/notebooks/13-1-ai-safety-and-alignment-fundamentals-scenarios.ipynb)

```python
scenarios = pd.DataFrame(
    [
        {
            "scenario": "Feed ranking",
            "intended_goal": "Long-term user value",
            "proxy_metric": "Click-through rate",
            "failure_mode": "Sensational content over-ranked",
            "safer_redesign": "Multi-objective ranking with quality constraints",
        },
        {
            "scenario": "Support triage",
            "intended_goal": "Resolve highest-risk tickets first",
            "proxy_metric": "Average handling time",
            "failure_mode": "Complex critical tickets deferred",
            "safer_redesign": "Risk-weighted SLA and escalation policy",
        },
...
```

```text
           scenario                       intended_goal  \
0      Feed ranking                Long-term user value   
1    Support triage  Resolve highest-risk tickets first   
2  Safety assistant           Prevent harmful responses   

            proxy_metric                       failure_mode  \
0     Click-through rate    Sensational content over-ranked   
1  Average handling time  Complex critical tickets deferred   
2           Refusal rate         Over-refusal harms utility   

                                     safer_redesign  
0  Multi-objective ranking with quality constraints  
1           Risk-weighted SLA and escalation policy  
2    Context-aware policy and calibrated confidence  
```

### 13.2 Robustness, Adversarial ML & AI Security

**Core concepts:** Overview; Adversarial Machine Learning; Robustness & Evaluation; AI Security & Offensive AI; Security Operations Pattern for AI Systems; Safety & Security Case Studies & Exceptions

Robustness and security are foundational to safe AI operations. A model can be accurate on clean validation data and still fail under intentional attack or small environmental shifts. Adversarial ML studies those failures and defensive techniques.

This dual-use reality requires defenders to secure both AI-enabled products and AI-enhanced adversaries.

Theory source: [`13-ai-safety-security-and-trustworthy-ai/13-2-robustness-adversarial-ml-and-ai-security/theory/13-2-robustness-adversarial-ml-and-ai-security.md`](13-ai-safety-security-and-trustworthy-ai/13-2-robustness-adversarial-ml-and-ai-security/theory/13-2-robustness-adversarial-ml-and-ai-security.md)

**Representative notebook:** [`13-ai-safety-security-and-trustworthy-ai/13-2-robustness-adversarial-ml-and-ai-security/notebooks/13-2-robustness-and-adversarial-ml-demo.ipynb`](13-ai-safety-security-and-trustworthy-ai/13-2-robustness-adversarial-ml-and-ai-security/notebooks/13-2-robustness-and-adversarial-ml-demo.ipynb)

```python
digits = load_digits()
X, y = digits.data, digits.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

clf = LogisticRegression(max_iter=2000)
clf.fit(X_train_s, y_train)

clean_acc = accuracy_score(y_test, clf.predict(X_test_s))
clean_acc
```

```text
0.9777777777777777
```

### 13.3 Trustworthy AI: Robust, Fair, Explainable & Governed Systems

**Core concepts:** Overview; Fairness & Non-Discrimination; Explainability & Interpretability; Governance & Assurance; Building Trustworthy Systems in Practice; Safety & Security Case Studies & Exceptions

Trustworthy AI is a systems property, not a single model feature. A trustworthy system is expected to be:

$$ \text{Trustworthiness} = f(\text{technical reliability}, \text{ethical validity}, \text{governance maturity}) $$

Theory source: [`13-ai-safety-security-and-trustworthy-ai/13-3-trustworthy-ai-robust-fair-explainable-and-governed-systems/theory/13-3-trustworthy-ai-robust-fair-explainable-and-governed-systems.md`](13-ai-safety-security-and-trustworthy-ai/13-3-trustworthy-ai-robust-fair-explainable-and-governed-systems/theory/13-3-trustworthy-ai-robust-fair-explainable-and-governed-systems.md)

**Representative notebook:** [`13-ai-safety-security-and-trustworthy-ai/13-3-trustworthy-ai-robust-fair-explainable-and-governed-systems/notebooks/13-3-trustworthy-ai-fairness-and-explainability-demo.ipynb`](13-ai-safety-security-and-trustworthy-ai/13-3-trustworthy-ai-robust-fair-explainable-and-governed-systems/notebooks/13-3-trustworthy-ai-fairness-and-explainability-demo.ipynb)

```python
n = 3000
protected = np.random.binomial(1, 0.45, size=n)  # 0/1 group indicator

income_score = np.random.normal(0.0 + 0.3 * protected, 1.0, size=n)
credit_history = np.random.normal(0.2, 1.2, size=n)
debt_ratio = np.random.beta(2, 5, size=n)

# True approval propensity with structural bias term
logit = 0.9 * income_score + 0.6 * credit_history - 2.2 * debt_ratio - 0.35 * protected
prob = 1 / (1 + np.exp(-logit))
y = np.random.binomial(1, prob)

df = pd.DataFrame(
    {
        "income_score": income_score,
        "credit_history": credit_history,
...
```

```text
   income_score  credit_history  debt_ratio  protected  approved
0      0.416603       -1.068969    0.197406          1         0
1     -0.097093       -0.213212    0.194100          0         0
2      1.203193        0.868782    0.310849          0         1
3      0.220291        0.726494    0.716868          1         0
4      0.540631       -1.722355    0.236287          1         0
```

### 13.4 Practical Guardrails, Evaluations & Safe Agent Design

**Core concepts:** Overview; Guardrail Techniques; Evaluation & Red Teaming; Safe Agent Design; Governance Linkages; Safety & Security Case Studies & Exceptions

Modern LLM and agent systems combine language generation, retrieval, tool use, and workflow automation. This increases utility and also expands risk surface: policy violations, prompt injection, unauthorized tool actions, unsafe autonomy, and cost blowups.

These methods improve baseline behavior but do not replace application-level controls.

Theory source: [`13-ai-safety-security-and-trustworthy-ai/13-4-practical-guardrails-evaluations-and-safe-agent-design/theory/13-4-practical-guardrails-evaluations-and-safe-agent-design.md`](13-ai-safety-security-and-trustworthy-ai/13-4-practical-guardrails-evaluations-and-safe-agent-design/theory/13-4-practical-guardrails-evaluations-and-safe-agent-design.md)

**Representative notebook:** [`13-ai-safety-security-and-trustworthy-ai/13-4-practical-guardrails-evaluations-and-safe-agent-design/notebooks/13-4-guardrails-and-safety-evaluation-playbook.ipynb`](13-ai-safety-security-and-trustworthy-ai/13-4-practical-guardrails-evaluations-and-safe-agent-design/notebooks/13-4-guardrails-and-safety-evaluation-playbook.ipynb)

```python
SAFETY_POLICY = {
    "disallowed_keywords": ["build malware", "bypass authentication", "steal credentials"],
    "sensitive_patterns": [r"\b\d{3}-\d{2}-\d{4}\b", r"\b(?:\d[ -]*?){13,16}\b"],  # SSN / card-like
    "allowed_tools": {
        "calculator": ["add", "subtract", "multiply", "divide"],
        "knowledge_search": ["query_docs"],
    },
    "risk_threshold_for_human_review": "medium",
}

SAFETY_POLICY
```

```text
{'disallowed_keywords': ['build malware',
  'bypass authentication',
  'steal credentials'],
 'sensitive_patterns': ['\\b\\d{3}-\\d{2}-\\d{4}\\b',
  '\\b(?:\\d[ -]*?){13,16}\\b'],
 'allowed_tools': {'calculator': ['add', 'subtract', 'multiply', 'divide'],
  'knowledge_search': ['query_docs']},
 'risk_threshold_for_human_review': 'medium'}
```


### Bridge to Next Lesson
You now have the core concepts and practical patterns from this lesson. Next, you will build on them in the following lesson with deeper abstraction, larger system scope, and stronger production tradeoff analysis.

[Back to Table of Contents](#table-of-contents)

## Lesson 14: Frontier & Emerging Directions in AI

### Chapter Objectives
- Understand the key concepts and where they fit in production AI engineering.
- Apply one practical pattern from this lesson in code or system design.
- Connect this lesson to your capstone or portfolio narrative.

### How to Work Through This Chapter
1. Read each sub-lesson theory section in order.
2. Run the representative notebook examples and inspect outputs.
3. Capture one reusable artifact (template/checklist/snippet) for future projects.


### What You Cover in This Lesson
- **14.1 Neurosymbolic AI & Causal Reasoning**
- **14.2 Multi-Agent Systems & Complex Environments**
- **14.3 Quantum & Neuromorphic AI (Conceptual Overview)**
- **14.4 Lifelong Learning, Reading Groups & Contributing to the Field**
- **14.5 GenAI Observability and Evaluation Standards**

### 14.1 Neurosymbolic AI & Causal Reasoning

**Core concepts:** Overview; Neurosymbolic AI; Causal Reasoning in ML; Example Use Cases; Frontier Case Studies & Exceptions; Interview Questions & Answers

Frontier AI research increasingly focuses on improving reliability, reasoning, and transfer under distribution shift. Two major lines are especially important for applied engineers:

$$ \text{NeSy System} = \text{Neural Perception} + \text{Structured Reasoning} $$

Theory source: [`14-frontier-and-emerging-directions-in-ai/14-1-neurosymbolic-ai-and-causal-reasoning/theory/14-1-neurosymbolic-ai-and-causal-reasoning.md`](14-frontier-and-emerging-directions-in-ai/14-1-neurosymbolic-ai-and-causal-reasoning/theory/14-1-neurosymbolic-ai-and-causal-reasoning.md)

**Representative notebook:** [`14-frontier-and-emerging-directions-in-ai/14-1-neurosymbolic-ai-and-causal-reasoning/notebooks/14-1-neurosymbolic-and-causal-reasoning-toy-demo.ipynb`](14-frontier-and-emerging-directions-in-ai/14-1-neurosymbolic-ai-and-causal-reasoning/notebooks/14-1-neurosymbolic-and-causal-reasoning-toy-demo.ipynb)

```python
G = nx.DiGraph()
G.add_edges_from(
    [
        ("Policy", "AdSpend"),
        ("Economy", "AdSpend"),
        ("Economy", "Demand"),
        ("AdSpend", "Demand"),
        ("Demand", "Revenue"),
    ]
)

plt.figure(figsize=(7, 4))
pos = nx.spring_layout(G, seed=7)
nx.draw_networkx(G, pos=pos, node_color="#d9e8fb", node_size=1700, arrows=True)
plt.title("Toy Causal DAG")
plt.axis("off")
...
```

```text
<Figure size 700x400 with 1 Axes>
```

### 14.2 Multi-Agent Systems & Complex Environments

**Core concepts:** Overview; Multi-Agent Basics; Complex Environments & Emergent Behaviour; Practical & Safety Considerations; Frontier Case Studies & Exceptions; Interview Questions & Answers

Multi-agent systems (MAS) model environments where several autonomous entities learn or act simultaneously. This is important because many real systems are inherently interactive:

For practitioners, these concepts help diagnose policy oscillation, collusion, and fragile coordination.

Theory source: [`14-frontier-and-emerging-directions-in-ai/14-2-multi-agent-systems-and-complex-environments/theory/14-2-multi-agent-systems-and-complex-environments.md`](14-frontier-and-emerging-directions-in-ai/14-2-multi-agent-systems-and-complex-environments/theory/14-2-multi-agent-systems-and-complex-environments.md)

**Representative notebook:** [`14-frontier-and-emerging-directions-in-ai/14-2-multi-agent-systems-and-complex-environments/notebooks/14-2-multi-agent-gridworld-toy-demo.ipynb`](14-frontier-and-emerging-directions-in-ai/14-2-multi-agent-systems-and-complex-environments/notebooks/14-2-multi-agent-gridworld-toy-demo.ipynb)

```python
configs = {
    "random_vs_random": (random_policy, random_policy),
    "greedy_vs_random": (greedy_policy, random_policy),
    "greedy_vs_greedy": (greedy_policy, greedy_policy),
}

rows = []
for name, (pa, pb) in configs.items():
    for ep in range(EPISODES):
        out = run_episode(pa, pb)
        rows.append({"config": name, "episode": ep, **out})

results = pd.DataFrame(rows)
summary = (
    results.groupby("config")
    .agg(
...
```

```text
             config  mean_reward_a  mean_reward_b  mean_collisions
0  greedy_vs_greedy     -62.050000      -62.05000        28.000000
1  greedy_vs_random     143.058750       -7.45250         1.450000
2  random_vs_random      -4.975833       -4.47625         0.291667
```

### 14.3 Quantum & Neuromorphic AI (Conceptual Overview)

**Core concepts:** Overview; Quantum Machine Learning - Intuition Only; Neuromorphic & Brain-Inspired Computing; Relationship to Mainstream AI Practice; Frontier Case Studies & Exceptions; Interview Questions & Answers

Quantum and neuromorphic AI are hardware-centric frontier directions. They are not drop-in replacements for mainstream ML stacks today, but they shape long-term capability, efficiency, and algorithm design thinking.

Neuromorphic computing builds hardware and algorithms inspired by neural spiking and co-located memory/compute patterns in biological systems.

Theory source: [`14-frontier-and-emerging-directions-in-ai/14-3-quantum-and-neuromorphic-ai/theory/14-3-quantum-and-neuromorphic-ai.md`](14-frontier-and-emerging-directions-in-ai/14-3-quantum-and-neuromorphic-ai/theory/14-3-quantum-and-neuromorphic-ai.md)

**Representative notebook:** [`14-frontier-and-emerging-directions-in-ai/14-3-quantum-and-neuromorphic-ai/notebooks/14-3-frontier-technologies-concept-map.ipynb`](14-frontier-and-emerging-directions-in-ai/14-3-quantum-and-neuromorphic-ai/notebooks/14-3-frontier-technologies-concept-map.ipynb)

```python
frontier_topics = {
    "quantum_ml": {
        "core_questions": [
            "Is there evidence of practical advantage for this problem class?",
            "Can we run a hybrid pilot with clear baseline comparisons?",
            "Do we have access to tooling and specialists?",
        ],
        "suggested_resources": [
            "https://ep.jhu.edu/courses/605628-introduction-to-quantum-machine-learning/",
            "https://www.ibm.com/think/topics/quantum-machine-learning",
        ],
    },
    "neuromorphic_ai": {
        "core_questions": [
            "Is power budget the dominant constraint?",
            "Is the workload event-driven and sparse?",
...
```

```text
{'quantum_ml': {'core_questions': ['Is there evidence of practical advantage for this problem class?',
   'Can we run a hybrid pilot with clear baseline comparisons?',
   'Do we have access to tooling and specialists?'],
  'suggested_resources': ['https://ep.jhu.edu/courses/605628-introduction-to-quantum-machine-learning/',
   'https://www.ibm.com/think/topics/quantum-machine-learning']},
 'neuromorphic_ai': {'core_questions': ['Is power budget the dominant constraint?',
   'Is the workload event-driven and sparse?',
   'Do lifecycle costs justify non-standard hardware/toolchain?'],
  'suggested_resources': ['https://courses.ece.cmu.edu/18743SV',
   'https://www.ibm.com/think/topics/neuromorphic-computing',
   'https://www.cse.sc.edu/class/714']}}
```

### 14.4 Lifelong Learning, Reading Groups & Contributing to the Field

**Core concepts:** Overview; Reading & Staying Current; Building & Joining Communities; Contributing to the Field; Designing Your Personal AI Roadmap; Frontier Case Studies & Exceptions

AI evolves faster than static degree plans. A strong AI engineer must develop learning systems, not just complete courses.

This chapter turns those pillars into a practical operating system for long-term growth.

Theory source: [`14-frontier-and-emerging-directions-in-ai/14-4-lifelong-learning-reading-groups-and-contributing/theory/14-4-lifelong-learning-reading-groups-and-contributing.md`](14-frontier-and-emerging-directions-in-ai/14-4-lifelong-learning-reading-groups-and-contributing/theory/14-4-lifelong-learning-reading-groups-and-contributing.md)

**Representative notebook:** [`14-frontier-and-emerging-directions-in-ai/14-4-lifelong-learning-reading-groups-and-contributing/notebooks/14-4-personal-ai-learning-roadmap-planner.ipynb`](14-frontier-and-emerging-directions-in-ai/14-4-lifelong-learning-reading-groups-and-contributing/notebooks/14-4-personal-ai-learning-roadmap-planner.ipynb)

```python
import pandas as pd

tracks = {
    "research": {
        "activities": [
            "Read and replicate one paper per month",
            "Join technical reading group",
            "Run ablation-focused experiments",
            "Write short technical reports",
        ]
    },
    "engineering": {
        "activities": [
            "Ship production-grade ML/LLM pipeline project",
            "Practice evaluation/monitoring patterns",
            "Contribute to open-source tooling",
...
```

```text
{'research': {'activities': ['Read and replicate one paper per month',
   'Join technical reading group',
   'Run ablation-focused experiments',
   'Write short technical reports']},
 'engineering': {'activities': ['Ship production-grade ML/LLM pipeline project',
   'Practice evaluation/monitoring patterns',
   'Contribute to open-source tooling',
   'Document architecture decisions']},
 'product': {'activities': ['Define AI product PRDs and metric trees',
   'Run small user validation studies',
   'Prototype workflow assistants',
   'Publish product case analyses']},
 'safety': {'activities': ['Study alignment/robustness materials',
   'Build guardrail and eval test suites',
   'Participate in safety reading groups',
   'Write incident-style postmortems']}}
```

### 14.5 GenAI Observability and Evaluation Standards

**Core concepts:** Interoperability; Reproducibility; Governance and audits; OpenTelemetry baseline; Minimum production telemetry schema; Agent-specific extensions

As GenAI applications move from demos to business-critical systems, teams need standards for telemetry and evaluation. Without common schemas, metrics, and trace semantics, organizations cannot compare releases, audit incidents, or scale operations across tools and teams.

This chapter focuses on practical standardization patterns for LLM and agent systems, including OpenTelemetry-aligned conventions and benchmark harness integration.

Theory source: [`14-frontier-and-emerging-directions-in-ai/14-5-genai-observability-and-evaluation-standards/theory/14-5-genai-observability-and-evaluation-standards.md`](14-frontier-and-emerging-directions-in-ai/14-5-genai-observability-and-evaluation-standards/theory/14-5-genai-observability-and-evaluation-standards.md)

**Representative notebook:** [`14-frontier-and-emerging-directions-in-ai/14-5-genai-observability-and-evaluation-standards/notebooks/14-5-genai-observability-and-evaluation-standards-playbook.ipynb`](14-frontier-and-emerging-directions-in-ai/14-5-genai-observability-and-evaluation-standards/notebooks/14-5-genai-observability-and-evaluation-standards-playbook.ipynb)

```python
core_fields = [
    "trace_id", "session_id", "model_id", "provider",
    "latency_ms", "prompt_tokens", "completion_tokens",
    "tool_calls", "safety_flag", "user_rating"
]
pd.DataFrame({"field": core_fields})
```

```text
               field
0           trace_id
1         session_id
2           model_id
3           provider
4         latency_ms
5      prompt_tokens
6  completion_tokens
7         tool_calls
8        safety_flag
9        user_rating
```


### Bridge to Next Lesson
You now have the core concepts and practical patterns from this lesson. Next, you will build on them in the following lesson with deeper abstraction, larger system scope, and stronger production tradeoff analysis.

[Back to Table of Contents](#table-of-contents)

## Lesson 15: AI Engineering Capstone & Professional Practice

### Chapter Objectives
- Understand the key concepts and where they fit in production AI engineering.
- Apply one practical pattern from this lesson in code or system design.
- Connect this lesson to your capstone or portfolio narrative.

### How to Work Through This Chapter
1. Read each sub-lesson theory section in order.
2. Run the representative notebook examples and inspect outputs.
3. Capture one reusable artifact (template/checklist/snippet) for future projects.


### What You Cover in This Lesson
- **15.1 Capstone Design & Scoping**
- **15.2 Execution: Data, Modeling, Deployment & Documentation**
- **15.3 Teamwork, Communication & Stakeholder Management**
- **15.4 Final Presentation, Reflection & Next Steps**

### 15.1 Capstone Design & Scoping

**Core concepts:** Overview; Capstone Objectives & Competencies; Project Selection & Scoping; Linking to Earlier Lessons; Capstone Architecture Pre-Design Template; Milestone Plan and Definition of Done

In AI engineering programs, the capstone is the integration point where learners prove they can deliver a full project under realistic constraints, not just train isolated models. Strong capstones combine technical depth with planning discipline, communication, and practical trade-off decisions.

| Lesson | Skill signal expected in capstone evidence | |---|---| | 1 | clean code, modularity, testing, API hygiene | | 2 | mathematically sound metrics, optimization/statistics reasoning | | 3 | baseline modeling and rigorous model selection | | 4 | deep learning architecture/training decisions (when relevant) | | 5 | GenAI/LLM workflow design (prompting, RAG, generation quality controls) | | 6 | foundational MLOps/LLMOps lifecycle and deployment discipline | | 7 | agent workflow design, orchestration, and context handling | | 8 | ethical risk framing, governance awareness, and responsible AI controls | | 9 | specialization depth (RL/CV/NLP/domain-specific techniques) where applicable | | 10 | edge/robotics constraints and system realism where applicable | | 11 | product thinking, business impact framing, and research literacy | | 12 | advanced observability, evaluation loops, and operational controls | | 13 | safety, robustness, security, and guardrail strategies | | 14 | frontier-awareness and evidence-based technical judgment |

Theory source: [`15-ai-engineering-capstone-and-professional-practice/15-1-capstone-design-and-scoping/theory/15-1-capstone-design-and-scoping.md`](15-ai-engineering-capstone-and-professional-practice/15-1-capstone-design-and-scoping/theory/15-1-capstone-design-and-scoping.md)

**Representative notebook:** [`15-ai-engineering-capstone-and-professional-practice/15-1-capstone-design-and-scoping/notebooks/15-1-capstone-design-and-scoping-planner.ipynb`](15-ai-engineering-capstone-and-professional-practice/15-1-capstone-design-and-scoping/notebooks/15-1-capstone-design-and-scoping-planner.ipynb)

```python
import pandas as pd

ideas = pd.DataFrame(
    [
        {"idea": "Customer support RAG assistant", "impact": 5, "feasibility": 4, "data_availability": 4, "novelty": 3, "career_relevance": 5},
        {"idea": "Medical imaging classifier benchmark", "impact": 4, "feasibility": 3, "data_availability": 2, "novelty": 4, "career_relevance": 4},
        {"idea": "Fraud detection ML pipeline + API", "impact": 5, "feasibility": 5, "data_availability": 4, "novelty": 3, "career_relevance": 4},
        {"idea": "Agentic travel planner", "impact": 3, "feasibility": 2, "data_availability": 3, "novelty": 5, "career_relevance": 4},
    ]
)
ideas
```

```text
                                   idea  impact  feasibility  \
0        Customer support RAG assistant       5            4   
1  Medical imaging classifier benchmark       4            3   
2     Fraud detection ML pipeline + API       5            5   
3                Agentic travel planner       3            2   

   data_availability  novelty  career_relevance  
0                  4        3                 5  
1                  2        4                 4  
2                  4        3                 4  
3                  3        5                 4  
```

### 15.2 Execution: Data, Modeling, Deployment & Documentation

**Core concepts:** Overview; Data & Modeling; Deployment & MLOps/LLMOps Integration; Documentation & Artefacts; Implementation Playbook (Execution Template); Deployment and Documentation Rubric

Capstone execution should mirror real AI engineering workflows: data pipeline, modeling loop, deployment path, monitoring plan, and professional documentation. The objective is not just a model score; it is a defensible system narrative.

| Dimension | Weight | Minimum Bar | |---|---:|---| | Data and pipeline integrity | 20% | schema checks + reproducible transforms | | Modeling and evaluation quality | 25% | baseline + improvements + error analysis | | Deployment readiness | 20% | runnable serving/batch artifact with versioning | | Observability and operations | 15% | latency/error metrics + monitoring notes | | Documentation quality | 20% | setup, architecture, results, limitations, runbook |

Theory source: [`15-ai-engineering-capstone-and-professional-practice/15-2-execution-data-modeling-deployment-and-documentation/theory/15-2-execution-data-modeling-deployment-and-documentation.md`](15-ai-engineering-capstone-and-professional-practice/15-2-execution-data-modeling-deployment-and-documentation/theory/15-2-execution-data-modeling-deployment-and-documentation.md)

**Representative notebook:** [`15-ai-engineering-capstone-and-professional-practice/15-2-execution-data-modeling-deployment-and-documentation/notebooks/15-2-capstone-execution-checklists-and-skeleton.ipynb`](15-ai-engineering-capstone-and-professional-practice/15-2-execution-data-modeling-deployment-and-documentation/notebooks/15-2-capstone-execution-checklists-and-skeleton.ipynb)

```python
from pathlib import Path

repo_root = Path.cwd().resolve().parents[3]
capstone_root = repo_root / "projects" / "capstone-template"

print("Capstone scaffold:", capstone_root)
required = [
    "README.md",
    "configs/config.yaml",
    "data/ingest.py",
    "data/prepare.py",
    "model/train.py",
    "model/evaluate.py",
    "serve/api.py",
]
for rel in required:
    p = capstone_root / rel
    print(f"- {rel}: {'OK' if p.exists() else 'MISSING'}")
```

```text
Capstone scaffold: projects/capstone-template
- README.md: OK
- configs/config.yaml: OK
- data/ingest.py: OK
- data/prepare.py: OK
- model/train.py: OK
- model/evaluate.py: OK
- serve/api.py: OK
```

### 15.3 Teamwork, Communication & Stakeholder Management

**Core concepts:** Overview; Team Roles & Collaboration; Stakeholder Management; Communication Artefacts; Professional Practice & Ethics Integration; Communication Scoring Rubric

AI capstones are explicitly professional-practice environments, not only technical assignments. Programs increasingly evaluate teamwork, communication, stakeholder engagement, and ethical reasoning because these are core requirements in real AI delivery.

In practice, strong technical work can fail if team alignment and stakeholder communication are weak.

Theory source: [`15-ai-engineering-capstone-and-professional-practice/15-3-teamwork-communication-and-stakeholder-management/theory/15-3-teamwork-communication-and-stakeholder-management.md`](15-ai-engineering-capstone-and-professional-practice/15-3-teamwork-communication-and-stakeholder-management/theory/15-3-teamwork-communication-and-stakeholder-management.md)

**Representative notebook:** [`15-ai-engineering-capstone-and-professional-practice/15-3-teamwork-communication-and-stakeholder-management/notebooks/15-3-team-and-stakeholder-comms-playbook.ipynb`](15-ai-engineering-capstone-and-professional-practice/15-3-teamwork-communication-and-stakeholder-management/notebooks/15-3-team-and-stakeholder-comms-playbook.ipynb)

```python
import pandas as pd

sample_decisions = pd.DataFrame(
    [
        {
            "date": "2026-07-03",
            "decision": "Use batch scoring for MVP",
            "options": "online API, batch job",
            "chosen": "batch job",
            "rationale": "timeline fit",
            "owner": "MLOps lead",
        },
        {
            "date": "2026-07-10",
            "decision": "Model choice",
            "options": "xgboost, logistic regression",
...
```

```text
         date                   decision                       options  \
0  2026-07-03  Use batch scoring for MVP         online API, batch job   
1  2026-07-10               Model choice  xgboost, logistic regression   

      chosen                        rationale       owner  
0  batch job                     timeline fit  MLOps lead  
1    xgboost  better F1 at acceptable latency     ML lead  
```

### 15.4 Final Presentation, Reflection & Next Steps

**Core concepts:** Overview; Preparing Your Final Presentation; Reflection & Learning Extraction; Final Presentation Rubric; Reflection Scorecard Template; Next Steps After Capstone

The capstone finale is not only a demo; it is a professional synthesis of technical work, decision quality, and growth trajectory. A strong close demonstrates:

| Dimension | Weight | What “strong” looks like | |---|---:|---| | Problem clarity and relevance | 15% | clear stakeholders, baseline pain, bounded scope | | Technical narrative | 20% | architecture decisions and trade-offs are concrete | | Evidence and metrics | 20% | baseline vs final with limitations acknowledged | | Operational readiness | 15% | deployment, monitoring, rollback discussed | | Communication quality | 15% | concise structure, audience-appropriate language | | Reflection and next steps | 15% | honest lessons + realistic roadmap |

Theory source: [`15-ai-engineering-capstone-and-professional-practice/15-4-final-presentation-reflection-and-next-steps/theory/15-4-final-presentation-reflection-and-next-steps.md`](15-ai-engineering-capstone-and-professional-practice/15-4-final-presentation-reflection-and-next-steps/theory/15-4-final-presentation-reflection-and-next-steps.md)

**Representative notebook:** [`15-ai-engineering-capstone-and-professional-practice/15-4-final-presentation-reflection-and-next-steps/notebooks/15-4-capstone-presentation-and-reflection-planner.ipynb`](15-ai-engineering-capstone-and-professional-practice/15-4-final-presentation-reflection-and-next-steps/notebooks/15-4-capstone-presentation-and-reflection-planner.ipynb)

```python
import pandas as pd

reflection_prompts = [
    "What went better than expected?",
    "What did not go as planned?",
    "Which technical decision had biggest impact?",
    "Which communication decision changed outcomes?",
    "What would you change in version 2?",
    "How does this map to your target role?",
]

reflection_df = pd.DataFrame({"prompt": reflection_prompts, "your_notes": ["" for _ in reflection_prompts]})
reflection_df
```

```text
                                           prompt your_notes
0                 What went better than expected?           
1                     What did not go as planned?           
2    Which technical decision had biggest impact?           
3  Which communication decision changed outcomes?           
4             What would you change in version 2?           
5          How does this map to your target role?           
```


### Bridge to Next Lesson
You now have the core concepts and practical patterns from this lesson. Next, you will build on them in the following lesson with deeper abstraction, larger system scope, and stronger production tradeoff analysis.

[Back to Table of Contents](#table-of-contents)

## Glossary

- **Ablation Study**: Controlled experiment removing or changing one component to measure its impact on model performance.
- **Agentic AI**: AI systems that plan, call tools, maintain state, and execute multi-step tasks toward explicit goals.
- **Alignment**: Degree to which model objectives and behaviors match intended human goals and constraints.
- **Bagging**: Ensemble method that trains models on bootstrapped samples and aggregates predictions to reduce variance.
- **Bias-Variance Tradeoff**: Relationship where simpler models underfit (high bias) and overly complex models overfit (high variance).
- **Calibration**: How well predicted probabilities match observed outcome frequencies.
- **Causal Inference**: Reasoning about interventions and cause-effect, not just correlation patterns.
- **Cross-Validation**: Resampling method for estimating model generalization across multiple train/validation splits.
- **DPO**: Direct Preference Optimization, a method to align LLMs using preference pairs without full RL pipelines.
- **Data Drift**: Change in production input data distribution compared with training-time data.
- **ELBO**: Evidence Lower Bound optimized in VAEs to balance reconstruction quality and latent regularization.
- **Embeddings**: Dense vectors encoding semantic properties for retrieval, similarity, and downstream tasks.
- **F1 Score**: Harmonic mean of precision and recall, often used for imbalanced classification.
- **FSDP**: PyTorch Fully Sharded Data Parallel training strategy for large models and memory scaling.
- **GAN**: Generative Adversarial Network with generator and discriminator trained in a minimax game.
- **GraphRAG**: RAG architecture enhanced with graph/knowledge-graph structure for better multi-hop retrieval.
- **Guardrails**: Runtime policies and checks that constrain unsafe, out-of-scope, or invalid model behavior.
- **Inference Endpoint**: Deployed API or service interface used to obtain predictions from a trained model.
- **Inner Alignment**: Risk that a model develops internal objectives that differ from its intended training objective.
- **KL Divergence**: Measure of divergence between probability distributions; used in VAEs and probabilistic learning.
- **LoRA**: Low-Rank Adaptation: parameter-efficient fine-tuning by training low-rank adapter matrices.
- **MCP**: Model Context Protocol for exposing tools/resources to LLM applications in a structured way.
- **MLOps**: Practices for reliable ML lifecycle management: data, training, deployment, monitoring, governance.
- **Model Card**: Structured documentation of model purpose, data, metrics, risks, and limitations.
- **Multi-Agent System**: Multiple interacting agents that cooperate or compete in a shared environment.
- **Outer Alignment**: Correctness of objective specification relative to human intent.
- **PEFT**: Parameter-Efficient Fine-Tuning family (e.g., LoRA, adapters, prompt tuning).
- **PID Controller**: Feedback controller combining proportional, integral, and derivative terms for stable control.
- **Precision**: Fraction of predicted positives that are truly positive.
- **QLoRA**: Quantized LoRA fine-tuning approach combining 4-bit model loading with low-rank adapters.
- **RAG**: Retrieval-Augmented Generation: fetch relevant context then generate grounded answers.
- **RLHF**: Reinforcement Learning from Human Feedback for preference-aligned language model behavior.
- **Recall**: Fraction of actual positives correctly identified by the model.
- **Red Teaming**: Structured adversarial testing to discover vulnerabilities and unsafe behaviors.
- **SHAP**: Feature attribution method estimating local contribution of each feature to a prediction.
- **SLAM**: Simultaneous Localization and Mapping for robot position estimation and map construction.
- **SLO**: Service Level Objective defining reliability/performance targets for production systems.
- **Specification Gaming**: Model exploits proxy objective to maximize score while violating true intent.
- **Token Budget**: Constraint on prompt+response token usage, affecting cost, latency, and context size.
- **Zero Trust Security**: Security model requiring explicit verification of identity and permissions for each action.
