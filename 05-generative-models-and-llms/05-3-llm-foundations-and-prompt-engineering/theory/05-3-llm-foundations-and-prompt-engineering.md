# Overview

A **Large Language Model (LLM)** is a neural sequence model, usually Transformer-based, trained on large text corpora to predict tokens and learn broad linguistic/statistical structure.

At a high level, LLM development has two major phases:

1. **Pre-training**: learn general language/modeling capability from large-scale unlabeled text using next-token or related objectives.
2. **Adaptation**: align and specialize with instruction tuning, preference optimization, task fine-tuning, and retrieval/tool augmentation.

Connection to Transformer fundamentals (from Lesson 4):

- Self-attention enables context-dependent token representations.
- Stacked blocks increase abstraction depth.
- Positional encoding and causal masking enforce sequence semantics for decoder-only LMs.

Formal next-token objective:

$$
\max_\theta \sum_{t=1}^{T} \log p_\theta(x_t \mid x_{<t}).
$$

This simple objective, scaled with data/compute/model size, leads to emergent capabilities such as summarization, translation, coding assistance, and instruction following when combined with alignment methods.

## Pre-training vs Fine-tuning

- **Pre-training** gives broad priors and language competence.
- **Fine-tuning / instruction tuning** adapts model behavior to desired tasks, formats, safety constraints, or domains.

Rule of thumb for practitioners:

- Start with prompting + retrieval.
- Move to fine-tuning when repeated prompt engineering cannot meet quality/latency/cost targets.

# LLM Capabilities & Limitations

## Capabilities

1. **In-context learning**
   - The model adapts behavior from examples within the prompt without parameter updates.
2. **Reasoning-like behavior**
   - Structured prompts can improve step decomposition, planning, and consistency.
3. **Code generation and transformation**
   - Useful for scaffolding, migration, tests, and refactoring assistance.
4. **Style and format control**
   - Output schema, tone, and response length can be guided with clear constraints.

## Limitations

1. **Hallucinations**
   - Confident but incorrect outputs when knowledge is missing or prompts are ambiguous.
2. **Context window limits**
   - Very long contexts can degrade retrieval/usefulness despite larger windows.
3. **Bias and safety issues**
   - Models can reflect harmful patterns from training data.
4. **Non-determinism**
   - Sampling settings and model updates can change outputs.
5. **Weak calibration**
   - Verbal confidence does not reliably match factual correctness.

Practical implication: LLMs should be treated as probabilistic generators, not authoritative databases.

# Prompt Engineering

Prompt engineering is the disciplined design of model inputs to reliably elicit desired outputs.

A robust prompt usually defines:

- **Task**: what to do.
- **Context**: relevant background/evidence.
- **Constraints**: format, style, length, do/don't rules.
- **Examples**: demonstrations of expected behavior.
- **Evaluation hooks**: checks for completeness/correctness.

## Core Patterns

### Instruction + Role + Constraints

Example structure:

- Role: "You are a financial analyst."
- Task: "Summarize quarterly performance."
- Constraints: "Return JSON with keys revenue, margin, risks."

### Few-shot Prompting

Provide exemplar input-output pairs that define desired transformation behavior. Useful when task requirements are subtle (tone, schema, domain-specific mapping rules).

### Chain-of-Thought and Structured Reasoning Prompts

Asking for intermediate reasoning can improve some tasks, but production systems should avoid exposing sensitive internal rationale when unnecessary. A safer pattern is asking for concise justifications and verifiable steps.

### Delimiter and Grounding Patterns

Wrap external context in clear delimiters and instruct model to rely only on provided evidence to reduce hallucination.

## Controlling Style, Format, and Reliability

Levers:

- Temperature/top-p.
- Explicit schema templates.
- Self-check instructions ("verify against source snippets").
- Post-processing validators (JSON schema, regex, business rules).

Prompt anti-patterns:

- Vague objectives.
- Contradictory instructions.
- Overloaded context with no prioritization.

# Fine-tuning & Parameter-Efficient Methods

## Instruction Tuning

Supervised fine-tuning on instruction-response pairs teaches task following and response style alignment.

## Parameter-Efficient Fine-Tuning (PEFT)

PEFT methods update only a small subset of parameters, reducing GPU memory and training cost.

### LoRA (Low-Rank Adaptation)

LoRA injects low-rank matrices into weight updates:

$$
W' = W + \Delta W,\quad \Delta W = A B,
$$

where $A\in\mathbb{R}^{d\times r}, B\in\mathbb{R}^{r\times k}, r\ll\min(d,k)$.

Benefits:

- Lower memory footprint.
- Faster iteration for domain adaptation.
- Easy swapping of adapters for multi-domain deployment.

### Adapters (high-level)

Small trainable modules inserted between layers; base model remains mostly frozen.

When to choose PEFT:

