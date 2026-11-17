#!/usr/bin/env python3
"""Read FMMods' declared WhatsApp compatibility without bypassing runtime guards."""
import argparse
import pathlib
import sys
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
RES = ROOT / "app/src/main/res"

def arrays():
    result = {}
    for xml in RES.rglob("*.xml"):
        try:
            tree = ET.parse(xml)
        except ET.ParseError:
            continue
        for node in tree.iter("string-array"):
            name = node.get("name")
            if name in ("supported_versions_wpp", "supported_versions_business"):
                result.setdefault(name, []).extend(
                    (item.text or "").strip() for item in node.findall("item")
                )
    return {k: sorted(set(v)) for k, v in result.items()}

def matches(version, rules):
    return any(version.startswith(rule[:-2] if rule.endswith("xx") else rule)
               for rule in rules)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", default="2.26.46.10")
    parser.add_argument("--target", choices=["whatsapp", "business"], default="whatsapp")
    args = parser.parse_args()
    key = "supported_versions_wpp" if args.target == "whatsapp" else "supported_versions_business"
    rules = arrays().get(key, [])
    if not rules:
        print(f"ERROR: No declared rules found for {key}", file=sys.stderr)
        return 2
    print(f"Target: {args.target}; host: {args.version}")
    print(f"Declared rules: {', '.join(rules)}")
    print(f"Rule match: {'YES' if matches(args.version, rules) else 'NO'}")
    print("Note: rule match is NOT evidence that hooks work on a device.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
