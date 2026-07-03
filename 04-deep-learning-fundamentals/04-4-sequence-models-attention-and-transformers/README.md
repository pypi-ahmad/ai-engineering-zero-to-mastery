# 4.4 Sequence Models, Attention & Transformers

Introduces sequential modeling (RNN/LSTM intuition), attention mechanics, and transformer fundamentals as a bridge to Lesson 5 and LLM content.

## Why This Matters

Transformers power modern LLMs and many vision systems. This sub-lesson gives you the minimum transformer intuition needed to understand tokenization, attention, and why context matters.

## Key Terms (Plain English)

- **Token**: a chunk of text a model processes (not always a full word).
- **Attention**: a mechanism for mixing information across positions.
- **Positional encoding**: a way to represent order in sequences.

## Start Here

1. Theory: `theory/04-4-sequence-models-attention-and-transformers.md`
2. Notebook: `notebooks/04-4-sequence-models-attention-and-transformers.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## Outcomes

- Understand sequence modeling trade-offs across RNN/LSTM/Transformer families.
- Explain self-attention and positional encoding at an engineering level.
- Connect transformer foundations to modern GenAI and LLM workflows.

## Verify Your Work

- Run the notebook from a clean kernel.
- Complete the exercises and explain what attention is doing in one paragraph.

## Common Mistakes

- Treating transformers as “magic” without understanding tokens/context limits.
- Confusing training (pretraining/fine-tuning) with inference (generation).
