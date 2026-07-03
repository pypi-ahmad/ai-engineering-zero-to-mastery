#!/usr/bin/env python3
"""Validate repository curriculum integrity.

This script is intentionally stdlib-only so it can run in CI and in fresh clones
without needing the full ML stack installed.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


LESSON_DIR_RE = re.compile(r"^\d{2}-")
ABS_REPO_PATH_RE = re.compile(
    r"(?i)(/home/|/users/|[a-zA-Z]:\\\\)[^\\s\"']*ai-engineering-zero-to-mastery"
)


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


def _git_tracked_files(root: Path) -> list[Path]:
    """Return git-tracked files under root.

    This avoids false-failing when learners generate local artifacts that are
    gitignored (e.g., notebook outputs, artifacts, downloaded datasets).
    """
    try:
        out = subprocess.check_output(
            ["git", "-C", str(root), "ls-files"], text=True, stderr=subprocess.DEVNULL
        )
    except Exception:
        return []
    return [root / line for line in out.splitlines() if line.strip()]


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


def validate_exercises(root: Path) -> list[ValidationError]:
    """Require a consistent practice loop for the early curriculum.

    Lessons 1-6 are designed to be beginner-first with a predictable cadence:
    theory -> notebook -> exercises -> solutions. Later lessons may add practice
    content iteratively without being blocked by CI.
    """
    errors: list[ValidationError] = []

    lesson_dirs = sorted([p for p in root.iterdir() if p.is_dir() and LESSON_DIR_RE.match(p.name)])
    for lesson in lesson_dirs:
        try:
            lesson_num = int(lesson.name[:2])
        except Exception:
            continue
        if lesson_num > 6:
            continue

        sub_lessons = sorted(
            [
                d
                for d in lesson.iterdir()
                if d.is_dir() and re.match(rf"^{lesson.name[:2]}-\d+", d.name)
            ]
        )
        for sub in sub_lessons:
            exercises_dir = sub / "exercises"
            exercises_md = exercises_dir / "exercises.md"
            solutions_md = exercises_dir / "solutions.md"

            if not exercises_dir.exists():
                errors.append(
                    ValidationError(
                        code="EX001",
                        message="Missing exercises/ directory (Lessons 1-6 require practice loop)",
                        path=str(exercises_dir),
                    )
                )
            else:
                if not exercises_md.exists():
                    errors.append(
                        ValidationError(
                            code="EX002",
                            message="Missing exercises/exercises.md",
                            path=str(exercises_md),
                        )
                    )
                if not solutions_md.exists():
                    errors.append(
                        ValidationError(
                            code="EX003",
                            message="Missing exercises/solutions.md",
                            path=str(solutions_md),
                        )
                    )

            readme = sub / "README.md"
            if readme.exists():
                txt = _read_text(readme)
                if "## Practice (Recommended)" not in txt:
                    errors.append(
                        ValidationError(
                            code="EX010",
                            message="Sub-lesson README missing 'Practice (Recommended)' section (Lessons 1-6)",
                            path=str(readme),
                        )
                    )
                if "exercises/exercises.md" not in txt or "exercises/solutions.md" not in txt:
                    errors.append(
                        ValidationError(
                            code="EX011",
                            message="Sub-lesson README missing links to exercises + solutions (Lessons 1-6)",
                            path=str(readme),
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


def _iter_markdown_links(text: str) -> list[str]:
    # Minimal link matcher: ignores nested-paren edge cases (rare in this repo).
    return re.findall(r"\]\(([^)]+)\)", text)


def _strip_fenced_code_blocks(text: str) -> str:
    """Remove fenced code blocks so code like `fn(x)` doesn't look like `](x)` links."""
    out_lines: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            out_lines.append(line)
    return "\n".join(out_lines)


def validate_markdown_links(root: Path) -> list[ValidationError]:
    errors: list[ValidationError] = []
    tracked = _git_tracked_files(root)
    md_files = [p for p in tracked if p.suffix == ".md"] if tracked else sorted(root.rglob("*.md"))

    for md in md_files:
        if _is_excluded(md):
            continue
        text = _strip_fenced_code_blocks(_read_text(md))
        for raw in _iter_markdown_links(text):
            link = raw.strip()
            if not link:
                continue
            if link.startswith("#"):
                continue
            if link.startswith(("http://", "https://", "mailto:")):
                continue
            if "://" in link:
                continue

            # Strip anchors and decode minimal URL-escapes used in local paths.
            link = link.split("#", 1)[0].replace("%20", " ")
            if not link:
                continue

            if link.startswith("/"):
                target = root / link.lstrip("/")
            else:
                target = (md.parent / link).resolve()

            try:
                target.relative_to(root.resolve())
            except Exception:
                errors.append(
                    ValidationError(
                        code="LINK900",
                        message=f"Suspicious local link outside repo: {raw}",
                        path=str(md),
                    )
                )
                continue

            if not target.exists():
                errors.append(
                    ValidationError(
                        code="LINK001",
                        message=f"Broken local link: {raw}",
                        path=str(md),
                    )
                )

    return errors


def validate_tracked_hygiene(root: Path) -> list[ValidationError]:
    """Ensure we don't ship generated artifacts, datasets, or maintainer dumps."""
    errors: list[ValidationError] = []
    tracked = _git_tracked_files(root)
    if not tracked:
        return errors

    forbidden_substrings = [
        "/notebooks/artifacts/",
        "/notebooks/data/",
        "docs/_artifacts/",
        "docs/_research/firecrawl/",
        "docs/superpowers/",
    ]
    for path in tracked:
        rel = str(path.relative_to(root)).replace("\\", "/")
        for sub in forbidden_substrings:
            if sub in rel:
                errors.append(
                    ValidationError(
                        code="HYGIENE001",
                        message=f"Generated/maintainer-only content must not be tracked: {rel}",
                        path=str(path),
                    )
                )
                break
    return errors


def validate_no_absolute_repo_paths(root: Path) -> list[ValidationError]:
    """Reject machine-specific absolute paths that mention the repo name."""
    errors: list[ValidationError] = []
    tracked = _git_tracked_files(root)
    if not tracked:
        return errors

    text_exts = {".md", ".py", ".ipynb", ".json", ".yml", ".yaml", ".toml", ".txt"}
    for path in tracked:
        if path.suffix not in text_exts:
            continue
        if _is_excluded(path):
            continue
        text = _read_text(path)
        if ABS_REPO_PATH_RE.search(text):
            errors.append(
                ValidationError(
                    code="PATH001",
                    message="Machine-specific absolute path containing repo name found",
                    path=str(path),
                )
            )
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]

    errors: list[ValidationError] = []
    errors.extend(validate_structure(root))
    errors.extend(validate_notebooks(root))
    errors.extend(validate_exercises(root))
    errors.extend(validate_placeholders(root))
    errors.extend(validate_markdown_links(root))
    errors.extend(validate_tracked_hygiene(root))
    errors.extend(validate_no_absolute_repo_paths(root))

    if errors:
        print("Curriculum validation failed:")
        for err in errors:
            print("-", err.format())
        return 1

    print("Curriculum validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
