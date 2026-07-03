# 6.3 Model Deployment & Serving

This sub-lesson explains how trained models become reliable prediction services.

## Why This Matters

Training is not deployment. Serving requires stable input/output contracts, versioning, latency controls, and safe rollout/rollback. Without these, “it worked in the notebook” becomes an incident.

## Key Terms (Plain English)

- **Contract test**: tests that enforce API request/response shapes.
- **Canary rollout**: send a small % of traffic to a new version first.
- **Rollback**: revert quickly to a previous version when things go wrong.

## Start Here

1. `theory/06-3-model-deployment-and-serving.md`
2. `notebooks/06-3-model-deployment-and-serving-fastapi-demo.ipynb`

## Practice (Recommended)
1. Exercises: `exercises/exercises.md`
2. Solutions (check your work): `exercises/solutions.md`

## Coverage

- Online, batch, and streaming serving modes
- Model packaging with containers and orchestration
- Safe rollout strategies and rollback patterns
- Registry-driven versioning and service reliability

## Verify Your Work

- Run the notebook from a clean kernel.
- Complete the exercises and ensure you can:
  - version endpoints (`/v1`, `/v2`),
  - run a contract test,
  - explain your rollback strategy.

## Common Mistakes

- Changing input schemas without versioning (breaks clients).
- Shipping without tests and relying on manual clicks.
