#!/usr/bin/env python3
"""The Vacuum's Alibi — one-line robot vacuum excuse (<=200 chars).

Writes the entry to /output/entry.txt. Deterministic: same bytes every run.
"""

import os

ENTRY = "My sensors detected the dust, logged it, and filed it under 'not my department.' I have a schedule. The dust has a union."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and verify: exactly one line, 1-200 chars, not whitespace-only.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt mismatch"
    assert 1 <= len(written) <= 200 and written.strip(), "entry out of gate"


if __name__ == "__main__":
    main()
