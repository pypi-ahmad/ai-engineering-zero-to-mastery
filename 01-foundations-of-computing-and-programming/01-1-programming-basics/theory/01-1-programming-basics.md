# Overview

Programming basics are the reliability layer under every AI system. Models can be state-of-the-art and still fail in production because of weak input checks, hidden notebook state, file-path bugs, or unhandled runtime exceptions.

In this chapter, "programming basics" means building deterministic, testable, reusable logic that behaves well under real-world data conditions.

A practical mental model:
- Modeling code is the brain.
- Data and control-flow code is the nervous system.
- Error handling and logging is the immune system.

If the system code is weak, even good models cannot produce stable business value.

Operationally, this is the difference between a model that looks good in a demo and a feature that survives real traffic. In real systems, bugs usually come from edge inputs, deployment mismatches, and silent assumptions, not from missing model layers. For example, a recommendation pipeline can fail if one upstream table changes timestamp format from UTC ISO-8601 to local strings. The fix is not "better ML"; it is boundary validation, explicit parsing, and clear failure policy.

A practical risk lens:
- **State risk:** hidden state, mutable globals, non-idempotent execution.
- **Data risk:** schema drift, null semantics, unit mismatches, encoding issues.
- **Control-flow risk:** retries without limits, swallowed exceptions, ambiguous fallbacks.

When writing beginner-level scripts with production intent, optimize for observability and failure clarity: every boundary validates input, every important function states assumptions, and every failure leaves a useful trace for debugging.

# Setting Up Your Environment

Use isolated environments for reproducibility and team handoff.

1. Create an environment: `uv venv --python 3.12`
2. Activate: `source .venv/bin/activate`
3. Install dependencies: `uv sync` or `uv add <pkg>`
4. Run notebooks: `jupyter lab`

Environment isolation reduces dependency conflicts and makes CI failures easier to reproduce locally.

Recommended baseline project layout:

```text
project/
  pyproject.toml
  src/
    app/
      __init__.py
      io_utils.py
      validation.py
      transforms.py
  tests/
  notebooks/
```

Environment reproducibility checklist:
- Pin runtime and dependency versions.
- Keep setup one-command where possible (`uv sync`).
- Document hardware assumptions for longer runs.
- Ensure teammate setup is deterministic: clone -> activate -> smoke test.

Exception in early prototyping: fast package iteration may be necessary. Even then, snapshot dependencies before sharing results.

# Python Basics

## Variables and Types

Formal definition: a variable is a name bound to an object in memory.

Core built-in types:
- Numeric: `int`, `float`
- Text: `str`
- Boolean: `bool`
- Collections: `list`, `tuple`, `dict`, `set`
- Nullability marker: `None`

Typed-thinking principle: every function has an implicit domain and codomain.
If `f: X -> Y`, passing values not in `X` is a contract violation.

Example:

```python
def monthly_growth(current: float, previous: float) -> float:
    if previous == 0:
        raise ValueError("previous must be non-zero")
    return (current - previous) / previous
```

## Control Flow

Control flow defines execution order.
- Branching: `if / elif / else`
- Iteration: `for`, `while`
- Early exits: `break`, `continue`, `return`

Production AI use-cases:
- Branch to fallback model if primary model is unavailable.
- Skip malformed records but continue batch processing.
- Stop loops when data-quality thresholds are exceeded.

Diagram in words:
Imagine each `if` condition as a gate in a pipeline. Good systems place these gates at boundaries (ingestion, feature generation, prediction output), not only at the final stage.

## Functions and Reuse

Formal definition: a function maps inputs to outputs, optionally with side effects.

For pure functions:
$$
f: X \rightarrow Y
$$

Properties of good reusable functions:
- Single responsibility.
- Explicit inputs/outputs.
- Deterministic for same input.
- Raises informative exceptions for invalid states.

Function design checklist:
- What assumptions does this function require?
- What can fail?
- What should happen on failure (raise, retry, fallback)?

## Modules and Imports

A module is a Python file that encapsulates related logic.

Why modularization matters in AI work:
- Notebooks stay readable.
- Core logic becomes testable.
- Reuse across training/inference pipelines is straightforward.

Common split:
- `validation.py`: schema/type/range checks
- `feature_engineering.py`: transformations
- `train.py`: training orchestration
- `serve.py`: inference entry points

## Error Handling

Formal definition: an exception is a runtime signal indicating a violated assumption or an abnormal execution state.

Patterns:
- `try/except` for recoverable failures.
- `raise` for invalid inputs and invariant violations.
- Domain exceptions for business clarity.

Example hierarchy:
- `DataValidationError`
- `ExternalAPIError`
- `ModelInferenceError`

Exception handling anti-pattern:

```python
# Bad: swallows root cause
try:
    risky_call()
except Exception:
    pass
```

Preferred pattern:

```python
try:
    risky_call()
except TimeoutError as exc:
    logger.warning("Vendor timeout", extra={"service": "feature_api"})
    raise ExternalAPIError("feature lookup timed out") from exc
```

## Input/Output

I/O is where most operational bugs originate.

I/O contract checklist:
- Input schema validated?
- Required columns/fields present?
- Types and units explicit?
- Missing values strategy defined?
- Output schema versioned?

## Code Style and Readability

Readability is a scaling property for teams.

Practical rules:
- Prefer descriptive names over short cryptic names.
- Keep functions small and composable.
- Separate orchestration from business logic.
- Use docstrings for public functions.

Readable code reduces incident recovery time and onboarding costs.

# Working in Jupyter

Jupyter is ideal for exploration but risky when execution order is non-deterministic.

Notebook discipline:
- Restart kernel + run all before committing.
- Move stable logic into modules under `src/`.
- Keep markdown next to code to state assumptions.
- Keep cells idempotent.

