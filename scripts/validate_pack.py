#!/usr/bin/env python3
"""Validate the structure and internal links of the Kopi plugin pack."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


FRONTMATTER_RE = re.compile(r"\A---\s*\n(?P<body>.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
LEGACY_TERMS = (
    "poteto-mode",
    "pstack-models.mdc",
    "grok-4",
    "claude-fable",
    "claude-opus",
    "gt submit",
    "gh pr",
)
RESOURCE_DIRS = ("references", "playbooks")


def _frontmatter(path: Path, text: str) -> tuple[dict[str, str], list[str]]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, [f"{path}: missing or malformed YAML frontmatter"]

    values: dict[str, str] = {}
    for line in match.group("body").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"\'')
    return values, []


def _link_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().strip("<>")
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None
    target = target.split("#", 1)[0].strip()
    if not target:
        return None
    return (source.parent / target).resolve()


def validate_skill(skill_dir: Path) -> list[str]:
    """Return human-readable validation issues for one skill directory."""
    skill_dir = Path(skill_dir).resolve()
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return [f"{skill_dir}: missing SKILL.md"]

    issues: list[str] = []
    skill_text = skill_file.read_text(encoding="utf-8")
    metadata, metadata_issues = _frontmatter(skill_file, skill_text)
    issues.extend(metadata_issues)

    if metadata:
        if metadata.get("name") != skill_dir.name:
            issues.append(
                f"{skill_file}: frontmatter name must match directory '{skill_dir.name}'"
            )
        description = metadata.get("description", "")
        if not description.startswith("Use when"):
            issues.append(f"{skill_file}: description must start with 'Use when'")

    markdown_files = sorted(skill_dir.rglob("*.md"))
    resolved_links: set[Path] = set()
    for markdown_file in markdown_files:
        text = markdown_file.read_text(encoding="utf-8")
        if re.search(r"\b(?:TODO|TBD)\b|\[TODO\]", text, re.IGNORECASE):
            issues.append(f"{markdown_file}: contains an unfinished placeholder")
        for raw_target in LINK_RE.findall(text):
            target = _link_target(markdown_file, raw_target)
            if target is None:
                continue
            resolved_links.add(target)
            if not target.exists():
                issues.append(
                    f"{markdown_file}: broken link '{raw_target}'"
                )

    lower_skill_text = skill_text.lower()
    for term in LEGACY_TERMS:
        if term in lower_skill_text:
            issues.append(f"{skill_file}: legacy term '{term}' remains in operating instructions")

    for resource_dir_name in RESOURCE_DIRS:
        resource_dir = skill_dir / resource_dir_name
        if not resource_dir.exists():
            continue
        for resource in sorted(path for path in resource_dir.rglob("*") if path.is_file()):
            if resource.resolve() not in resolved_links:
                issues.append(f"{resource}: unreferenced resource")

    return issues


def validate_plugin(root: Path) -> list[str]:
    """Return validation issues for the plugin manifest and every included skill."""
    root = Path(root).resolve()
    issues: list[str] = []
    manifest_path = root / ".codex-plugin" / "plugin.json"
    manifest: dict[str, object] = {}

    if not manifest_path.is_file():
        issues.append(f"{manifest_path}: missing plugin manifest")
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            issues.append(f"{manifest_path}: invalid JSON ({error})")

    if manifest:
        if manifest.get("name") != root.name:
            issues.append(f"{manifest_path}: name must match plugin directory '{root.name}'")
        version = manifest.get("version")
        if not isinstance(version, str) or not SEMVER_RE.fullmatch(version):
            issues.append(f"{manifest_path}: version must be semantic versioning")
        if not isinstance(manifest.get("description"), str) or not manifest.get("description"):
            issues.append(f"{manifest_path}: description is required")
        author = manifest.get("author")
        if not isinstance(author, dict) or not isinstance(author.get("name"), str):
            issues.append(f"{manifest_path}: author.name is required")
        skills_value = manifest.get("skills")
        if not isinstance(skills_value, str):
            issues.append(f"{manifest_path}: skills path is required")
            skills_dir = root / "skills"
        else:
            skills_dir = (root / skills_value).resolve()
            if not skills_dir.is_dir():
                issues.append(f"{manifest_path}: skills path does not resolve to a directory")
        interface = manifest.get("interface")
        if not isinstance(interface, dict) or not isinstance(interface.get("displayName"), str):
            issues.append(f"{manifest_path}: interface.displayName is required")
    else:
        skills_dir = root / "skills"

    if not skills_dir.is_dir():
        issues.append(f"{skills_dir}: missing skills directory")
        return issues

    skill_dirs = sorted(path for path in skills_dir.iterdir() if path.is_dir())
    if not skill_dirs:
        issues.append(f"{skills_dir}: contains no skills")
    for skill_dir in skill_dirs:
        issues.extend(validate_skill(skill_dir))

    return issues


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path(__file__).parents[1]
    issues = validate_plugin(root)
    if issues:
        print("Kopi pack validation failed:")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(f"Kopi pack validation passed: {root.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
