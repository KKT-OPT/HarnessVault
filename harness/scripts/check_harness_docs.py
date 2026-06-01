#!/usr/bin/env python3
"""
HarnessVault dry-run document checker.

This script only reads files and prints findings. It must not modify, move,
delete, or create Harness documents.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Set, Tuple

FRONTMATTER_PATTERN = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
WIKILINK_PATTERN = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")
REQUIRED_FIELDS = [
    "documentName",
    "title",
    "aliases",
    "tags",
    "version",
    "status",
    "type",
    "purpose",
    "scope",
    "owner",
    "reviewAfter",
]
TEMPLATE_REQUIRED_FIELDS = REQUIRED_FIELDS + [
    "templateName",
    "templateTarget",
    "templateEngine",
    "templatePurpose",
]
EXCLUDED_PARTS = {
    ".git",
    ".idea",
    "node_modules",
    "dist",
    "build",
}
EXCLUDED_SUFFIXES = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".pdf",
}
EXCLUDED_OBSIDIAN_PLUGIN_PARTS = {"plugins"}


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    path: str
    message: str


def iter_markdown_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.md"):
        parts = set(path.parts)
        if parts & EXCLUDED_PARTS:
            continue
        if ".obsidian" in parts and EXCLUDED_OBSIDIAN_PLUGIN_PARTS & parts:
            continue
        if path.suffix.lower() in EXCLUDED_SUFFIXES:
            continue
        yield path


def is_template_file(root: Path, path: Path) -> bool:
    rel_parts = path.relative_to(root).parts
    return bool(rel_parts and rel_parts[0] == "templates")


def parse_frontmatter(text: str) -> Tuple[Dict[str, str], bool, List[str]]:
    match = FRONTMATTER_PATTERN.match(text)
    if not match:
        return {}, False, []
    raw = match.group(1)
    values: Dict[str, str] = {}
    lines = raw.splitlines()
    for line in lines:
        if not line.strip() or line.startswith(" ") or line.startswith("-"):
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"')
    return values, True, lines


def extract_aliases(frontmatter_lines: List[str]) -> Set[str]:
    candidates: Set[str] = set()
    in_aliases = False
    for line in frontmatter_lines:
        if line.startswith("aliases:"):
            in_aliases = True
            continue
        if in_aliases:
            if line.startswith("  - "):
                candidates.add(line.replace("  - ", "", 1).strip().strip('"'))
            elif line and not line.startswith(" "):
                in_aliases = False
    return {item for item in candidates if item}


def collect_aliases(root: Path, markdown_files: List[Path]) -> Dict[str, List[str]]:
    aliases: Dict[str, List[str]] = {}
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        frontmatter, _, lines = parse_frontmatter(text)
        title = frontmatter.get("title")
        stem = path.stem
        candidates = {stem}
        if title:
            candidates.add(title)
        candidates.update(extract_aliases(lines))
        rel = str(path.relative_to(root)).replace("\\", "/")
        for item in candidates:
            if item:
                aliases.setdefault(item, []).append(rel)
    return aliases


def check_file(root: Path, path: Path, aliases: Dict[str, List[str]]) -> List[Finding]:
    findings: List[Finding] = []
    emitted: Set[Tuple[str, str]] = set()
    rel = str(path.relative_to(root)).replace("\\", "/")
    text = path.read_text(encoding="utf-8")
    frontmatter, has_frontmatter, _ = parse_frontmatter(text)
    template_file = is_template_file(root, path)

    def add(severity: str, code: str, message: str) -> None:
        key = (code, message)
        if key not in emitted:
            findings.append(Finding(severity, code, rel, message))
            emitted.add(key)

    if not has_frontmatter:
        add("high", "FM-MISSING", "Missing YAML frontmatter.")
        return findings

    required_fields = TEMPLATE_REQUIRED_FIELDS if template_file else REQUIRED_FIELDS
    for field in required_fields:
        if field not in frontmatter:
            add("medium", "FM-FIELD-MISSING", f"Missing frontmatter field: {field}")

    document_name = frontmatter.get("documentName")
    if document_name and document_name != rel:
        add("medium", "FM-DOCUMENT-NAME-MISMATCH", f"documentName is '{document_name}', actual path is '{rel}'.")

    if template_file and frontmatter.get("type") != "template":
        add("medium", "TEMPLATE-TYPE-MISMATCH", "templates/** files should use type: template.")

    for target in set(WIKILINK_PATTERN.findall(text)):
        matches = aliases.get(target, [])
        if not matches:
            add("low", "WIKI-UNRESOLVED-CANDIDATE", f"Wikilink target may be unresolved: [[{target}]]")
        elif len(matches) > 1:
            add("low", "WIKI-AMBIGUOUS-CANDIDATE", f"Wikilink target is ambiguous: [[{target}]] -> {matches}")

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Dry-run HarnessVault documentation checker.")
    parser.add_argument("--root", default="harness", help="Harness vault root. Default: harness")
    parser.add_argument("--format", choices=["text"], default="text")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"ERROR: root does not exist: {root}", file=sys.stderr)
        return 2

    markdown_files = sorted(iter_markdown_files(root))
    aliases = collect_aliases(root, markdown_files)

    findings: List[Finding] = []
    for path in markdown_files:
        findings.extend(check_file(root, path, aliases))

    severity_counts: Dict[str, int] = {}
    for finding in findings:
        severity_counts[finding.severity] = severity_counts.get(finding.severity, 0) + 1

    print("HarnessVault dry-run document check")
    print(f"Root: {root}")
    print(f"Markdown files checked: {len(markdown_files)}")
    print(f"Findings: {len(findings)}")
    print(f"Severity summary: {severity_counts}")
    print("No files were modified.")
    print()

    for finding in findings:
        print(f"[{finding.severity}] {finding.code} {finding.path} - {finding.message}")

    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
