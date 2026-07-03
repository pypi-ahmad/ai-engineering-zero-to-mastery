# 1.3 Software Engineering Practices

This sub-lesson builds engineering discipline needed to ship reliable AI systems: version control, clean design, and API fundamentals.

## Why This Matters

Most “AI projects” fail because the codebase becomes untestable and unreproducible. Engineering practices are what turn experiments into software other people can run, review, and deploy.

## Learning Objectives
- Apply safe Git workflows with branches, pull requests, and review hygiene.
- Structure Python code for readability, modularity, and testability.
- Understand HTTP/JSON API patterns used by ML and GenAI services.

## Key Terms (Plain English)

- **Reproducibility**: a teammate can rerun your work and get the same (or explainably similar) results.
- **Test**: a small program that checks behavior automatically (prevents regressions).
- **API contract**: an agreed request/response shape so clients don’t break when you deploy.
- **Version control**: tracking changes over time (Git) so you can review and rollback.

## Theory Chapters
- `theory/01-3-1-version-control-git-branching-prs.md`
- `theory/01-3-2-clean-code-modular-design-documentation.md`
- `theory/01-3-3-basic-rest-apis-http-json.md`

## Teaching Notebooks
- `notebooks/01-3-1-version-control-git-branching-prs.ipynb`
- `notebooks/01-3-2-clean-code-modular-design-documentation.ipynb`
- `notebooks/01-3-3-basic-rest-apis-http-json.ipynb`

## Practice (Recommended)
After you complete the notebooks, do:

1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## Expected Outcomes

- You can describe a safe Git workflow (branch -> PR -> review -> merge).
- You can structure Python code into modules and write at least one test.
- You can define a minimal HTTP endpoint contract for a model prediction.

## Verify Your Work

- Run the notebooks from a clean kernel.
- Complete the exercises and write one additional test for a function you wrote.
- Explain what you would log and persist for a training run (config, metrics, artifacts).

## Common Mistakes

- Treating notebooks as deployable code without tests.
- Making breaking API changes without versioning.
- “It works on my machine” due to missing environment pinning.

## Prerequisites
- Lesson 1.1 and 1.2 basics (Python syntax, data structures, control flow).
- Basic command-line familiarity.

## What's Next
Continue to Lesson 2 (Mathematics for AI) with stronger engineering habits for implementing and validating ML workflows.
