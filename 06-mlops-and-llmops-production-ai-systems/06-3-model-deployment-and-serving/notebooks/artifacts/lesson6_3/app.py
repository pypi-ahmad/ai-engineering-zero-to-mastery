from __future__ import annotations

import joblib
from fastapi import FastAPI
from pydantic import BaseModel, Field

MODEL_PATH = r"/home/ahmad/AI/Github/ai-engineering-zero-to-mastery/06-mlops-and-llmops-production-ai-systems/06-3-model-deployment-and-serving/notebooks/artifacts/lesson6_3/iris_rf.joblib"
model = joblib.load(MODEL_PATH)

app = FastAPI(title="Iris Model Service", version="1.0.0")


class IrisRequest(BaseModel):
    sepal_length_cm: float = Field(..., ge=0)
    sepal_width_cm: float = Field(..., ge=0)
    petal_length_cm: float = Field(..., ge=0)
    petal_width_cm: float = Field(..., ge=0)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/predict")
def predict(payload: IrisRequest) -> dict:
    x = [[
        payload.sepal_length_cm,
        payload.sepal_width_cm,
        payload.petal_length_cm,
        payload.petal_width_cm,
    ]]
    pred = int(model.predict(x)[0])
    probs = model.predict_proba(x)[0].tolist()
    return {"prediction": pred, "probabilities": probs}