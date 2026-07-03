# Exercises: 6.3 Model Deployment & Serving

Prerequisite (recommended):

```bash
uv sync --frozen --extra serving --group dev
```

## Exercise 1: Request/Response Schemas (Pydantic)

Define request/response models for a prediction endpoint with:
- typed fields,
- basic range validation,
- explicit output schema.

Expected outcome:
- bad inputs are rejected with a clear error.

## Exercise 2: Contract Test (FastAPI TestClient)

Write a contract test that checks:
- `GET /health` returns 200 + JSON status,
- `POST /predict` returns a JSON object with required fields.

Expected outcome:
- test fails if schema changes unexpectedly.

## Exercise 3: Versioned Endpoints (v1/v2)

Add:
- `/v1/predict` and `/v2/predict`

Expected outcome:
- you can ship a change without breaking old clients immediately.

## Exercise 4: Canary Routing (Toy)

Implement a routing function that sends:
- `p%` of requests to v2,
- the rest to v1,
based on a stable hash of `request_id`.

Expected outcome:
- routing is deterministic per `request_id`.

## Exercise 5: Lazy Model Load

Implement lazy model loading:
- model loaded once on first request,
- cached for later requests.

Expected outcome:
- avoids “import-time” crashes and reduces cold start surprises.

