# Notebook Playbook (How To Learn Without Getting Stuck)

This repo uses notebooks as **teaching tools**, not production code. This page explains how to run them reliably and how to verify you learned something real.

## What Notebooks Are Good For

- Seeing an end-to-end demo quickly.
- Experimenting with parameters and visualizations.
- Learning patterns you later move into scripts/modules.

## What Notebooks Are Bad For

- Hidden state (cells run out of order).
- Silent dependency issues (wrong kernel).
- Hard-to-review changes (large JSON diffs).

## How To Run (Recommended)

1. Start Jupyter from the virtual environment:
   - follow `docs/setup-and-troubleshooting.md`
2. In the notebook:
   - Restart kernel
   - Run all

If results differ:
- check your environment versions (`uv.lock`),
- check seeds and splits,
- prefer CPU if GPU kernels are nondeterministic.

## Verification (How To Know You Actually Learned It)

After running a notebook once:

- Do the matching `exercises/` and compare with `solutions.md`.
- Change one parameter and predict what will change before running.
- Write a short note:
  - what you learned,
  - what artifact you produced (metric, model file, plot),
  - what you still don’t understand.

## Common Mistakes (And Fixes)

- Wrong kernel:
  - start Jupyter after activating `.venv/`
- Notebook runs once but fails later:
  - restart kernel, run all
- Code works in notebook but not as a script:
  - move logic into functions/modules; add a minimal test

