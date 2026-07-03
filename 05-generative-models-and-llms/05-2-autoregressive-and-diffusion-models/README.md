# 5.2 Autoregressive & Diffusion Models

This chapter compares two dominant modern generation paradigms:

- **Autoregressive models**: generate sequentially via conditional probabilities.
- **Diffusion models**: generate by iteratively denoising noisy samples.

## Why This Matters

Autoregressive and diffusion models are the backbone of modern text and image generation. Understanding their sampling tradeoffs helps you reason about latency, controllability, and quality in production.

## Key Terms (Plain English)

- **Decoding**: how you sample tokens (greedy, beam, top-k, nucleus).
- **Denoising**: diffusion generation step that refines a sample.
- **Sampling temperature**: how random outputs are.

## Start Here

1. Theory: `theory/05-2-autoregressive-and-diffusion-models.md`
2. Notebook: `notebooks/05-2-autoregressive-and-diffusion-models-demo.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## What You Will Learn

- Joint distribution factorization and decoding strategies for AR models.
- Forward/reverse diffusion intuition and sampling implications.
- Why diffusion quality is often strong but inference can be expensive.
- Where each family fits in production workloads.

## Verify Your Work

- Run the notebook from a clean kernel.
- Complete the exercises and compare two decoding settings (quality vs diversity vs determinism).
