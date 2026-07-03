# 4.1 Neural Networks & Backpropagation

Introduces perceptrons, multilayer networks, forward propagation, loss functions, and backpropagation intuition with a minimal implementation.

## Why This Matters

Backprop is the engine of deep learning. If you understand forward pass, loss, and gradients, you can debug shape errors, training instability, and “why isn’t it learning” issues.

## Key Terms (Plain English)

- **Forward pass**: compute outputs from inputs.
- **Loss**: a number describing how wrong the model is.
- **Gradient**: how to change parameters to reduce loss.
- **Backpropagation**: computing gradients through the network.

## Start Here

1. Theory: `theory/04-1-neural-networks-and-backpropagation.md`
2. Notebook: `notebooks/04-1-neural-networks-and-backpropagation.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## Outcomes

- Explain how neural networks learn nonlinear decision boundaries.
- Derive gradient flow intuition through backpropagation.
- Implement a toy network and compare it to linear baselines.

## Verify Your Work

- Restart kernel -> Run all in the notebook.
- Complete the exercises and confirm your model’s shapes match expectations.

## Common Mistakes

- Applying softmax before `CrossEntropyLoss` (double-softmax mistake).
- Ignoring tensor shapes until runtime errors happen.
- Forgetting to set seeds when comparing runs.
