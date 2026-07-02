# Overview

Generative modeling asks a different question than classical predictive modeling. In supervised learning, we typically learn a mapping from input to label, such as $f(x) \rightarrow y$. In generative modeling, we try to learn the data-generating process itself, i.e., a model that can produce realistic samples from the same distribution as the training data.

Formally, if real data comes from an unknown distribution $p_{\text{data}}(x)$, a generative model aims to approximate either:

- the density directly: $p_\theta(x) \approx p_{\text{data}}(x)$,
- or the sampling mechanism: $x = G_\theta(z)$ where $z \sim p(z)$.

Two broad families are useful to separate early:

1. **Explicit density models**: they define a tractable (or approximately tractable) likelihood $p_\theta(x)$.
Examples: VAEs (optimize a lower bound to log-likelihood), normalizing flows (exact likelihood by change of variables).
2. **Implicit models**: they define a sampling procedure but often do not provide tractable $p_\theta(x)$.
Examples: GANs.

A useful mental model:

- A classifier tells you *which class* an image likely belongs to.
- A generative model tells you *what valid images from this domain look like*.

Core use cases include:

- **Image synthesis**: creating new images from learned style/content distributions.
- **Data augmentation**: increasing training diversity where labeled data is expensive.
- **Anomaly detection**: low-likelihood or high-reconstruction-error samples are suspicious.
- **Privacy-preserving synthetic data**: sharing statistically similar data when raw records are sensitive.

Text diagram for orientation:

- Imagine real data points as a dense cloud in high-dimensional space.
- A good generative model learns a manifold that overlaps this cloud.
- Different model classes reach this goal via different optimization objectives.

## Density Models vs Implicit Models in Practice

If your application requires calibrated likelihoods, uncertainty estimates, or anomaly scoring, explicit-density families (VAEs, flows) are often easier to reason about. If your highest priority is perceptual sample quality, GAN-style adversarial training can produce sharper outputs but is harder to stabilize and evaluate.

## Why This Matters for AI Engineers

In production, model choice is not only about benchmark quality. It is about:

- Training stability and debugging cost.
- Hardware and latency budgets.
- Explainability and risk controls.
- Compliance constraints around synthetic data usage.

# Variational Autoencoders (VAEs)

A **latent variable model** introduces hidden variables $z$ that explain observed data $x$:

$$
p_\theta(x) = \int p_\theta(x, z)\, dz = \int p_\theta(x\mid z)p(z)\, dz.
$$

A VAE combines neural networks with variational inference:

- **Encoder** (inference network): $q_\phi(z\mid x)$ approximates posterior $p_\theta(z\mid x)$.
- **Decoder** (generative network): $p_\theta(x\mid z)$ maps latent codes to data space.
- **Prior**: usually $p(z)=\mathcal{N}(0, I)$.

## Probabilistic View and ELBO

Directly maximizing $\log p_\theta(x)$ is intractable in most deep latent models. VAEs maximize the Evidence Lower BOund (ELBO):

$$
\log p_\theta(x) \geq \mathbb{E}_{q_\phi(z\mid x)}[\log p_\theta(x\mid z)] - D_{\mathrm{KL}}\big(q_\phi(z\mid x)\;\|\;p(z)\big).
$$

Interpretation:

- **Reconstruction term**: encourages decoder to reconstruct $x$ from $z$.
- **KL term**: regularizes latent codes to stay close to prior, enabling smooth sampling.

Intuition diagram in text:

- If reconstruction dominates too much, latents may memorize training points.
- If KL dominates too much, decoder ignores latent signal (posterior collapse).
- Good training balances both terms.

A common practical variant is the $\beta$-VAE objective:

$$
\mathcal{L}_{\beta\text{-VAE}} = \mathbb{E}_{q_\phi(z\mid x)}[\log p_\theta(x\mid z)] - \beta\, D_{\mathrm{KL}}(q_\phi(z\mid x)\|p(z)).
$$

- $\beta > 1$: stronger disentanglement pressure, often weaker reconstruction.
- $\beta < 1$: stronger reconstruction fidelity, often less structured latent space.

## Reparameterization Trick

Sampling $z \sim q_\phi(z\mid x)$ blocks naive backpropagation. VAEs use:

$$
z = \mu_\phi(x) + \sigma_\phi(x) \odot \epsilon,\quad \epsilon \sim \mathcal{N}(0,I).
$$

