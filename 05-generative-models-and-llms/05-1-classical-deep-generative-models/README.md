# 5.1 Classical Deep Generative Models

This chapter introduces foundational deep generative model families:

- **VAEs** (probabilistic latent-variable models trained with ELBO)
- **GANs** (adversarial game between generator and discriminator)
- **Normalizing Flows** (invertible transformations with tractable likelihood)

## Why This Matters

These model families teach the core ideas behind generative modeling: latent variables, likelihood vs implicit modeling, and training instability tradeoffs. Even if you mainly build LLM apps, this builds intuition for generative behavior and failure modes.

## Key Terms (Plain English)

- **Latent variable**: a hidden representation learned by the model.
- **Likelihood**: how well the model explains observed data.
- **Mode collapse**: GAN generates limited variety (diversity failure).

## Start Here

1. Theory: `theory/05-1-classical-deep-generative-models.md`
2. Notebook: `notebooks/05-1-classical-deep-generative-models-vae-gan.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## What You Will Learn

- Formal differences between explicit-density and implicit generative models.
- ELBO terms and VAE latent-space intuition.
- GAN training dynamics, mode collapse, and practical mitigations.
- Business and risk trade-offs when using synthetic data.

## Verify Your Work

- Run the notebook from a clean kernel.
- Complete the exercises and write 5–10 lines comparing VAE vs GAN tradeoffs (stability, quality, control).
