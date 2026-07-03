# Exercises: 6.4 Monitoring, Drift & Governance

Offline-first exercises using toy distributions and simple metrics.

## Exercise 1: Drift Detection (KS Test)

Simulate:
- training feature distribution,
- serving feature distribution.

Use a statistical test (e.g., KS test) and decide:
- when to alert,
- when to investigate,
- when to rollback.

Expected outcome:
- you can choose thresholds and explain tradeoffs.

## Exercise 2: Rolling Performance Monitor

Simulate a stream of predictions with labels and compute:
- rolling accuracy (window size 200),
- an alert when accuracy drops below a threshold.

Expected outcome:
- you can see how noisy signals can create false alerts.

## Exercise 3: Data Quality Gates for Inference

Write a validator that checks:
- missing rate,
- numeric ranges,
- allowed categories.

Expected outcome:
- invalid requests are rejected or routed to fallback (explicit policy).

## Exercise 4: Governance Checklist (Release Gate)

Write a checklist that must be true before a model rollout:
- evaluation complete,
- monitoring in place,
- rollback plan,
- privacy/security review.

Expected outcome:
- you can use it as a pre-deploy gate in CI.

## Exercise 5: Retraining Trigger Policy

Define a simple retraining trigger:
- drift above threshold OR
- metric drop sustained for N windows.

Expected outcome:
- policy is explicit and avoids “retrain on every alert”.