Notebook-to-module handoff pattern:
1. Prototype with small deterministic samples.
2. Extract stable logic into `src/` functions with type hints.
3. Add unit tests for extracted functions.
4. Keep notebook as narrative and experiment log, not runtime source of truth.

Diagram in words:
Think of notebook execution as a timeline. If rerunning from top to bottom changes behavior, hidden state exists and reproducibility is compromised.

# Common Pitfalls & Exceptions

## Hidden State

Cells executed out of order can leave stale variables that make results appear correct.

Mitigation:
- Restart-run-all checks.
- Encapsulate repeated logic in functions.

## Silent Type Coercion

`"10" + "5"` and `10 + 5` are semantically different.

Mitigation:
- Validate and cast types at boundaries.

## Broad Exception Handling

Catching all exceptions without context hides real failures.

Mitigation:
- Catch specific exception classes.
- Add context in logs.

## Hardcoded Paths

Absolute local paths break CI and teammate environments.

Mitigation:
- Use `pathlib.Path` and project-relative paths.

# Mini Projects

## Project 1: CLI Metric Calculator

Goal: build a robust CLI utility that computes mean, variance, and z-scores from user input.

Requirements:
- Parse numeric inputs safely.
- Handle empty inputs.
- Return structured output.
- Log validation failures.

Extension:
- Add percentile and IQR for outlier-robust summaries.

## Project 2: File Processor

Goal: process CSV records, validate required columns, transform values, and persist valid rows.

Requirements:
- Validate schema before transformation.
- Log row-level failures with row index.
- Fail fast if error ratio exceeds threshold.

Extension:
- Add config-driven rules from YAML.

# Business Case Studies & Exceptions

## Case 1: ETL Preprocessor for Recommendation Features

Scenario:
A daily ETL pipeline computes user-level aggregates for recommendation features. A timestamp format drift from one source begins producing malformed dates.

Impact:
- Feature null rates spike.
- Model quality drops due to stale/incorrect features.
- Debugging slows because failures are swallowed.

Practical pattern:
- Parse timestamps with strict format and explicit timezone handling.
- Log invalid rows to a quarantine table.
- Continue processing valid rows.
- Abort job when invalid-row ratio exceeds a configured threshold.

Exception to the "continue-on-error" rule:
If malformed rows are concentrated in a regulated cohort (for example, risk decisions), fail the pipeline immediately and escalate.

## Case 2: Online Inference Input Validation

Scenario:
A prediction endpoint receives payloads from multiple clients. A client deploy changes field names and sends missing features.

Impact:
- Invalid predictions or 500s.
- Potential downstream business-rule violations.

Practical pattern:
- Validate request schema at API boundary.
- Return explicit 4xx validation errors.
- Track validation error rates by client version.

Exception:
For non-critical recommendation widgets, a fallback heuristic may be preferable to hard failure when a small subset of optional fields are missing.

## Case 3: Batch Job with Partial External API Outage

Scenario:
An enrichment API fails intermittently.

Pattern:
- Retry transient failures with capped backoff.
- Mark unresolved rows for later replay.
- Enforce max retry budget to avoid SLA breaches.

# Interview Questions & Answers

1. **Q: Why do strong programming fundamentals matter for AI engineers?**
   **A:** Most production failures come from data handling, control flow, and integration errors, not model architecture alone.

2. **Q: What is the difference between a syntax error and a runtime exception?**
   **A:** Syntax errors prevent program parsing before execution; runtime exceptions occur during execution for specific states/inputs.

3. **Q: What is a pure function and why is it useful?**
   **A:** A pure function depends only on inputs and has no side effects, which makes it easier to test and reason about.

4. **Q: When should you raise exceptions instead of returning default values?**
   **A:** Raise exceptions when invariants are violated or silent fallback would hide safety-critical failures.

5. **Q: Why prefer logging over print in production?**
   **A:** Logging supports levels, timestamps, structured metadata, filtering, and centralized observability.

6. **Q: What is hidden state in notebooks?**
   **A:** State created by out-of-order cell execution that is not visible from top-to-bottom notebook flow.

7. **Q: How do you design a robust I/O boundary?**
   **A:** Validate schema, types, ranges, and missingness; define clear failure behavior and output contracts.

8. **Q: What is defensive programming in AI systems?**
   **A:** Explicit checks for assumptions, bounded retries, actionable errors, and safe fallbacks where appropriate.

9. **Q: What is a good function signature for production code?**
   **A:** Typed parameters, typed return value, minimal side effects, and clear contract around exceptions.

10. **Q: How do you decide between fail-fast and fail-soft behavior?**
    **A:** Use fail-fast for correctness/safety-critical workflows; fail-soft for non-critical paths with monitored degradation.

11. **Q: Why avoid broad `except Exception`?**
    **A:** It masks root causes and can convert critical failures into silent data corruption.

12. **Q: Give one sign that code should be modularized.**
    **A:** If the same logic appears in multiple notebooks/scripts, extract it into a shared module.

13. **Q: What is a good first hardening step for a notebook prototype?**
    **A:** Move core logic into tested module functions and keep the notebook for orchestration and analysis.

14. **Q: Why validate inputs at boundaries instead of deep in business logic?**
    **A:** Boundary checks fail fast with clearer context and prevent corrupted states from propagating.

15. **Q: How do programming basics reduce incident recovery time?**
    **A:** Clear contracts, structured logs, and explicit exceptions make root-cause analysis faster.

# References

- Python documentation: https://docs.python.org/3/
- Packaging with uv: https://docs.astral.sh/uv/
- Effective Python (book site): https://effectivepython.com/
