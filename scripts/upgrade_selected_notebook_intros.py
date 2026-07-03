#!/usr/bin/env python3
"""Upgrade intros for a small set of beginner-critical notebooks.

We intentionally do NOT rewrite every notebook in the repo. This script targets
only a few "first win" notebooks to make execution + verification explicit for
complete beginners.

Stdlib-only so it can run in fresh clones.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


NOTEBOOKS: dict[str, str] = {
    # Lesson 1.1
    "01-foundations-of-computing-and-programming/01-1-programming-basics/notebooks/01-1-programming-basics.ipynb": """\

## How to run (recommended)
- Restart kernel -> Run all.
- If imports fail, you are likely on the wrong Python kernel. See `docs/setup-and-troubleshooting.md`.

## Verify
- Change one small thing (a parameter or function) and predict what will change before rerunning.
- After you run this once, do `exercises/` for 1.1 and compare with `solutions.md`.
""",
    # Lesson 3.1
    "03-classical-machine-learning/03-1-supervised-learning/notebooks/03-1-supervised-learning.ipynb": """\

## How to run (recommended)
- Restart kernel -> Run all.
- Keep your train/test split fixed while comparing models (otherwise comparisons are noisy).

## Verify
- Record one baseline metric (and the split/seed used).
- Compare two model families and explain the tradeoff (performance vs interpretability vs cost).
""",
    # Lesson 3.3
    "03-classical-machine-learning/03-3-model-evaluation-and-selection/notebooks/03-3-model-evaluation-and-selection.ipynb": """\

## How to run (recommended)
- Restart kernel -> Run all.
- Do not touch the test set until the end (use it once).

## Verify
- Add one explicit leakage check to your workflow.
- Write down the metric + threshold you would use as a release gate.
""",
}


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _dump(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=1) + "\n", encoding="utf-8")


def _first_markdown_cell(cells: list[dict]) -> int | None:
    for i, c in enumerate(cells):
        if c.get("cell_type") == "markdown":
            return i
    return None


def upgrade_one(rel: str, addition: str) -> bool:
    nb_path = ROOT / rel
    data = _load(nb_path)
    cells = data.get("cells", [])
    idx = _first_markdown_cell(cells)
    if idx is None:
        return False

    src = "".join(cells[idx].get("source", []))
    if "## How to run" in src or "## Verify" in src:
        return False

    # Preserve existing content, append an explicit run/verify block.
    new_src = src.rstrip() + "\n" + addition.lstrip("\n")
    cells[idx]["source"] = [line if line.endswith("\n") else line + "\n" for line in new_src.splitlines()]
    data["cells"] = cells
    _dump(nb_path, data)
    return True


def main() -> int:
    changed = 0
    for rel, addition in NOTEBOOKS.items():
        if upgrade_one(rel, addition):
            changed += 1
    print(f"upgraded_notebooks={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

