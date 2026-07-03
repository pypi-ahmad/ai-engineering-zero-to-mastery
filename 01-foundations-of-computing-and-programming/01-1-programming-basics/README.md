# 1.1 Programming Basics

This lesson teaches practical Python foundations used across AI engineering pipelines and scripts.

## Why This Matters

Most AI learning gets blocked by basic programming friction (errors, environment confusion, messy scripts). This sub-lesson teaches the minimum Python you’ll reuse everywhere: data loading, training loops, and automation scripts.

## Learning Goals
- Use variables, control flow, functions, and modules confidently.
- Handle errors safely and write readable, maintainable code.
- Build small automation scripts that resemble real AI team workflows.

## How It Fits in the Curriculum
These fundamentals are reused in every later lesson for data prep, model training, serving, and operations code.

## Key Terms (Plain English)

- **Script**: a `.py` file you can run end-to-end from the terminal.
- **Function**: a reusable block of code with inputs and outputs.
- **Exception**: an error that stops execution unless you handle it.
- **Module**: a Python file you can import from other files.

## Start Here
1. Theory: `theory/01-1-programming-basics.md`
2. Notebook: `notebooks/01-1-programming-basics.ipynb`

## Practice (Recommended)
After running the notebook once, do:

1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## Expected Outcomes

- You can write a small script that reads input, transforms it, and writes output.
- You can debug common errors (NameError, TypeError, KeyError) without panic.
- You can refactor repeated code into functions.

## Verify Your Work

- Restart kernel -> Run all in the notebook without errors.
- Complete Exercises 1–3 without looking at solutions.
- Create one extra small script (10–30 lines) that automates a task you’d do repeatedly.

## Common Mistakes

- Writing everything in one notebook cell (hard to debug and reuse).
- Copy-pasting code instead of writing a small function.
- Ignoring error messages instead of reading the traceback top-to-bottom.

## Troubleshooting

- If imports fail: you’re likely running Jupyter outside `.venv/`. See `docs/setup-and-troubleshooting.md`.
