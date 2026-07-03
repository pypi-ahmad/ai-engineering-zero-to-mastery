from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def _run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def test_end_to_end_pipeline(tmp_path: Path) -> None:
    """Smoke-test the full offline pipeline on a temp workspace.

    This avoids writing generated data/artifacts into the git working tree.
    """
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
    evaluate = repo_root / "projects" / "capstone-template" / "model" / "evaluate.py"

    _run([sys.executable, str(ingest), "--config", str(config), "--root", str(root)])
    _run([sys.executable, str(prepare), "--config", str(config), "--root", str(root)])
    _run([sys.executable, str(train), "--config", str(config), "--root", str(root)])
    _run([sys.executable, str(evaluate), "--config", str(config), "--root", str(root)])

    model_path = root / "artifacts" / "model.joblib"
    assert model_path.exists()

    metrics_train = root / "artifacts" / "metrics_train.json"
    metrics_eval = root / "artifacts" / "metrics_eval.json"
    assert metrics_train.exists()
    assert metrics_eval.exists()

    train_obj = json.loads(metrics_train.read_text(encoding="utf-8"))
    eval_obj = json.loads(metrics_eval.read_text(encoding="utf-8"))

    assert "metrics" in train_obj and "accuracy" in train_obj["metrics"]
    assert "metrics" in eval_obj and "accuracy" in eval_obj["metrics"]

