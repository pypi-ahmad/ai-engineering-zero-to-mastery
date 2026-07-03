# Exercises: 5.5 LLM Post-Training & Fine-Tuning

These exercises are designed to be runnable offline by using a *toy* LoRA-like adapter on a small torch model.

Optional prereq (if you want to run the Transformers/PEFT notebook end-to-end and have model access):

```bash
uv sync --frozen --extra genai
```

## Exercise 1: Decision Checklist (Prompt vs RAG vs Fine-Tune)

Create a 3-column table:
- prompting
- RAG
- fine-tuning

For each, list:
- when it’s best,
- typical failure mode,
- what you must evaluate.

Expected outcome:
- you can justify the cheapest option that meets requirements.

## Exercise 2: Implement LoRA for Linear (Toy)

Implement a `LoRALinear` module that:
- wraps an `nn.Linear`,
- freezes the base weight,
- adds a low-rank update `BA` scaled by `alpha/r`.

Expected outcome:
- only LoRA parameters require gradients.

## Exercise 3: Train Adapter on a Small Task

Create a toy dataset where `y = sign(w^T x)` and train:
- a frozen base linear model + LoRA adapter,
- compare to training the full model.

Expected outcome:
- adapter training improves accuracy without updating base weights.

## Exercise 4: Eval-First Workflow

Before training:
- define a metric,
- define a heldout split,
- define a “stop” condition.

Expected outcome:
- you can detect overfitting or no improvement early.

## Exercise 5: Package and Reload

Save only LoRA parameters to disk and reload into a fresh model.

Expected outcome:
- reloaded adapter gives the same predictions as before save.

