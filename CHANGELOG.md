# Changelog

All notable changes to this repository are documented here.

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
