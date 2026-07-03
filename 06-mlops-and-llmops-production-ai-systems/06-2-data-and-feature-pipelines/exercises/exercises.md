# Exercises: 6.2 Data & Feature Pipelines

Offline-first exercises that build “data pipeline muscle”: validation, feature correctness, and lineage.

## Exercise 1: Schema + Range Validation

Write `validate_table(df)` that checks:
- required columns exist,
- dtypes are as expected,
- simple range checks (e.g., non-negative age).

Expected outcome:
- invalid data fails fast with a clear error.

## Exercise 2: Dataset Fingerprint (Hash)

Compute a stable fingerprint for a DataFrame:
- sort columns,
- serialize deterministically (CSV bytes),
- hash with SHA-256.

Expected outcome:
- same data => same hash.

## Exercise 3: Point-in-Time Join (Toy)

Given:
- an events table with `(entity_id, event_time)`,
- a features table with `(entity_id, feature_time, value)`,

Join each event to the latest feature row with `feature_time <= event_time`.

Expected outcome:
- no “future leakage” in joined features.

## Exercise 4: Offline/Online Feature Consistency Check

Simulate:
- offline feature computed in batch,
- online feature computed in a streaming-like function.

Write a test that checks they match on the same input.

Expected outcome:
- you detect drift caused by different preprocessing.

## Exercise 5: Pipeline Metadata Record

Write a JSON metadata record containing:
- input dataset hash,
- output dataset hash,
- feature list,
- code version (git sha if available),
- timestamp.

Expected outcome:
- you can trace outputs back to inputs.

