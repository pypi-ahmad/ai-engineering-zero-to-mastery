# Lesson 5: Generative Models & LLMs

Lesson 5 moves from classical generative modeling to modern LLM application design and post-training practice. It is organized as five chapter-style sub-lessons with both theory and runnable notebooks.

## Why This Matters

Generative AI is now a systems problem as much as a modeling problem: prompts, retrieval, tools, evaluation, and operational controls determine whether an LLM app is reliable. This lesson builds those foundations before you scale into LLMOps.

## Expected Outcomes

- You can explain what an LLM does and what it does not guarantee (non-determinism, hallucinations).
- You can build a small grounded system (RAG or tool-augmented) and evaluate it.
- You can describe when prompting is enough vs when fine-tuning makes sense.

## Sub-lessons

1. **5.1 Classical Deep Generative Models (VAEs, GANs, Flows)**
   - Latent-variable modeling, ELBO intuition, adversarial training, and invertible density modeling.
2. **5.2 Autoregressive & Diffusion Models**
   - Token-by-token generation vs iterative denoising, with practical sampling trade-offs.
3. **5.3 LLM Foundations & Prompt Engineering**
   - LLM capabilities/limits, prompting patterns, and fine-tuning/PEFT overview.
4. **5.4 RAG, Tools, and AI Agents**
   - Retrieval-grounded generation, tool/function calling patterns, and multi-step agent loops.
5. **5.5 LLM Post-Training & Fine-Tuning**
   - Eval-first adaptation workflows with SFT, PEFT, LoRA, QLoRA, and alignment handoff (DPO/RLHF concepts).

## How to Use This Lesson

1. Read each sub-lesson `theory/*.md` chapter first.
2. Run the paired notebook in `notebooks/`.
3. Focus on the “Business Case Studies & Exceptions” and “Interview Questions & Answers” sections for production and interview depth.

## File Layout

- `05-1-classical-deep-generative-models/`
- `05-2-autoregressive-and-diffusion-models/`
- `05-3-llm-foundations-and-prompt-engineering/`
- `05-4-rag-tools-and-ai-agents/`
- `05-5-llm-post-training-and-fine-tuning/`

## Bridge from Lesson 4
**Why this follows:** Lesson 4 gives the neural and transformer fundamentals required to understand modern generative AI behavior.

**You should already know:** backpropagation intuition, optimization basics, and sequence/attention concepts.

**What you will do next:** build from model-level generative concepts to application-level LLM patterns (prompting, RAG, tool use, agent loops).

## Bridge to Lesson 6
Lesson 6 turns these GenAI prototypes into production systems by introducing MLOps/LLMOps lifecycle design, deployment, monitoring, and governance.
