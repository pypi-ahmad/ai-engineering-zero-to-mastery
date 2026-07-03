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

## Execution Logs

Historical notebook execution logs (from prior nbconvert runs) live in:

- `docs/_artifacts/notebook_execution_failures.json`
- `docs/_artifacts/notebook_rerun_failures.json`

These are not authoritative “current failures” because:

- notebook execution depends on environment constraints (GPU, network, permissions),
- dependencies evolve over time,
- CI does not execute every notebook by default.

If you find a notebook that fails in a standard local setup, open an issue with:
- the notebook path,
- your OS + Python version,
- the exact error traceback,
- the output of `uv pip freeze` (or the relevant section of `uv.lock`).

