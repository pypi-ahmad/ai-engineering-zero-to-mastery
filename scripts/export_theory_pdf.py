#!/usr/bin/env python3
"""Export lesson markdown files to PDF using pandoc."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def export_one(src: Path, dst: Path) -> int:
    if not src.exists():
        print(f"PDF export failed: source file not found: {src}")
        return 1

    dst.parent.mkdir(parents=True, exist_ok=True)
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
        print(f"PDF export failed for {src}")
        print(result.stderr)
        return result.returncode
    print(f"PDF generated: {dst}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Export lesson markdown files to PDF using pandoc.")
    parser.add_argument(
        "--src",
        type=Path,
        default=None,
        help="Path to source markdown file.",
    )
    parser.add_argument(
        "--dst",
        type=Path,
        default=None,
        help="Path to output PDF file.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Export all markdown files under */*/theory/ and */*/ */theory/ patterns for lessons 1-3.",
    )
    args = parser.parse_args()

    if args.all:
        theory_roots = [
            Path("01-foundations-of-computing-and-programming"),
            Path("02-mathematics-for-ai"),
            Path("03-classical-machine-learning"),
        ]
        md_files: list[Path] = []
        for root in theory_roots:
            if root.exists():
                md_files.extend(root.rglob("theory/*.md"))
        md_files = sorted(md_files)
        if not md_files:
            print("No theory markdown files found.")
            return 1

        failures = 0
        for src in md_files:
            dst = src.with_suffix(".pdf")
            failures += export_one(src, dst)
        return 1 if failures else 0

    src = args.src
    dst = args.dst
    if src is None:
        src = Path("01-foundations-of-computing-and-programming/01-1-programming-basics/theory/01-1-programming-basics.md")
    if dst is None:
        dst = src.with_suffix(".pdf")
    return export_one(src, dst)


if __name__ == "__main__":
    raise SystemExit(main())