- Limited compute budget.
- Need multiple domain-specific variants.
- Need faster retraining cycles.

# Evaluation of LLMs

No single metric is sufficient.

## Automatic Metrics (task-dependent)

- Perplexity (language modeling proxy).
- Exact match / F1 for QA extraction tasks.
- ROUGE/BLEU-like overlap metrics for summarization/translation (with caveats).

## Human Evaluation

Rate dimensions such as:

- factuality,
- completeness,
- helpfulness,
- style compliance,
- safety.

## System-Level Evaluation

For real applications, evaluate end-to-end outcomes:

- Deflection rate in support bots.
- Resolution quality.
- Hallucination incidence.
- Latency and cost per successful task.

## Continuous Evaluation in Production

- Curate benchmark suites from real failure cases.
- Run regression tests on prompt/model changes.
- Track drift after model/version updates.

# Business Case Studies & Exceptions

## Case Study 1: Customer Support Assistant

Scenario:

- Enterprise support team wants faster first-response quality.

Pattern:

1. Prompted LLM drafts answer.
2. Retrieval injects policy/product docs.
3. Agent enforces citation requirement.
4. Human escalation for high-risk requests.

Business impact:

- Reduced average handling time.
- Better consistency across agents.

Exceptions/Risks:

- Policy hallucinations can create compliance issues.
- Strict guardrails required for legal/financial/medical content.

## Case Study 2: Developer Copilot for Internal Codebase

Scenario:

- Engineering org needs faster onboarding and code explanations.

Pattern:

- Retrieval over internal docs/code snippets.
- Prompt templates for refactor/test/document modes.
- Quality gate via static checks and tests.

Benefits:

- Higher dev velocity for repetitive tasks.
- Better standardization of patterns.

Exceptions/Risks:

- Suggested code may include subtle bugs.
- Must validate against current repository conventions.

## When LLMs Are a Bad Fit

- Hard real-time systems with strict deterministic guarantees.
- High-stakes domains requiring near-zero hallucination tolerance without human oversight.
- Tasks where a simple rules engine already achieves target quality at lower cost.

# Interview Questions & Answers

1. **What is an LLM?**
   A large Transformer-based language model trained to predict tokens and adapted for downstream instructions/tasks.

2. **Difference between pre-training and fine-tuning?**
   Pre-training learns general language representations from large unlabeled corpora; fine-tuning specializes behavior for tasks/domains.

3. **What is in-context learning?**
   Task adaptation from prompt examples without updating model weights.

4. **Why does prompt engineering matter even with strong models?**
   Prompt structure strongly affects reliability, formatting, and factual grounding.

5. **What causes hallucinations?**
   Missing grounding, ambiguous prompts, weak retrieval, and probabilistic generation under uncertainty.

6. **How do few-shot prompts help?**
   They demonstrate expected mapping patterns, reducing ambiguity for task behavior.

7. **What is LoRA?**
   A PEFT method that learns low-rank adaptation matrices while freezing most base model weights.

8. **When should you choose fine-tuning over prompting?**
   When repeated prompt tuning cannot achieve quality/cost/latency targets or when consistent specialized behavior is required.

9. **How do you evaluate an LLM-powered assistant?**
   Combine offline benchmarks, human ratings, hallucination audits, latency/cost tracking, and business KPIs.

10. **Why is temperature important?**
    It controls sampling randomness: lower for determinism, higher for diversity.

11. **What is instruction tuning?**
    Supervised tuning on instruction-response pairs to improve task following and helpfulness.

12. **How do you reduce unsafe outputs?**
    Safety-aligned prompts, policy filters, refusal handling, retrieval constraints, and human review for sensitive cases.

13. **What are limitations of perplexity as a metric?**
    It measures predictive fit, not factuality, usefulness, or safety in downstream tasks.

14. **What is a practical LLM baseline strategy in production?**
    Start with prompt + retrieval + deterministic output schema and add fine-tuning only if measurable gaps remain.

15. **How do you control format reliability?**
    Use explicit schema instructions, examples, and strict post-parse validation with retries.

16. **Why can long context hurt?**
    Relevant evidence may be diluted; retrieval quality and context compression become critical.

17. **What is the key trade-off in PEFT?**
    Lower adaptation cost and modularity versus potential ceiling in task-specific performance compared with full fine-tuning.

# Further Reading & Sources

- DeepLearning.AI: Generative AI with LLMs (curriculum framing): https://www.deeplearning.ai/courses/generative-ai-with-llms
- Coursera course page: https://www.coursera.org/learn/generative-ai-with-llms
- Hugging Face Transformers docs: https://huggingface.co/docs/transformers/index
- LoRA paper (Hu et al., 2021): https://arxiv.org/abs/2106.09685
- Brown et al., GPT-3 (few-shot behavior): https://arxiv.org/abs/2005.14165