This expresses stochasticity in $\epsilon$ while keeping $\mu,\sigma$ differentiable wrt parameters.

## Strengths and Weaknesses

Strengths:

- Stable optimization objective.
- Continuous, often semantically meaningful latent spaces.
- Natural fit for interpolation and anomaly scoring.

Weaknesses:

- Pixel-level reconstruction losses can lead to blurry images.
- Tuning KL/reconstruction balance is delicate.

# Generative Adversarial Networks (GANs)

GANs define a two-player game between:

- **Generator** $G_\theta(z)$: transforms latent noise into synthetic samples.
- **Discriminator** $D_\psi(x)$: predicts whether input is real or generated.

Classic minimax objective:

$$
\min_G \max_D\; \mathbb{E}_{x\sim p_{\text{data}}}[\log D(x)] + \mathbb{E}_{z\sim p(z)}[\log(1 - D(G(z)))].
$$

In practice, non-saturating generator losses and modern stabilizers are common.

## Intuition

GAN training is an adversarial feedback loop:

1. Discriminator gets better at spotting fakes.
2. Generator gets gradients that push fakes toward realism.
3. Ideally, generated distribution approaches real distribution.

The reason GAN outputs can look sharp: discriminator-based losses focus on perceptual realism rather than per-pixel averaging.

## Common Instabilities

### Mode Collapse

**Mode collapse**: generator outputs limited modes (low diversity), e.g., similar digits/faces repeatedly.

Why it happens:

- Generator can exploit discriminator weaknesses.
- Adversarial game is non-convex/non-stationary.

Typical mitigations:

- Architectural constraints (DCGAN heuristics).
- Wasserstein objectives + gradient penalty (WGAN-GP).
- Spectral normalization.
- Minibatch discrimination.
- Better training ratios and learning-rate schedules.

### Oscillation and Non-Convergence

Because both players update simultaneously, training can oscillate or diverge. This makes experiment tracking and checkpoint discipline essential.

# Normalizing Flows (high-level)

A normalizing flow transforms a simple base distribution into complex data distribution via invertible mappings.

Let $z_0 \sim p_0(z)$ and define invertible transforms:

$$
z_k = f_k \circ f_{k-1} \circ \dots \circ f_1(z_0),\quad x=z_k.
$$

By change of variables:

$$
\log p_X(x) = \log p_0(z_0) - \sum_{i=1}^{k} \log \left|\det \frac{\partial f_i}{\partial z_{i-1}}\right|.
$$

Key idea: choose transforms with tractable Jacobian determinants.

Benefits:

- Exact likelihood (unlike GANs).
- Exact latent-variable inversion (unlike many implicit models).

Trade-offs:

- Invertibility constraints limit architecture design.
- Computational overhead for high-dimensional data can be significant.

Common flow families (high-level): RealNVP, Glow, Masked Autoregressive Flow.

# Applications & Trade-offs

## Choosing Between VAEs, GANs, and Flows

Use this practical decision guide:

1. **Need stable training + latent arithmetic/interpolation + anomaly scoring**
   - Prefer VAE variants.
2. **Need highest perceptual realism in image synthesis**
   - Prefer GAN variants if you can absorb instability/debug cost.
3. **Need exact likelihood and invertible mappings**
   - Prefer flows.

## By Data Modality

- **Images**: GANs and diffusion dominate realism; VAEs still useful for representation learning.
- **Text**: pure GANs are less common because discrete sampling complicates gradients.
- **Tabular/time-series**: VAEs and flow-like models are often easier to validate and control.

## Engineering Trade-offs Table (textual)

- VAE: +stable, +latent structure, -sometimes blurry.
- GAN: +sharp outputs, -unstable, -hard metrics.
- Flow: +exact likelihood, +invertible, -architecture constraints.

# Common Pitfalls

1. **Treating visual quality as the only metric**
   - Use multiple metrics: FID/KID (images), coverage/diversity, task-specific utility.
2. **Ignoring data quality**
   - Generative models amplify training artifacts and biases.
3. **Weak validation for synthetic data utility**
   - Evaluate downstream task performance, not only sample aesthetics.
4. **No leakage checks in synthetic tabular data**
   - Check nearest-neighbor leakage, membership inference risk, and attribute disclosure.
5. **Overfitting discriminator in GAN training**
   - If discriminator dominates, generator gradients vanish.

# Business Case Studies & Exceptions

## Case Study 1: Synthetic Healthcare Data for Model Development

