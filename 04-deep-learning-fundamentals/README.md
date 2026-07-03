# Lesson 4: Deep Learning Fundamentals

This lesson bridges classical ML into modern deep learning. It introduces neural network fundamentals, practical training patterns, core computer vision architectures, and sequence/attention concepts that prepare learners for Generative AI and LLM systems.

## Why This Matters

Deep learning is how modern systems handle high-dimensional data (images, text, audio). Even if you never train huge models, you need enough understanding to debug training behavior, interpret architectures, and use pretrained models safely.

## Expected Outcomes

- You can train a small neural network and interpret learning curves.
- You can explain why optimization stability matters (learning rates, gradients).
- You can explain what attention/transformers do at a high level (bridge to LLMs).

## Sub-lessons

1. `4.1 Neural Networks & Backpropagation`
2. `4.2 Training Deep Neural Networks`
3. `4.3 Convolutional Neural Networks & Computer Vision`
4. `4.4 Sequence Models, Attention & Transformers`

## How to Use This Lesson

1. Start with 4.1 and 4.2 to build optimization and architecture intuition.
2. Apply those patterns in 4.3 (vision) and 4.4 (sequence + transformer bridge).
3. Use project prompts and practice exercises at the end of each chapter/notebook.

## Verify Your Work

- Install the deep learning extra when you reach this lesson:

```bash
uv sync --frozen --extra dl
```

- Run at least one notebook from a clean kernel and complete the `exercises/` for 4.1 and 4.2 (minimum recommended).

## Bridge from Lesson 3
**Why this follows:** After classical ML, deep learning is the next step when feature engineering plateaus or data is high-dimensional (images, text, sequences).

**You should already know:** supervised learning basics, train/validation/test discipline, and core evaluation metrics.

**What you will do next:** move from linear/tree models to neural networks, stable training, CNNs, and transformer foundations.

## Bridge to Lesson 5
Lesson 5 builds directly on 4.4 by shifting from sequence fundamentals to generative systems: VAEs/GANs, autoregressive and diffusion models, LLM prompting, RAG, and agents.
