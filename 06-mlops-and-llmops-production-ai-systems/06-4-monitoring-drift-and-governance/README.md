# 6.4 Monitoring, Drift & Governance

This sub-lesson focuses on keeping deployed AI systems reliable, compliant, and trustworthy.

## Why This Matters

Models decay. Data distributions shift. Dependencies fail. Monitoring and governance are how you detect issues early, choose when to retrain, and avoid shipping harmful behavior.

## Key Terms (Plain English)

- **Drift**: inputs or performance change compared to training.
- **Alert threshold**: when you notify/investigate/rollback.
- **Retraining trigger**: explicit policy for when retraining is allowed.

## Start Here

1. `theory/06-4-monitoring-drift-and-governance.md`
2. `notebooks/06-4-monitoring-drift-and-governance-demo.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## Coverage

- Drift monitoring and performance decay detection
- Alerting and threshold design
- Responsible AI governance controls
- Safe retraining decision frameworks

## Verify Your Work

- Run the notebook from a clean kernel.
- Complete the exercises and write an alert policy that avoids constant false alarms.

## Common Mistakes

- Alerting on noisy metrics without persistence checks (alert fatigue).
- Retraining on every alert (churn without improvement).
