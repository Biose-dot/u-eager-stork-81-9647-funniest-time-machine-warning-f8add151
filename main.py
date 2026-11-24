#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

A warning label for a time machine, phrased like a genuine safety notice — until the last words, when your older self shows up with a grudge and decades of rehearsal time.
"""
import os

ENTRY = 'WARNING: Do not meet yourself. He knows what you did, and he has had years to plan this conversation.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
