# Setup and Troubleshooting

This repo uses **uv** for reproducible Python environments.

## Prerequisites

- Python: 3.10+
- OS: Linux/macOS/Windows (WSL2 is fine)
- Disk: enough for ML packages (especially if you install deep learning extras)

## Install uv

Follow the official installer instructions (recommended):

- Linux/macOS:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

- Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

More install options (Homebrew, WinGet, Scoop, etc.) are in the uv docs:
https://docs.astral.sh/uv/getting-started/installation/

## Setup (Recommended)

```bash
uv venv --python 3.12
source .venv/bin/activate
uv sync --frozen --group dev
jupyter lab
```

If you are new to environments: the virtual environment lives at `.venv/`.

## Quick Verification (Recommended)

From the repo root, verify the curriculum structure and links:

```bash
python3 scripts/validate_curriculum.py
```

If you already have a working `.venv/`, verify the runnable scaffold tests:

```bash
.venv/bin/python -m pytest -q
```

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

### `python` not found (only `python3` exists)

Some systems do not provide a `python` alias. Use:
- `python3 ...` for scripts, or
- `uv run python ...` for reproducible runs inside the uv environment.

### uv sync fails

1. Ensure you activated the environment: `source .venv/bin/activate`
2. Try clearing uv cache if needed:
   - `uv cache clean`
3. If you are behind a proxy or have restrictive DNS, configure your network or use a different network.

If your home directory is read-only (common in some sandboxes/containers), set the uv cache to a writable location:

```bash
mkdir -p /tmp/uv-cache
UV_CACHE_DIR=/tmp/uv-cache XDG_CACHE_HOME=/tmp uv sync --frozen --group dev
```

### Jupyter kernel doesn’t show the venv

Install `ipykernel` (already included in base deps) and restart:

```bash
uv sync --frozen
```

Then restart Jupyter Lab.

If you still don’t see the right kernel, run notebooks from the activated environment and prefer:
- Jupyter started after `source .venv/bin/activate`
- `uv run jupyter lab` if you suspect PATH confusion

### Torch install issues

Torch wheels vary by OS, Python version, and GPU/CUDA setup. If `uv sync --frozen --extra dl` fails:

- Try a different Python version (3.12 tends to be the most compatible).
- If you need GPU acceleration, follow PyTorch’s official install matrix for your platform.

### Notebook runs but results differ

Most notebooks set seeds, but results can still vary due to:

- nondeterministic GPU kernels,
- library version differences,
- randomization in data splits or sampling.

If determinism matters, run on CPU, pin versions via `uv.lock`, and keep seeds fixed.

## Common Setup Mistakes

- Installing every optional extra on day 1 (install extras only when you reach those lessons).
- Running `jupyter lab` before activating `.venv/` (you end up on a different Python).
- Mixing system Python + venv Python in the same session.
