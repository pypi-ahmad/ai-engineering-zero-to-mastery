# Overview

Autoregressive and diffusion models are two dominant paradigms in modern generative AI.

- **Autoregressive (AR) models** generate outputs one token/step at a time by factorizing joint probability into conditionals.
- **Diffusion models** learn to reverse a progressive noising process, generating data by iterative denoising.

Both can model highly complex distributions, but they differ in objective, sampling behavior, and deployment trade-offs.

Historical arc (high-level):

- AR era milestones: n-gram models, RNN language models, WaveNet, PixelRNN/PixelCNN, Transformer LMs.
- Diffusion era milestones: DDPM and latent diffusion systems used in modern image generation pipelines (e.g., Stable Diffusion family).

Text diagram:

- AR: "left to right" generation where each step conditions on prior outputs.
- Diffusion: "noise to signal" generation where each step removes estimated noise.

## Why this distinction matters

For production use, AR vs diffusion decisions affect:

- latency profile (token-by-token vs many denoise steps),
- controllability and prompt conditioning,
- infrastructure costs,
- quality and mode coverage characteristics.

# Autoregressive Models

The fundamental AR factorization for sequence $x_{1:T}$ is:

$$
p(x_{1:T}) = \prod_{t=1}^{T} p(x_t \mid x_{<t}).
$$

Training often maximizes conditional log-likelihood via teacher forcing:

$$
\max_\theta \sum_{t=1}^{T} \log p_\theta(x_t \mid x_{<t}).
$$

## Core Intuition

An AR model learns "next-step prediction" repeatedly. If next-token predictions are good across contexts, iterative sampling can produce coherent full outputs.

## Examples

- **Language models**: GPT-style text generation.
- **PixelRNN/PixelCNN**: model image pixels in fixed ordering.
- **WaveNet-style audio models**: sample-level or chunk-level autoregressive generation.

## Sampling One Step at a Time

At inference:

1. Start with prompt/context.
2. Predict distribution over next token.
3. Sample or choose token by decoding strategy.
4. Append token and repeat until stop condition.

Decoding controls quality-diversity trade-offs:

- Greedy decoding: deterministic, can be repetitive.
- Beam search: stronger likelihood, sometimes generic outputs.
- Top-k / nucleus (top-p): better diversity with controllable randomness.

## Practical Strengths and Limits

Strengths:

- Straightforward likelihood training.
- Strong language modeling and sequential coherence.

Limits:

- Inherently sequential sampling can be slow for long outputs.
- Error propagation: early mistakes influence later tokens.

# Diffusion Models

Diffusion models define:

1. A **forward process** that gradually corrupts data with noise.
2. A **reverse process** learned by a neural network to denoise step-by-step.

## Forward Process (DDPM-style)

For timestep $t$:

$$
q(x_t \mid x_{t-1}) = \mathcal{N}(\sqrt{1-\beta_t}x_{t-1},\, \beta_t I),
$$

with a schedule $\{\beta_t\}_{t=1}^T$.

Closed form:

$$
q(x_t \mid x_0) = \mathcal{N}(\sqrt{\bar\alpha_t}x_0,\, (1-\bar\alpha_t)I),
$$

where $\alpha_t = 1-\beta_t$ and $\bar\alpha_t = \prod_{s=1}^t \alpha_s$.

## Reverse Process

Learn model $\epsilon_\theta(x_t, t, c)$ (optionally conditioned on prompt/context $c$) that predicts noise. Reverse updates progressively recover clean sample from Gaussian noise.

Intuitive picture:

- Forward: image turns to static.
- Reverse: model learns which parts of static correspond to meaningful structure.

## Score-based View (high-level)

Diffusion and score-based models are closely related; both learn gradients of log density (scores) or equivalent denoising objectives. This underpins many modern sampler variants.

## Why Diffusion Outputs Are Often High Quality

Iterative denoising can model multi-modal distributions with strong fidelity and diversity, often with fewer mode-collapse issues than adversarial training.

## Main Limitation: Sampling Cost

Classic diffusion requires many denoising steps, increasing latency and compute cost at inference. Practical systems use improved samplers, distillation, and latent-space generation to reduce cost.

# Applications

## Text

Autoregressive decoders remain dominant for long-form text generation, coding assistants, and chat completion.

## Audio

WaveNet-like and diffusion-based audio generation are used for speech synthesis, music, and audio restoration.

## Images

Latent diffusion systems power modern creative tools: concept art, ad creatives, product mockups, and design ideation.

## Multimodal Systems

Hybrid stacks combine AR decoders with diffusion image generators and retrieval/tool modules in one product workflow.

# Common Pitfalls

