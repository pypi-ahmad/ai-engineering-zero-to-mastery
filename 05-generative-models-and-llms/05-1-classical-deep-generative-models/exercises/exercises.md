# Exercises: 5.1 Classical Deep Generative Models

Prerequisite (recommended):

```bash
uv sync --frozen --extra dl
```

Use digits (offline) unless you explicitly choose a dataset that requires download.

## Exercise 1: VAE Loss Terms (Correctness)

Implement `vae_loss(logits, x, mu, logvar)` that returns:
- total loss,
- reconstruction term,
- KL term.

Expected outcome:
- losses are finite and shapes match.

## Exercise 2: Train VAE on Digits (Small)

Train a small VAE on digits for a few epochs and sample 32 images.

Expected outcome:
- sampled images are not pure noise after a few epochs (even if blurry).

## Exercise 3: GAN One-Step Sanity

Implement a tiny GAN (MLP generator/discriminator) and run:
- one discriminator update,
- one generator update.

Expected outcome:
- losses are finite; training loop runs end-to-end.

## Exercise 4: Diversity Metric (Mode Collapse Hint)

Compute a simple diversity score on generated samples:
- pixel-wise variance across the batch,
- or mean pairwise L2 distance.

Expected outcome:
- you can detect “all samples look the same” by a low diversity score.

## Exercise 5: Synthetic Data Risk Note

Write 8–12 lines answering:
- when synthetic data helps,
- how it can introduce bias/leakage,
- one validation gate you would require before production use.

