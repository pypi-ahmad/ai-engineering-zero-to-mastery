#!/usr/bin/env python3
"""Export lesson markdown to PDF using pandoc."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Export a markdown theory lesson to PDF using pandoc.")
    parser.add_argument(
        "--src",
        type=Path,
        default=Path("foundations-of-computing-and-programming/theory/lesson-01-python-and-jupyter-basics.md"),
        help="Path to source markdown file.",
    )
    parser.add_argument(
        "--dst",
        type=Path,
        default=Path("foundations-of-computing-and-programming/theory/lesson-01-python-and-jupyter-basics.pdf"),
        help="Path to output PDF file.",
    )
    args = parser.parse_args()

    src = args.src
    dst = args.dst

    if not src.exists():
        print(f"PDF export failed: source file not found: {src}")
        return 1

    cmd = [
        "pandoc",
        str(src),
        "-o",
        str(dst),
        "--pdf-engine=xelatex",
        "-V",
        "geometry:margin=1in",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("PDF export failed")
        print(result.stderr)
        return result.returncode

    print(f"PDF generated: {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
