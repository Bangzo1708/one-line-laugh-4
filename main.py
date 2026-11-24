#!/usr/bin/env python3
"""The One-Line Laugh (one-line-laugh-4) — deterministic one-liner writer.

Writes a single funny line to /output/entry.txt. The line is fixed in this
file, so every run produces byte-identical output.
"""

import os

# The chosen line (108 characters, one sentence, one line):
# A setup that promises deep thought, then a self-owning twist at the end:
# the headphones work perfectly — the problem was never the noise.
LINE = (
    "I bought noise-cancelling headphones so I could hear myself think, "
    "and it turns out I had nothing to say."
)


def main() -> None:
    # Guard the gate: 1-200 characters, a single line, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Round-trip check: what landed on disk must be exactly the chosen line,
    # so a silent encoding or newline problem can never reach the gate.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        assert f.read() == LINE, "written entry.txt does not match LINE"


if __name__ == "__main__":
    main()
