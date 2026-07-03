# Setup and Troubleshooting

This repo uses **uv** for reproducible Python environments.

## Prerequisites

- Python: 3.10+
- OS: Linux/macOS/Windows (WSL2 is fine)
- Disk: enough for ML packages (especially if you install deep learning extras)

## Setup (Recommended)

```bash
uv venv --python 3.12
source .venv/bin/activate
uv sync --frozen --group dev
jupyter lab
```

If you are new to environments: the virtual environment lives at `.venv/`.

## Optional Extras (Install When Needed)

```bash
# Deep learning (torch/vision)
uv sync --frozen --extra dl

# GenAI / LLM lessons (HF stack + PEFT/TRL)
uv sync --frozen --extra genai

# RL demos
uv sync --frozen --extra rl

# Serving demos + capstone API
uv sync --frozen --extra serving

# Ops / experiment tracking
uv sync --frozen --extra ops
```

## Troubleshooting

### uv sync fails

1. Ensure you activated the environment: `source .venv/bin/activate`
2. Try clearing uv cache if needed:
   - `uv cache clean`
3. If you are behind a proxy or have restrictive DNS, configure your network or use a different network.

### Jupyter kernel doesn’t show the venv

Install `ipykernel` (already included in base deps) and restart:

```bash
uv sync --frozen
```

Then restart Jupyter Lab.

### Torch install issues

Torch wheels vary by OS, Python version, and GPU/CUDA setup. If `uv sync --extra dl` fails:

- Try a different Python version (3.12 tends to be the most compatible).
- If you need GPU acceleration, follow PyTorch’s official install matrix for your platform.

### Notebook runs but results differ

Most notebooks set seeds, but results can still vary due to:

- nondeterministic GPU kernels,
- library version differences,
- randomization in data splits or sampling.

If determinism matters, run on CPU, pin versions via `uv.lock`, and keep seeds fixed.

