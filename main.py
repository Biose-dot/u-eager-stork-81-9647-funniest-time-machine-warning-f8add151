#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

The label stays deadpan-official while the punchline lands at the end: your future self is not a stranger, he is a witness with a grudge — and he has had decades to rehearse this exact moment.
"""
import os

ENTRY = 'WARNING: Never wave at yourself. He remembers this moment, he is still angry, and he has had decades to rehearse it.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
