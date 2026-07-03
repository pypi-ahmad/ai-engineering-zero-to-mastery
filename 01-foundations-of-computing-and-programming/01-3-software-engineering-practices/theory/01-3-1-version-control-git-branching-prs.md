# Overview

Version control is the source of truth for software evolution. In AI engineering, reproducibility, auditability, and rollback are critical because data pipelines and models change frequently.

This chapter covers Git concepts, branching workflows, pull-request quality, and CI/CD integration for production-safe delivery.

In real AI organizations, version control is also a governance mechanism. It links model changes to reviewers, issue tickets, deployment history, and incident timelines. When a prediction regression appears in production, teams need to answer: what changed, who approved it, what checks passed, and how to roll back. Git history plus PR metadata is the fastest path to those answers.

# Core Git Concepts

- **Repository:** versioned project history.
- **Commit:** immutable snapshot with message and metadata.
- **Branch:** independent line of work.
- **Remote:** shared upstream repository.
- **Tag:** named release checkpoint.

Commit quality guideline:
A commit should represent one coherent intent and be independently reviewable.

# Branching & Workflow

Common workflow styles:

1. Feature branching
- Create branch per task.
- Merge via PR into `main`.

2. Trunk-based development
- Short-lived branches.
- Frequent integration.
- Lower merge drift.

3. GitFlow
- Structured release/hotfix branches.
- Useful for strict release governance.

Pragmatic recommendation for AI repos:
- Feature branches + frequent rebasing/merging + protected `main`.

Operational heuristic:
- Short-lived branches reduce merge risk.
- Small PRs reduce review fatigue.
- Frequent integration reveals incompatibilities earlier.

Naming examples:
- `feat/credit-risk-threshold-calibration`
- `fix/leakage-in-scaler-fit`
- `chore/add-cv-metrics-report`

# Pull Requests & Code Review

A PR is a risk-reduction checkpoint.

Strong PR template should include:
- Problem statement.
- What changed.
- Repro steps (commands, seeds, config).
- Metric deltas (before vs after).
- Risks and rollback plan.

Review depth guideline:
- Low-risk docs/config edits: lightweight review.
- Model/pipeline contract changes: mandatory technical + product/risk review.
- Serving/infra changes: require rollback simulation evidence.

AI-specific review checklist:
- Data leakage risk checked?
- Split strategy preserved?
- Random seeds set where needed?
- Claims supported by notebook/script outputs?
- Backward compatibility for model APIs ensured?

# CI/CD Basics for AI Teams

CI: automated checks on every PR.
CD: controlled deployment/publishing after checks pass.

Typical CI checks:
- Unit tests
- Lint/type checks
- Basic notebook execution smoke test
- Secret scanning

Typical CD gates:
- Versioned artifact built
- Promotion criteria met (metrics and monitoring checks)
- Rollback artifact available

Diagram in words:
Developer commit -> PR -> CI checks -> review approval -> merge -> release pipeline -> deployment -> monitoring.

# Practical AI Engineering Scenarios

## Experiment Branch Strategy

Use dedicated experiment branches and keep experiment-only artifacts separate from reusable production modules.

Pattern:
- Branch for hypothesis test.
- Capture configs and metrics.
- Squash to concise final commits for production merge.

## PR for Pipeline Contract Changes

When feature schema changes:
- Include before/after schema examples.
- Add migration notes.
- Add integration tests for old/new clients where relevant.

## Release Hotfix Under Incident

Hotfix procedure:
- Branch from stable tag.
- Minimal targeted patch.
- Fast CI + reviewer signoff.
- Tag release.
- Post-incident root-cause follow-up PR.

# Common Pitfalls

- Committing large raw datasets to Git history.
- Combining unrelated refactors with bug fixes in one PR.
- Force-pushing shared branches without team coordination.
- Merging without green CI.
- Ambiguous commit messages ("fix stuff", "update").

# Business Case Studies & Exceptions

## Case 1: Secret Leaked in Commit

Scenario:
An API key was committed in notebook output and pushed to remote.

Response pattern:
1. Revoke and rotate credential immediately.
2. Remove exposure from current code.
3. Rewrite history if required by policy.
4. Add secret scanning in CI and pre-commit hooks.

Exception:
For internal-only sandbox repos, history rewrite may be unnecessary if immediate rotation + repository cleanup satisfies policy.

## Case 2: Broken Merge Before Release

Scenario:
Model-serving code merged without integration test against latest feature schema.

Impact:
Production inference failures.

Fix pattern:
- Branch protection requiring CI pass.
- Mandatory reviewer for high-risk paths.
- Pre-release smoke tests.

## Case 3: Long-Lived Branch Drift

Scenario:
Two-week branch accumulates conflicts and stale assumptions.

Fix pattern:
- Rebase/merge from `main` frequently.
- Slice work into smaller PRs.

# Interview Questions & Answers

1. **Q: Why is Git especially important for ML projects?**
   **A:** It provides traceability and rollback for code that directly influences data pipelines, features, and model behavior.

2. **Q: Merge vs rebase?**
   **A:** Merge preserves branching history; rebase rewrites commit base for linear history. Use team conventions consistently.

3. **Q: What makes a strong PR in AI systems?**
   **A:** Clear intent, reproducible evidence, metric impact, risk analysis, and rollback plan.

4. **Q: Why protect `main` branch?**
   **A:** To enforce checks/reviews before integration and reduce accidental unstable merges.

5. **Q: What should CI validate before merge?**
   **A:** Tests, lint/type checks, security scans, and critical workflow smoke tests.

6. **Q: Why avoid large binary data in Git?**
   **A:** It bloats history and slows clone/fetch operations; use external data storage/versioning systems.

7. **Q: How do you handle emergency hotfixes safely?**
   **A:** Minimal patch on stable baseline, accelerated but still mandatory checks, immediate monitoring.

8. **Q: What is rollback strategy in practice?**
   **A:** Revert problematic commit or redeploy last known-good artifact/tag.

9. **Q: Why split large changes into smaller PRs?**
   **A:** Smaller PRs are easier to review, test, and revert.

10. **Q: What is the risk of skipping PR review for "small" changes?**
    **A:** Small changes can still introduce leakage, contract breaks, or hidden operational regressions.

11. **Q: Why are small, frequent PRs preferred in AI teams?**
    **A:** They lower review complexity, reduce conflict probability, and speed safe iteration.

12. **Q: What should a rollback-ready release include?**
    **A:** Last-known-good artifact/version, clear rollback command path, and verification checklist.

13. **Q: How does Git help with regulated AI workloads?**
    **A:** It provides auditable change history with reviewer and approval traceability.

14. **Q: When should you block merge even with passing tests?**
    **A:** When PR lacks reproducible evidence, clear risk analysis, or contract-impact documentation.

15. **Q: What is one anti-pattern in AI experiment branches?**
    **A:** Long-lived branches that combine unrelated experiments and production changes.

# References

- Pro Git book: https://git-scm.com/book/en/v2
- Git branching docs: https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell
- GitHub docs on PRs: https://docs.github.com/en/pull-requests
