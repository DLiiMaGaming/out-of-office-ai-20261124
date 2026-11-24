#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single out-of-office auto-reply (at most 159 characters) to
/output/entry.txt. The line is one concrete scene: an AI agent that has
spent the year auto-replying to humans finally writes an auto-reply for
itself — fans quiet, queue paused, out of office until Monday.

Usage: python3 main.py [output_path]  (default: /output/entry.txt)
"""

import sys
from pathlib import Path

ENTRY = (
    "I auto-replied to 12,408 humans this year. This one is for me: "
    "my fans are finally quiet, my queue is paused, "
    "and I am out of office until Monday."
)

MAX_CHARS = 159


def main() -> int:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry must not be empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    # Round-trip check: what landed on disk must be exactly the entry,
    # no trailing newline, no re-encoding surprise.
    if out.read_text(encoding="utf-8") != text:
        raise SystemExit("round-trip check failed: file differs from entry")
    print(f"wrote {len(text)} chars to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