Scenario:

- A hospital wants to let vendors prototype readmission models without sharing raw PHI.

Pattern:

1. Train a tabular VAE/flow on de-identified internal data.
2. Generate synthetic cohorts.
3. Evaluate utility with downstream model parity tests.
4. Run privacy risk checks (record linkage, re-identification heuristics).

Benefits:

- Faster partner collaboration.
- Reduced direct exposure of sensitive records.

Risks/Exceptions:

- Synthetic data is not automatically private.
- Rare disease patterns may be underrepresented.
- Regulatory teams may still require strict controls.

Code pattern concept:

- `fit_generator(train_df)`
- `synthetic_df = sample(n=...)`
- `assert downstream_auc_gap < threshold`
- `assert privacy_risk_score < threshold`

## Case Study 2: Industrial Defect Detection with Synthetic Augmentation

Scenario:

- A manufacturer has only a few hundred defective examples.

Pattern:

1. Train a GAN or diffusion model on defect patches.
2. Generate diverse but realistic defect variants.
3. Combine with real data for classifier training.
4. Measure false-negative reduction by defect subtype.

Benefits:

- Better recall on rare defects.
- Reduced manual data collection cycles.

Risks/Exceptions:

- Unrealistic textures can hurt generalization.
- Synthetic distribution shift can bias model toward artifacts.

Guardrails:

- Human QA on generated samples.
- Holdout set must remain real-only.
- Track performance separately on real vs synthetic-influenced slices.

# Interview Questions & Answers

1. **What is a latent variable model?**
   A model that explains observed data $x$ using hidden variables $z$, usually via $p(x)=\int p(x\mid z)p(z)dz$.

2. **Explain VAE intuition in one minute.**
   A VAE learns a compressed probabilistic representation of data and reconstructs from it, while regularizing latents toward a known prior for smooth sampling.

3. **What does the ELBO optimize?**
   A lower bound to log-likelihood: reconstruction quality minus KL regularization between approximate posterior and prior.

4. **Why do VAEs sometimes produce blurry images?**
   Reconstruction losses (e.g., pixel-wise) can average plausible outputs, reducing sharp high-frequency detail.

5. **What is mode collapse in GANs?**
   The generator maps many latent inputs to similar outputs, reducing diversity despite possibly fooling discriminator locally.

6. **How do GANs conceptually differ from VAEs?**
   GANs learn via adversarial game and implicit sampling; VAEs optimize probabilistic evidence lower bound with explicit latent inference.

7. **When would you choose a flow over GAN/VAE?**
   When exact likelihood and invertibility are important (density estimation, exact latent inference, some anomaly tasks).

8. **Why are GANs hard to train?**
   Non-stationary two-player optimization, sensitivity to architecture and hyperparameters, and unstable gradient dynamics.

9. **What is the role of the prior in VAE?**
   It regularizes latent organization and enables sampling by drawing $z$ from known distribution (usually standard normal).

10. **Name practical GAN stabilization methods.**
    Wasserstein loss with gradient penalty, spectral normalization, careful architecture design, balanced update schedules.

11. **How would you evaluate a generative model in production?**
    Combine perceptual/diversity metrics, downstream task utility, privacy checks, and bias/slice analysis.

12. **Can synthetic data replace real data entirely?**
    Usually no. It augments or unlocks early experimentation; final validation should rely heavily on real representative data.

13. **What is posterior collapse?**
    In VAEs, decoder ignores latent code and approximate posterior matches prior too closely, reducing useful latent information.

14. **Why are explicit likelihoods useful?**
    They provide density-based scoring for anomaly detection and clearer probabilistic interpretation.

15. **What is a practical first baseline for image generation projects?**
    Start with a small VAE for stability/diagnostics, then move to GAN/diffusion if quality targets demand it.

# Further Reading & Sources

- Stanford CS236: Deep Generative Models (course structure and topic sequencing): https://deepgenerativemodels.github.io/
- UCLA CS261 (deep learning / generative content context): https://catalog.registrar.ucla.edu/course/2024/comsci261
- PyTorch DCGAN tutorial (implementation patterns): https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html
- Goodfellow et al., GANs (2014): https://arxiv.org/abs/1406.2661
- Kingma & Welling, Auto-Encoding Variational Bayes (2013): https://arxiv.org/abs/1312.6114
- Dinh et al., Real NVP (2016): https://arxiv.org/abs/1605.08803
