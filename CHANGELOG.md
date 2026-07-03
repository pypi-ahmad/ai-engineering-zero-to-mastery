# Changelog

All notable changes to this repository are documented here.

## v1.1.0 (2026-07-03)

Beginner-first release focused on reproducibility, runnable scaffolds, and maintainability.

- Added `pyproject.toml` + `uv.lock` and documented optional extras (`dl`, `genai`, `rl`, `serving`, `ops`) for dependency clarity.
- Added a runnable capstone scaffold at `projects/capstone-template/` (data → train → eval → serve) with pytest coverage.
- Added `scripts/validate_curriculum.py` and updated CI to use it (structure + notebook + link checks, excluding `.venv/` noise).
- Added beginner onboarding docs: `docs/start-here.md`, `docs/setup-and-troubleshooting.md`, `docs/learning-tracks.md`.
- Added MIT `LICENSE`.

