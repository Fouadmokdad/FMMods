#!/usr/bin/env python3
"""Generate a static feature-by-feature compatibility checklist for FMMods.

This is a source inventory only; it does not claim any hook works on a host version.
"""
import argparse
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "app/src/main/java/com/wmods/wppenhacer/xposed/core/FeatureRegistry.kt"
FEATURES = ROOT / "app/src/main/java/com/wmods/wppenhacer/xposed/features"

def inventory():
    source = REGISTRY.read_text(encoding="utf-8")
    block = source.split("val features: List<Class<out Feature>> = listOf(", 1)[1].split("\n    )", 1)[0]
    names = re.findall(r"\b([A-Za-z][A-Za-z0-9]*)::class\.java", block)
    if not names or len(names) != len(set(names)):
        raise ValueError("Empty or duplicate feature registry")
    files = {p.stem: p for p in FEATURES.rglob("*.kt")}
    missing = sorted(set(names) - set(files))
    if missing:
        raise ValueError("Missing feature sources: " + ", ".join(missing))
    return [(name, files[name].relative_to(ROOT)) for name in names]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", default="2.26.46.10")
    parser.add_argument("--output", type=pathlib.Path)
    args = parser.parse_args()
    items = inventory()
    lines = [
        f"# FMMods feature audit — WhatsApp {args.version}",
        "",
        "Static inventory only. All features remain **unverified** until tested on this host.",
        "Do not enable bypass_version_check on a primary account based on this checklist.",
        "",
        "| # | Feature | Source | Compatibility |",
        "|---:|---|---|---|",
    ]
    for i, (name, source) in enumerate(items, 1):
        lines.append(f"| {i} | {name} | `{source}` | Not verified |")
    lines.extend(["", f"**Total registered features: {len(items)}**", ""])
    output = "\n".join(lines)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output)

if __name__ == "__main__":
    main()
