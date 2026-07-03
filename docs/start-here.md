# Start Here

If you are new to AI engineering, start with **Lesson 1** and follow the order. This repo is designed as a curriculum, not a bag of scripts.

## What Is AI Engineering?

AI engineering is the practice of building **AI systems that work reliably**:

- data ingestion and validation,
- training and evaluation (including baselines),
- packaging and serving,
- monitoring quality, latency, and cost,
- safety, governance, and incident readiness.

“Model training” is only one part of the job.

## Key Terms (2-minute skim)

If you hit jargon early, skim the glossary:
- [`docs/glossary.md`](./glossary.md)

## How To Study This Repo

For each sub-lesson:

1. Read the sub-lesson `README.md` (what you’ll do and why).
2. Read the `theory/*.md` chapter (plain English + tradeoffs).
3. Run the `notebooks/*.ipynb` teaching notebook (hands-on).
4. Do the `exercises/` (if present) to verify understanding.
5. Write a short summary:
   - what you learned,
   - what you can now build,
   - what confused you (make it a note).

## What “Good Progress” Looks Like

- You can explain the concept in your own words.
- You can run the notebook **from a clean kernel** (restart → run all).
- You can modify one parameter and predict what will change.
- You can reproduce outputs (or understand why they differ).

## Common Beginner Mistakes

- Skipping Lesson 1 and getting blocked later by basic Python/runtime issues.
- Only reading theory (no execution), or only running code (no understanding).
- Treating notebooks as production code (hidden state, hardcoded paths).
- Not saving artifacts (model files, metrics, configs) for reproducibility.

## Expected Outcomes (First Week)

- You can run notebooks from a clean kernel and explain what changed when you tweak a parameter.
- You can train + evaluate a baseline model with a defensible metric.
- You can produce at least one saved artifact (metrics JSON, model file, or a small API contract).

## Verification (Day 1 Sanity Checks)

From the repo root:

```bash
python3 scripts/validate_curriculum.py
```

If you already have a `.venv/`, run tests:

```bash
.venv/bin/python -m pytest -q
```

## Where To Go Next

- If you want quick hands-on wins: follow the **Beginner Track** in `docs/learning-tracks.md`.
- If you want a guided beginner-first order: follow `curriculum/README.md`.
- If you want the full journey: follow Lessons 1 → 15 in order.
- If you want a runnable system scaffold: start with `projects/capstone-template/`.
