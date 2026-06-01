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
from typing import Dict, Iterable, List, Tuple

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


@dataclass
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


def parse_frontmatter(text: str) -> Tuple[Dict[str, str], bool]:
    match = FRONTMATTER_PATTERN.match(text)
    if not match:
        return {}, False
    raw = match.group(1)
    values: Dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip() or line.startswith(" ") or line.startswith("-"):
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"')
    return values, True


def collect_aliases(root: Path, markdown_files: List[Path]) -> Dict[str, List[str]]:
    aliases: Dict[str, List[str]] = {}
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        frontmatter, _ = parse_frontmatter(text)
        title = frontmatter.get("title")
        stem = path.stem
        candidates = {stem}
        if title:
            candidates.add(title)
        # Lightweight alias extraction: handles simple YAML list under aliases.
        match = FRONTMATTER_PATTERN.match(text)
        if match:
            raw = match.group(1).splitlines()
            in_aliases = False
            for line in raw:
                if line.startswith("aliases:"):
                    in_aliases = True
                    continue
                if in_aliases:
                    if line.startswith("  - "):
                        candidates.add(line.replace("  - ", "", 1).strip().strip('"'))
                    elif line and not line.startswith(" "):
                        in_aliases = False
        rel = str(path.relative_to(root)).replace("\\", "/")
        for item in candidates:
            if item:
                aliases.setdefault(item, []).append(rel)
    return aliases


def check_file(root: Path, path: Path, aliases: Dict[str, List[str]]) -> List[Finding]:
    findings: List[Finding] = []
    rel = str(path.relative_to(root)).replace("\\", "/")
    text = path.read_text(encoding="utf-8")
    frontmatter, has_frontmatter = parse_frontmatter(text)

    if not has_frontmatter:
        findings.append(Finding("high", "FM-MISSING", rel, "Missing YAML frontmatter."))
        return findings

    for field in REQUIRED_FIELDS:
        if field not in frontmatter:
            findings.append(Finding("medium", "FM-FIELD-MISSING", rel, f"Missing frontmatter field: {field}"))

    document_name = frontmatter.get("documentName")
    if document_name and document_name != rel:
        findings.append(
            Finding(
                "medium",
                "FM-DOCUMENT-NAME-MISMATCH",
                rel,
                f"documentName is '{document_name}', actual path is '{rel}'.",
            )
        )

    for target in WIKILINK_PATTERN.findall(text):
        matches = aliases.get(target, [])
        if not matches:
            findings.append(Finding("low", "WIKI-UNRESOLVED-CANDIDATE", rel, f"Wikilink target may be unresolved: [[{target}]]"))
        elif len(matches) > 1:
            findings.append(Finding("low", "WIKI-AMBIGUOUS-CANDIDATE", rel, f"Wikilink target is ambiguous: [[{target}]] -> {matches}"))

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

    print("HarnessVault dry-run document check")
    print(f"Root: {root}")
    print(f"Markdown files checked: {len(markdown_files)}")
    print(f"Findings: {len(findings)}")
    print("No files were modified.")
    print()

    for finding in findings:
        print(f"[{finding.severity}] {finding.code} {finding.path} - {finding.message}")

    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
