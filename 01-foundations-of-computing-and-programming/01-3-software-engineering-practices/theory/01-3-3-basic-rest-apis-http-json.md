# Overview

AI systems are integration-heavy. Even if modeling code is correct, weak API design or unsafe client behavior can break production workflows.

This chapter covers HTTP/JSON fundamentals, REST patterns, resilience patterns, and practical failure handling.

# HTTP Basics

An HTTP request has:
- Method
- URL
- Headers
- Optional body

Common methods:
- `GET`: retrieve resource
- `POST`: create or trigger processing
- `PUT`: full replacement
- `PATCH`: partial update
- `DELETE`: remove resource

Status code families:
- `2xx`: success
- `4xx`: client/request issue
- `5xx`: server/internal issue

Operational rule:
Always treat non-2xx responses as explicit branches in control flow.

# JSON Basics

JSON value types:
- object, array
- string, number, boolean
- null

Common data quality hazards:
- Missing keys
- Null where numeric expected
- Type drift (`"42"` vs `42`)

Formal validation objective:
Given payload $p$, validate $p \in S$ where $S$ is a predefined schema set.

# REST API Patterns

REST-oriented design patterns:
- Resource nouns in endpoints (`/v1/predictions`, `/v1/features/{id}`)
- Stateless requests
- Predictable method semantics

Frequent patterns:
- Pagination (`page`, `limit`, cursors)
- Filtering/sorting query params
- Versioned endpoints (`/v1`, `/v2`)
- Idempotency keys for retried write operations

# Reliability Patterns for API Clients

1. Timeout control
- Never call remote APIs without timeouts.

2. Retry with bounded exponential backoff
- Retry transient failures (`429`, `502`, `503`, `504`) with cap.

3. Circuit breaker behavior
- Stop hammering failing dependencies; fallback to degraded mode.

4. Schema validation on responses
- Validate before downstream feature/model use.

Diagram in words:
Client request -> Timeout guard -> Retry policy -> Response validation -> Business logic.
Each stage isolates one failure class.

# AI Engineering Use Cases

- Calling LLM or embedding APIs.
- Pulling real-time features from feature services.
- Serving model predictions over HTTP.
- Emitting inference traces to monitoring pipelines.

# Worked Example: Prediction API Contract

Example request payload:

```json
{
  "customer_id": "C12345",
  "features": {
    "age": 34,
    "income": 92000
  }
}
```

Example success response:

```json
{
  "prediction": 0.83,
  "label": "high_risk",
  "model_version": "credit-risk-v3.2.1",
  "request_id": "req-78f0"
}
```

Example error response:

```json
{
  "error_code": "INVALID_SCHEMA",
  "message": "Missing required key: features.income",
  "request_id": "req-78f0"
}
```

Contract rule:
- success and error payloads should be schema-stable and machine-readable.
- include request IDs for debugging and incident forensics.

# Edge Cases and Failure Handling

1. **Partial payloads**
- Return `400` with explicit missing-field details.
- Avoid silent defaults for high-risk inputs.

2. **Duplicate writes with retries**
- Use idempotency keys for mutation endpoints.
- Prevent duplicate side effects (for example double-charging).

3. **Upstream timeout with stale cache**
- Serve cached response only if freshness policy allows it.
- Include degraded-mode metadata in the response.

4. **Unexpected content type**
- Reject non-JSON payloads with clear `415` path.
- Log sanitized headers for diagnostics.

# Common Pitfalls

- Infinite/very long request timeout.
- Parsing `.json()` before checking status/content type.
- Treating all failures as retryable.
- Logging sensitive payloads (PII/secrets) in plain text.

# Business Case Studies & Exceptions

## Case 1: Timeout Cascade in Recommendation API

Scenario:
Downstream feature API latency spikes; upstream inference workers block waiting.

Impact:
- Thread pool exhaustion
- End-user latency spikes
- Partial outage

Fix pattern:
- Per-call timeout
- Capped retries
- Fallback to cached/partial features

Exception:
For financial/risk-critical predictions, fallback may be disallowed; fail closed and escalate.

## Case 2: Schema Drift in Vendor API

Scenario:
Vendor renamed `score` to `risk_score` without notice.

Impact:
Parser breaks or silently reads null.

Fix pattern:
- Strict schema validation layer.
- Alert on contract mismatch.
- Temporary compatibility mapper while vendor migration completes.

## Case 3: Retry Storm During Incident

Scenario:
All clients retry aggressively on 503 and amplify outage.

Fix pattern:
- Jittered backoff
- Retry budget
- Circuit breaker threshold

# Interview Questions & Answers

1. **Q: Why must API clients set explicit timeouts?**
   **A:** Without timeouts, blocked calls can exhaust workers and trigger cascading failures.

2. **Q: Why check status code before parsing JSON?**
   **A:** Error pages may be non-JSON or different schema, causing parse or semantic failures.

3. **Q: What is idempotency and why does it matter?**
   **A:** Repeated request has same effect; it enables safe retries for write endpoints.

4. **Q: Which errors are usually retryable?**
   **A:** Transient network/service errors (e.g., 429, 502, 503, 504), not validation errors.

5. **Q: What should be logged for failed API calls?**
   **A:** Endpoint, method, status, latency, correlation/request ID, retry count, and sanitized error details.

6. **Q: Why do schema contracts matter in AI systems?**
   **A:** Contract drift can poison feature pipelines or invalidate predictions.

7. **Q: GET vs POST for inference endpoints?**
   **A:** POST is preferred when payloads are non-trivial and semantics are action-oriented.

8. **Q: What is a circuit breaker?**
   **A:** A guard that stops repeated failing calls temporarily and enables degraded/fallback behavior.

9. **Q: How do you design robust prediction API responses?**
   **A:** Include prediction, confidence/metadata, model version, and structured error payloads.

10. **Q: What is one security rule for API integrations?**
    **A:** Keep credentials in environment/secret manager and never hardcode tokens in code or notebooks.

11. **Q: Why include request IDs in both success and error responses?**
    **A:** They enable traceability across logs, retries, and incident investigations.

12. **Q: What is a safe default for unknown payload fields?**
    **A:** Reject or explicitly ignore with validation policy; never silently reinterpret fields.

13. **Q: Why are idempotency keys important for payment or ticket actions?**
    **A:** They prevent duplicate state changes during network retries.

14. **Q: What should happen if fallback data is stale?**
    **A:** Return explicit degraded-mode metadata or fail closed based on risk policy.

15. **Q: Why separate client and server error classes operationally?**
    **A:** They drive different remediation paths: request fixes vs service reliability fixes.

# References

- HTTP semantics (IETF): https://httpwg.org/specs/rfc9110.html
- REST API design guide (Microsoft): https://learn.microsoft.com/azure/architecture/best-practices/api-design
- Requests docs: https://requests.readthedocs.io/

## Bridge to Next Lesson

- **What you now know:** You can now write reliable Python code, reason about data structures, and apply core software engineering workflows (Git, modular design, and API fundamentals).
- **Why the next lesson follows:** The next lesson follows because strong AI systems depend on mathematical intuition for modeling, optimization, and uncertainty, not only code execution.
- **What you'll build next:** You will build mathematical fluency in linear algebra, calculus, probability, and applied statistics to support ML design and evaluation.