1. **Ignoring decoding policy in AR evaluation**
   - Model quality depends heavily on generation strategy (temperature, top-k/top-p).
2. **Underestimating diffusion inference cost**
   - Throughput and GPU memory planning often break late in deployment.
3. **Training objective mismatch with business metric**
   - Likelihood improvements may not map to human preference or downstream utility.
4. **Safety blind spots in open generation**
   - Add content filters, guardrails, and human review for sensitive domains.
5. **Data licensing and provenance issues**
   - Generative systems require strict tracking of training-data permissions and usage rights.

# Business Case Studies & Exceptions

## Case Study 1: Marketing Creative Generation

Scenario:

- A growth team needs 500 weekly creative variations for regional campaigns.

Architecture choice:

- Diffusion for image generation (high visual quality).
- AR text model for ad copy variants.
- Human curation and brand-safety filters before launch.

Benefits:

- Lower content production turnaround.
- Faster A/B cycle for creatives.

Risks/Exceptions:

- Brand inconsistency without strong prompting/templates.
- Potential copyright/style concerns.
- Latency spikes under campaign bursts.

Operational pattern:

- Pre-generate candidate banks offline.
- Rank with offline quality model + policy checks.
- Route only top candidates to human reviewers.

## Case Study 2: Synthetic Scenario Generation for Simulation

Scenario:

- Autonomous perception team needs rare weather/lighting conditions.

Architecture choice:

- Diffusion-based generation for photorealistic variations.
- AR metadata/text generation for scenario descriptions.

Benefits:

- Improved coverage of rare corner cases.
- Reduced cost of collecting rare real-world footage.

Risks/Exceptions:

- Simulator-to-reality gap remains.
- Synthetic artifacts may overfit downstream models.

Mitigation:

- Always evaluate on real-world holdout slices.
- Track per-condition error reduction, not only aggregate metrics.

# Interview Questions & Answers

1. **Q: What is an autoregressive model?**
   **A:** A model that factorizes a joint distribution into conditional next-step probabilities and generates sequentially.

2. **Q: Why are autoregressive models naturally suited for text?**
   **A:** Language is sequential and causal in many tasks, matching token-by-token conditional prediction.

3. **Explain diffusion model intuition simply.**
   Corrupt training data with noise, then train a model to reverse corruption; generation starts from noise and iteratively denoises.

4. **Q: Why are diffusion models often slow to sample?**
   **A:** They may require tens to hundreds of iterative denoising steps per sample.

5. **Q: What is the forward diffusion process?**
   **A:** A fixed Markov process that progressively adds Gaussian noise according to a variance schedule.

6. **Q: What does the diffusion network predict?**
   **A:** Usually the added noise (or equivalent parameterization such as clean sample or velocity).

7. **Q: How does AR sampling differ from diffusion sampling?**
   **A:** AR appends one token per step; diffusion repeatedly refines a noisy sample toward clean data.

8. **Q: When might AR be preferred over diffusion?**
   **A:** Long-form text/code generation where causal decoding and tokenizer-based modeling are mature and efficient.

9. **Q: When might diffusion be preferred over AR?**
   **A:** High-fidelity image generation tasks where quality/diversity are critical.

10. **Q: What are common AR decoding controls?**
   **A:** Temperature, top-k, top-p (nucleus), repetition penalties, max tokens.

11. **Q: How do you reduce diffusion latency in practice?**
   **A:** Fewer-step samplers, latent diffusion, optimized schedulers, distillation, and hardware-specific acceleration.

12. **Q: Can diffusion models overfit?**
   **A:** Yes, especially with narrow datasets; monitor memorization and near-duplicate generations.

13. **Q: What business risk is unique to generative creative systems?**
   **A:** Brand and policy violations at scale if output controls and review workflows are weak.

14. **Q: How do you evaluate model choice between AR and diffusion?**
   **A:** Use task-specific quality metrics plus latency/cost/SLA constraints and human preference testing.

15. **Q: What is classifier-free guidance (high level)?**
   **A:** A conditioning technique in diffusion models that trades diversity for stronger prompt alignment.
# Further Reading & Sources

- Stanford CS236 (deep generative model curriculum): https://deepgenerativemodels.github.io/
- UCLA CS261 listing (deep learning/generative academic context): https://catalog.registrar.ucla.edu/course/2024/comsci261
- Hugging Face Diffusers Stable Diffusion API docs: https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/text2img
- Ho et al., Denoising Diffusion Probabilistic Models (2020): https://arxiv.org/abs/2006.11239
- van den Oord et al., WaveNet (2016): https://arxiv.org/abs/1609.03499
- PixelCNN (2016): https://arxiv.org/abs/1606.05328
