#!/usr/bin/env python3
from __future__ import annotations

import argparse
import logging
from pathlib import Path
from typing import Any

import joblib
import yaml

try:
    from fastapi import FastAPI
    from pydantic import BaseModel, Field
except Exception:  # noqa: BLE001 - keep import-time failures actionable for beginners
    FastAPI = None  # type: ignore[assignment]
    BaseModel = object  # type: ignore[assignment]
    Field = None  # type: ignore[assignment]


logger = logging.getLogger(__name__)


def _project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _load_config(config_path: Path) -> dict[str, Any]:
    data = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("config must be a YAML mapping")
    return data


def create_app(*, model_path: Path) -> Any:
    if FastAPI is None or Field is None:
        raise RuntimeError(
            "FastAPI is not installed. Install it with: uv sync --frozen --extra serving"
        )

    model = joblib.load(model_path)
    app = FastAPI(title="Capstone Template API", version="1.0.0")

    class PredictRequest(BaseModel):
        # Breast cancer dataset features (subset of typical scalars).
        mean_radius: float = Field(..., ge=0)
        mean_texture: float = Field(..., ge=0)
        mean_perimeter: float = Field(..., ge=0)
        mean_area: float = Field(..., ge=0)
        mean_smoothness: float = Field(..., ge=0)

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.post("/predict")
    def predict(payload: PredictRequest) -> dict[str, Any]:
        import pandas as pd

        x = pd.DataFrame(
            [
                {
                    "mean_radius": payload.mean_radius,
                    "mean_texture": payload.mean_texture,
                    "mean_perimeter": payload.mean_perimeter,
                    "mean_area": payload.mean_area,
                    "mean_smoothness": payload.mean_smoothness,
                }
            ]
        )
        pred = int(model.predict(x)[0])
        probs = model.predict_proba(x)[0].tolist()
        return {"prediction": pred, "probabilities": probs}

    return app


def create_app_stub(*, model_path: Path) -> Any:
    """Create an app that starts even if the model artifact is missing.

    This is helpful for beginners: the server can start, and endpoints return a
    clear actionable error until training is run.
    """
    if FastAPI is None or Field is None:
        raise RuntimeError(
            "FastAPI is not installed. Install it with: uv sync --frozen --extra serving"
        )

    from fastapi import HTTPException

    app = FastAPI(title="Capstone Template API", version="1.0.0")
    app.state.model = joblib.load(model_path) if model_path.exists() else None

    class PredictRequest(BaseModel):
        mean_radius: float = Field(..., ge=0)
        mean_texture: float = Field(..., ge=0)
        mean_perimeter: float = Field(..., ge=0)
        mean_area: float = Field(..., ge=0)
        mean_smoothness: float = Field(..., ge=0)

    @app.get("/health")
    def health() -> dict[str, str]:
        status = "ok" if app.state.model is not None else "model_missing"
        return {"status": status}

    @app.post("/predict")
    def predict(payload: PredictRequest) -> dict[str, Any]:
        if app.state.model is None:
            raise HTTPException(
                status_code=503,
                detail="Model artifact missing. Run model/train.py to generate artifacts.",
            )
        import pandas as pd

        x = pd.DataFrame(
            [
                {
                    "mean_radius": payload.mean_radius,
                    "mean_texture": payload.mean_texture,
                    "mean_perimeter": payload.mean_perimeter,
                    "mean_area": payload.mean_area,
                    "mean_smoothness": payload.mean_smoothness,
                }
            ]
        )
        pred = int(app.state.model.predict(x)[0])
        probs = app.state.model.predict_proba(x)[0].tolist()
        return {"prediction": pred, "probabilities": probs}

    return app


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    parser = argparse.ArgumentParser(description="Run the capstone template FastAPI server.")
    parser.add_argument(
        "--config",
        type=Path,
        default=_project_root() / "configs" / "config.yaml",
        help="Path to config YAML.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=_project_root(),
        help="Project root for resolving relative paths.",
    )
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    cfg = _load_config(args.config)
    model_path = args.root / str(cfg["paths"]["artifact_dir"]) / "model.joblib"
    if not model_path.exists():
        raise FileNotFoundError(f"model artifact not found: {model_path}. Run train.py first.")

    app = create_app(model_path=model_path)

    import uvicorn  # local import to keep base deps light

    logger.info("Starting server. host=%s port=%s model=%s", args.host, args.port, model_path)
    uvicorn.run(app, host=args.host, port=args.port)
    return 0


cfg_default = _load_config(_project_root() / "configs" / "config.yaml")
model_path_default = _project_root() / str(cfg_default["paths"]["artifact_dir"]) / "model.joblib"
app = create_app_stub(model_path=model_path_default)


if __name__ == "__main__":
    raise SystemExit(main())
