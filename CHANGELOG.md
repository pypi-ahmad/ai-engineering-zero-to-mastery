# Changelog

All notable changes to this repository are documented here.

## v1.3.0 (2026-07-03)

Release focused on strengthening the beginner practice loop through Lesson 6, with CI enforcing the practice structure for early lessons.

- Added exercises + solutions for Lessons 4–6 (Deep Learning, GenAI, and MLOps/LLMOps) to make practice consistent for beginners.
- Added a Lesson 6 LLMOps practice set covering prompt versioning, evaluation harnesses, cost/token gating, retrieval circuit breakers, and tool policy gates.
- Updated `scripts/validate_curriculum.py` to require the “theory -> notebook -> exercises -> solutions” loop for Lessons 1–6.

## v1.4.0 (2026-07-03)

Release focused on making the repository easier for complete beginners to navigate without losing the depth of the full 15-lesson curriculum.

- Added a new guided path in `curriculum/` with a recommended learning order, prerequisite flow, and completion criteria per module.
- Updated onboarding docs and tracks to point to the guided curriculum path.
- Added a `projects/` index and updated the capstone template quickstart to run scripts via `uv run python` for reproducible execution.

## v1.5.0 (2026-07-03)

Release focused on tutorial-grade pedagogy: clearer definitions, stronger verification steps, and fewer beginner dead-ends.

- Added a beginner-friendly glossary (`docs/glossary.md`) and strengthened onboarding/verification in `docs/start-here.md` and `docs/setup-and-troubleshooting.md`.
- Upgraded Lesson 1–6 READMEs (and their sub-lessons) with concise: why this matters, key terms, expected outcomes, verification, and common mistakes.
- Upgraded Lessons 7–15 lesson READMEs with expected outcomes and verification guidance.
- Added a notebook playbook and improved intros for selected beginner-critical notebooks with explicit run/verify steps.

## v1.5.1 (2026-07-03)

Release polish focused on consistency and beginner onboarding.

- Overhauled the root README into a clearer beginner-first “front door” with roadmap, navigation, curated references, and troubleshooting pointers.
- Standardized `uv sync` commands across docs and capstone error messages to recommend `--frozen` for reproducible installs.

## v1.2.0 (2026-07-03)

Release focused on portability, lean release hygiene, and a consistent beginner practice loop.

- Removed committed notebook-generated datasets/artifacts and maintainer-only scraped dumps; added ignores to prevent reintroducing them.
- Made notebooks more portable by removing machine-specific absolute paths and adding an offline fallback for Lesson 5.1 data loading.
- Improved onboarding by adding official `uv` installation instructions.
- Strengthened `scripts/validate_curriculum.py` to validate links across markdown, forbid tracked generated artifacts, and reject absolute repo paths.
- Added exercises + solutions for Lessons 1–3 to make practice consistent for beginners.

## v1.1.0 (2026-07-03)

Beginner-first release focused on reproducibility, runnable scaffolds, and maintainability.

- Added `pyproject.toml` + `uv.lock` and documented optional extras (`dl`, `genai`, `rl`, `serving`, `ops`) for dependency clarity.
- Added a runnable capstone scaffold at `projects/capstone-template/` (data → train → eval → serve) with pytest coverage.
- Added `scripts/validate_curriculum.py` and updated CI to use it (structure + notebook + link checks, excluding `.venv/` noise).
- Added beginner onboarding docs: `docs/start-here.md`, `docs/setup-and-troubleshooting.md`, `docs/learning-tracks.md`.
- Added MIT `LICENSE`.
