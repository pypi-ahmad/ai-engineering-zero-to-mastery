# Notebook Status and Validation

This repo prioritizes **runnable learning**, but also avoids pretending that every notebook can always be executed in every environment (GPU, network access, OS differences).

## What We Validate in CI

CI runs `scripts/validate_curriculum.py`, which checks:

- lesson and sub-lesson structure,
- notebook JSON parses correctly,
- required markdown sections exist (objectives, case studies/exceptions, interview Q&A),
- code cells compile (basic syntax check),
- root README local links resolve,
- placeholder tokens (TODO/TBD/Lorem ipsum) are not present in curriculum files.

## Notebook Execution (Local)

This repository does **not** commit notebook execution logs. They tend to contain:

- machine-specific file paths (not portable),
- transient network/GPU failures,
- large tracebacks that add noise for beginners.

If you want to verify notebooks on your machine:

1. Start from a clean kernel (restart -> run all).
2. Prefer `uv run ...` commands so you do not accidentally use the wrong Python.

If you find a notebook that fails in a standard local setup, open an issue with:

- the notebook path,
- your OS + Python version,
- the exact error traceback,
- the output of `uv pip freeze` (or the relevant section of `uv.lock`).
