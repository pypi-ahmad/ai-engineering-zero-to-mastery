# Overview

AI engineers frequently integrate external services and serve models through APIs. Understanding HTTP and JSON is essential for reliable model serving, microservice integration, and production monitoring.

# HTTP Basics

Common HTTP methods:
- `GET`: read data.
- `POST`: create data or request an action.
- `PUT`: replace/update data.
- `DELETE`: remove data.

Important status codes:
- `200` success
- `400` bad request
- `401` unauthorized
- `404` not found
- `500` server error

# JSON Basics

JSON represents structured data using key-value pairs, arrays, and nested objects. It is the most common payload format in modern APIs.

# REST API Patterns

REST APIs organize access around resources and endpoints, for example:
- `/posts`
- `/users/1`

Query parameters (e.g., `?userId=1`) help filter and paginate results.

# AI Engineering Use Cases

- Calling external APIs (LLM providers, feature services, metadata services).
- Serving model predictions through REST endpoints consumed by product applications.

# Common Pitfalls

- Not handling non-200 responses and timeouts correctly.
- Assuming response shape is always valid JSON without checks.

# Interview Prep Checklist

- Describe a simple REST endpoint design and request/response flow.
- Explain how to call an API from Python and parse JSON safely.
- Explain how to add retries, timeout handling, and response validation.
