#!/usr/bin/env python3
"""Validate repository curriculum integrity.

This script is intentionally stdlib-only so it can run in CI and in fresh clones
without needing the full ML stack installed.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


LESSON_DIR_RE = re.compile(r"^\d{2}-")


@dataclass(frozen=True)
class ValidationError:
    code: str
    message: str
    path: str | None = None

    def format(self) -> str:
        if self.path:
            return f"[{self.code}] {self.message} ({self.path})"
        return f"[{self.code}] {self.message}"


def _is_excluded(path: Path) -> bool:
    # Keep this conservative: ignore generated and tool folders, but validate all
    # curriculum content.
    parts = set(path.parts)
    return bool(
        parts.intersection(
            {
                ".git",
                ".venv",
                "__pycache__",
                ".ipynb_checkpoints",
                ".pytest_cache",
                ".ruff_cache",
                ".mypy_cache",
                "node_modules",
                ".firecrawl",
                ".codex",
                ".agents",
                "_artifacts",
                "_research",
            }
        )
    )


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def validate_structure(root: Path) -> list[ValidationError]:
    errors: list[ValidationError] = []

    lesson_dirs = sorted([p for p in root.iterdir() if p.is_dir() and LESSON_DIR_RE.match(p.name)])
    if len(lesson_dirs) != 15:
        errors.append(
            ValidationError(
                code="STRUCT001",
                message=f"Expected 15 lesson directories, found {len(lesson_dirs)}",
            )
        )

    for lesson in lesson_dirs:
        if not (lesson / "README.md").exists():
            errors.append(
                ValidationError(
                    code="STRUCT002",
                    message="Missing lesson README.md",
                    path=str(lesson / "README.md"),
                )
            )

        # Sub-lessons follow `<lesson_num>-<sub_num>-...`
        sub_lessons = sorted(
            [
                d
                for d in lesson.iterdir()
                if d.is_dir() and re.match(rf"^{lesson.name[:2]}-\d+", d.name)
            ]
        )
        if not sub_lessons:
            errors.append(
                ValidationError(
                    code="STRUCT003",
                    message="No sub-lessons found",
                    path=str(lesson),
                )
            )
            continue

        for sub in sub_lessons:
            readme = sub / "README.md"
            theory_dir = sub / "theory"
            notebooks_dir = sub / "notebooks"

            if not readme.exists():
                errors.append(
                    ValidationError(
                        code="STRUCT010",
                        message="Missing sub-lesson README.md",
                        path=str(readme),
                    )
                )

            theory_md = sorted(theory_dir.glob("*.md")) if theory_dir.exists() else []
            theory_pdf = sorted(theory_dir.glob("*.pdf")) if theory_dir.exists() else []
            notebooks = sorted(notebooks_dir.glob("*.ipynb")) if notebooks_dir.exists() else []

            if not theory_md:
                errors.append(
                    ValidationError(
                        code="STRUCT011",
                        message="Missing theory markdown",
                        path=str(theory_dir),
                    )
                )
            if not theory_pdf:
                errors.append(
                    ValidationError(
                        code="STRUCT012",
                        message="Missing theory PDF export",
                        path=str(theory_dir),
                    )
                )
            if not notebooks:
                errors.append(
                    ValidationError(
                        code="STRUCT013",
                        message="Missing teaching notebook(s)",
                        path=str(notebooks_dir),
                    )
                )

    return errors


def validate_notebooks(root: Path) -> list[ValidationError]:
    errors: list[ValidationError] = []
    notebooks = sorted(root.rglob("*.ipynb"))

    for nb in notebooks:
        if _is_excluded(nb):
            continue

        try:
            data = json.loads(nb.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001 - report as validation error
            errors.append(
                ValidationError(
                    code="NB001",
                    message=f"Notebook JSON parse error: {exc}",
                    path=str(nb),
                )
            )
            continue

        md_text = "\n".join(
            "".join(c.get("source", ""))
            for c in data.get("cells", [])
            if c.get("cell_type") == "markdown"
        ).lower()
        code_cells = [c for c in data.get("cells", []) if c.get("cell_type") == "code"]

        if "objective" not in md_text:
            errors.append(
                ValidationError(
                    code="NB010",
                    message="Notebook missing 'Objectives' section (keyword: objective)",
                    path=str(nb),
                )
            )
        if (
            "case studies" not in md_text
            and "case study" not in md_text
            and "exceptions" not in md_text
        ):
            errors.append(
                ValidationError(
                    code="NB011",
                    message="Notebook missing case studies/exceptions section",
                    path=str(nb),
                )
            )
        if "interview questions" not in md_text and "interview q&a" not in md_text:
            errors.append(
                ValidationError(
                    code="NB012",
                    message="Notebook missing interview Q&A section",
                    path=str(nb),
                )
            )
        if not code_cells:
            errors.append(
                ValidationError(
                    code="NB013",
                    message="Notebook has no code cells",
                    path=str(nb),
                )
            )

        # Optional: compile code cell sources (catches accidental syntax issues).
        for idx, cell in enumerate(code_cells):
            src = "".join(cell.get("source", ""))
            if not src.strip():
                continue
            # Skip notebook magics / shell escapes.
            lines = [
                ln
                for ln in src.splitlines()
                if not ln.lstrip().startswith(("%", "!", "?", "%%"))
            ]
            filtered = "\n".join(lines).strip()
            if not filtered:
                continue
            try:
                compile(filtered, f"{nb}#cell{idx}", "exec")
            except (SyntaxError, IndentationError) as exc:
                msg = f"{type(exc).__name__}: {getattr(exc, 'msg', str(exc))}"
                errors.append(
                    ValidationError(
                        code="NB020",
                        message=f"Notebook code cell does not compile: {msg}",
                        path=f"{nb}#cell{idx}",
                    )
                )

    return errors


def validate_placeholders(root: Path) -> list[ValidationError]:
    errors: list[ValidationError] = []
    tokens = ["TODO", "TBD", "Lorem ipsum"]

    # Placeholder scanning is intended for curriculum and runnable examples.
    # Avoid scanning tooling/docs that might legitimately mention these tokens.
    scan_roots = [
        p for p in root.iterdir() if p.is_dir() and LESSON_DIR_RE.match(p.name)
    ]
    projects = root / "projects"
    if projects.exists():
        scan_roots.append(projects)

    for scan_root in scan_roots:
        for path in scan_root.rglob("*"):
            if _is_excluded(path):
                continue
            if not path.is_file():
                continue
            if path.suffix not in {".md", ".py", ".txt", ".yml", ".yaml", ".toml"}:
                continue

            text = _read_text(path)
            for token in tokens:
                if token in text:
                    errors.append(
                        ValidationError(
                            code="PL001",
                            message=f"Placeholder token found: {token}",
                            path=str(path),
                        )
                    )

    return errors


def validate_readme_links(root: Path) -> list[ValidationError]:
    errors: list[ValidationError] = []
    readme = root / "README.md"
    if not readme.exists():
        return errors

    text = _read_text(readme)
    for match in re.findall(r"\]\((\./[^)#]+)\)", text):
        target = root / match[2:]
        if not target.exists():
            errors.append(
                ValidationError(
                    code="LINK001",
                    message=f"Broken README local link: {match}",
                    path=str(readme),
                )
            )

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]

    errors: list[ValidationError] = []
    errors.extend(validate_structure(root))
    errors.extend(validate_notebooks(root))
    errors.extend(validate_placeholders(root))
    errors.extend(validate_readme_links(root))

    if errors:
        print("Curriculum validation failed:")
        for err in errors:
            print("-", err.format())
        return 1

    print("Curriculum validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
