# Solutions: 6.3 Model Deployment & Serving

## Exercise 1: Request/Response Schemas (Pydantic)

```python
from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    x1: float = Field(..., ge=-1e6, le=1e6)
    x2: float = Field(..., ge=-1e6, le=1e6)


class PredictResponse(BaseModel):
    prediction: int
    score: float = Field(ge=0.0, le=1.0)
```

## Exercise 2–5: Minimal FastAPI App Sketch

```python
from __future__ import annotations

import hashlib
from functools import lru_cache

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class PredictRequest(BaseModel):
    x1: float = Field(..., ge=-1e6, le=1e6)
    x2: float = Field(..., ge=-1e6, le=1e6)


@lru_cache(maxsize=1)
def load_model() -> object:
    # Replace with real model loading logic.
    return {"version": "v1"}


def canary_route(request_id: str, percent_to_v2: float) -> str:
    if not (0.0 <= percent_to_v2 <= 1.0):
        raise ValueError("percent_to_v2 must be in [0,1]")
    h = hashlib.sha256(request_id.encode("utf-8")).hexdigest()
    bucket = int(h[:8], 16) / 0xFFFFFFFF
    return "v2" if bucket < percent_to_v2 else "v1"


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/v1/predict")
def predict_v1(payload: PredictRequest) -> dict:
    _model = load_model()
    score = 1.0 / (1.0 + abs(payload.x1 - payload.x2))
    pred = int(payload.x1 > payload.x2)
    return {"prediction": pred, "score": float(score), "model_version": "v1"}


@app.post("/v2/predict")
def predict_v2(payload: PredictRequest) -> dict:
    score = 1.0 / (1.0 + abs(payload.x1 - payload.x2))
    pred = int(payload.x1 >= payload.x2)
    return {"prediction": pred, "score": float(score), "model_version": "v2"}


@app.post("/predict")
def predict(payload: PredictRequest, request_id: str = "default") -> dict:
    route = canary_route(request_id=request_id, percent_to_v2=0.1)
    if route == "v2":
        return predict_v2(payload)
    return predict_v1(payload)
```

Example pytest contract test:

```python
from fastapi.testclient import TestClient

from your_app import app

client = TestClient(app)


def test_health() -> None:
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_predict_contract() -> None:
    r = client.post("/predict", json={"x1": 1.0, "x2": 2.0})
    assert r.status_code == 200
    body = r.json()
    assert "prediction" in body
    assert "score" in body
    assert "model_version" in body
```

