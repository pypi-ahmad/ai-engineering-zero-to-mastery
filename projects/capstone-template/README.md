# Capstone Template (Beginner-First)

This is a runnable, offline-friendly capstone scaffold that demonstrates the full AI engineering loop:

- data ingestion (offline, built-in dataset)
- train/validation split (fit preprocessing on train only)
- model training + metrics logging
- model evaluation + artifact persistence
- a simple prediction API contract (FastAPI)

## Quickstart

From the repository root:

```bash
uv sync --frozen --group dev
uv run python projects/capstone-template/data/ingest.py
uv run python projects/capstone-template/data/prepare.py
uv run python projects/capstone-template/model/train.py
uv run python projects/capstone-template/model/evaluate.py
```

Expected outputs:

- `projects/capstone-template/data/raw/breast_cancer.csv`
- `projects/capstone-template/data/processed/train.csv`
- `projects/capstone-template/data/processed/test.csv`
- `projects/capstone-template/artifacts/model.joblib`
- `projects/capstone-template/artifacts/metrics_train.json`
- `projects/capstone-template/artifacts/metrics_eval.json`

## Serving (optional)

Install the serving extra:

```bash
uv sync --frozen --extra serving
```

Run the API:

```bash
uv run uvicorn serve.api:app --app-dir projects/capstone-template --reload
```

Then test:

```bash
curl -s http://127.0.0.1:8000/health
```

## Testing

```bash
uv sync --frozen --extra serving --group dev
uv run pytest -q
```

## Notes for beginners

- This template uses `sklearn.datasets.load_breast_cancer` to avoid data download friction.
- Replace the dataset and model once you’re comfortable with the end-to-end flow.
- Keep the same discipline when you swap data:
  - fit preprocessing on train only
  - log metrics and artifacts
  - keep input/output schemas explicit
