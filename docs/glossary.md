# Glossary (Beginner-Friendly)

Short definitions for terms used throughout this curriculum. If a term still feels fuzzy, search for it in the relevant lesson’s theory chapter.

## Core ML / Data Terms

- **Artifact**: a saved output you can reproduce or deploy later (model file, metrics JSON, dataset snapshot, prompt template).
- **Baseline**: the simplest model/system you can ship first to set a reference performance level.
- **Data leakage**: information from the future or target variable accidentally sneaks into training, making metrics look better than reality.
- **Feature**: an input signal used by a model (a column like `age`, or an engineered value like `avg_spend_last_30d`).
- **Train/validation/test split**: separate data for fitting the model, tuning decisions, and final evaluation.
- **Metric**: a numeric score for quality (accuracy, F1, ROC AUC, latency, cost per request).
- **Overfitting**: model performs well on training data but poorly on new data.

## Deep Learning Terms

- **Backpropagation**: computing gradients so parameters can be updated to reduce loss.
- **Gradient**: how much a small parameter change changes the loss.
- **Loss**: the objective you minimize during training (cross entropy, MSE).
- **Transformer**: a neural network architecture built around attention, widely used for language.

## GenAI / LLM Terms

- **LLM**: large language model, trained to predict tokens (pieces of text).
- **Prompt**: instructions and context you send to an LLM.
- **RAG**: retrieval-augmented generation; retrieve relevant documents and include them in the prompt to ground answers.
- **Embedding**: a numeric vector representation of text/images used for similarity search.
- **Hallucination**: fluent output that is not supported by the provided evidence or reality.
- **Prompt injection**: an attack where untrusted text tries to override system instructions or tool policies.

## Production / Ops Terms

- **Serving**: making a model available to other systems via an API or batch job.
- **Inference**: using a trained model to produce predictions on new inputs.
- **Latency**: time to respond; often measured at p50/p95/p99 percentiles.
- **Drift**: input data or performance changes over time compared to training conditions.
- **Regression test / gate**: a check that blocks changes if quality drops below an agreed threshold.
- **Circuit breaker**: a safety mechanism that stops or degrades a system when a dependency fails (e.g., retrieval returns no docs).

