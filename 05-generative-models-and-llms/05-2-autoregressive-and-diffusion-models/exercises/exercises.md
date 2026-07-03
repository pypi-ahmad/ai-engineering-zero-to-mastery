# Exercises: 5.2 Autoregressive & Diffusion Models

Most exercises here are offline and runnable with NumPy.

Optional prereq (only if you want to run Diffusers demos):

```bash
uv sync --frozen --extra genai
```

## Exercise 1: Decoding Strategies (Toy Distribution)

Given a probability vector over 10 tokens, implement:
- greedy decoding,
- top-k sampling,
- nucleus (top-p) sampling.

Expected outcome:
- you can see how the sampled tokens change as you change `k` and `p`.

## Exercise 2: Temperature Scaling

Implement temperature scaling on logits and show:
- low temperature makes distribution sharper,
- high temperature makes it flatter.

Expected outcome:
- entropy increases with temperature.

## Exercise 3: Bigram Language Model (Character-Level)

Train a character-level bigram model from a small text string and sample 200 characters.

Expected outcome:
- sampled text reflects local character statistics (even if nonsense).

## Exercise 4: Diffusion Forward Process (1D)

Implement a forward diffusion process on a 1D signal:
- start from a clean vector `x0`,
- add noise for timesteps `t=1..T` using a simple beta schedule.

Expected outcome:
- noise increases over time; variance grows.

## Exercise 5 (Optional): Diffusers Sanity Run

If you have network access and the `genai` extra installed, run a small diffusion pipeline.

Expected outcome:
- you can explain why diffusion inference can be slower than autoregressive decoding.

