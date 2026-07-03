from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest


def _run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def test_api_contract(tmp_path: Path) -> None:
    pytest.importorskip("fastapi")
    pytest.importorskip("uvicorn")
    pytest.importorskip("pydantic")

    root = tmp_path / "capstone"
    (root / "configs").mkdir(parents=True, exist_ok=True)

    config = root / "configs" / "config.yaml"
    config.write_text(
        "\n".join(
            [
                "seed: 42",
                "paths:",
                "  raw_csv: data/raw/breast_cancer.csv",
                "  processed_train_csv: data/processed/train.csv",
                "  processed_test_csv: data/processed/test.csv",
                "  artifact_dir: artifacts",
                "split:",
                "  test_size: 0.25",
                "  stratify: true",
                "features:",
                "  - mean_radius",
                "  - mean_texture",
                "  - mean_perimeter",
                "  - mean_area",
                "  - mean_smoothness",
                "model:",
                "  type: logistic_regression",
                "  params:",
                "    max_iter: 2000",
                "    C: 1.0",
                "    solver: lbfgs",
                "",
            ]
        ),
        encoding="utf-8",
    )

    repo_root = Path(__file__).resolve().parents[3]
    ingest = repo_root / "projects" / "capstone-template" / "data" / "ingest.py"
    prepare = repo_root / "projects" / "capstone-template" / "data" / "prepare.py"
    train = repo_root / "projects" / "capstone-template" / "model" / "train.py"

    _run([sys.executable, str(ingest), "--config", str(config), "--root", str(root)])
    _run([sys.executable, str(prepare), "--config", str(config), "--root", str(root)])
    _run([sys.executable, str(train), "--config", str(config), "--root", str(root)])

    api_mod_path = repo_root / "projects" / "capstone-template" / "serve" / "api.py"

    import importlib.util

    spec = importlib.util.spec_from_file_location("capstone_api", api_mod_path)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[union-attr]

    # Build app against the temp workspace model artifact.
    model_path = root / "artifacts" / "model.joblib"
    app = mod.create_app(model_path=model_path)

    # Avoid network/socket usage in restricted sandboxes by calling route endpoints directly.
    from fastapi.routing import APIRoute

    routes = {r.path: r for r in app.routes if isinstance(r, APIRoute)}
    assert "/health" in routes
    assert "/predict" in routes

    health_out = routes["/health"].endpoint()  # type: ignore[call-arg]
    assert health_out == {"status": "ok"}

    payload = SimpleNamespace(
        mean_radius=14.0,
        mean_texture=20.0,
        mean_perimeter=90.0,
        mean_area=600.0,
        mean_smoothness=0.1,
    )
    pred_out = routes["/predict"].endpoint(payload)  # type: ignore[misc]
    assert set(pred_out.keys()) == {"prediction", "probabilities"}
    assert isinstance(pred_out["prediction"], int)
    assert isinstance(pred_out["probabilities"], list)
    assert len(pred_out["probabilities"]) == 2
