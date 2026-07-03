# 00: Orientation (Start Here)

Goal: remove setup friction, define what AI engineering is, and make your first progress day predictable.

## What To Do

1. Read: [`docs/start-here.md`](../../docs/start-here.md)
2. Setup your environment: [`docs/setup-and-troubleshooting.md`](../../docs/setup-and-troubleshooting.md)
3. Sanity check the repo:

```bash
python3 scripts/validate_curriculum.py
```

If you have a working local `.venv`, run tests:

```bash
.venv/bin/python -m pytest -q
```

## What You Should Understand After This

- The difference between: ML training vs AI engineering systems work.
- How to navigate this repo: lesson -> sub-lesson -> theory -> notebook -> exercises.
- How to keep progress steady: small artifacts and consistent verification.

## Common Beginner Mistakes

- Installing everything upfront. Instead, install optional extras only when a lesson needs them.
- Running notebooks out of order without restarting the kernel.
- Treating notebooks as production code: hidden state and hardcoded paths will hurt you later.

## Next

Continue to [01-foundations](../01-foundations/README.md).
