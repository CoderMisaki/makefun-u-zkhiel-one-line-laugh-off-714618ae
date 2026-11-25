#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt.
Pure standard library, no network, fully deterministic.
"""

from pathlib import Path

# One joke, one line, cold read: a bequest, a fast watch, and a
# grandfather who refuses to stop winning even after the funeral.
JOKE = "My grandfather left me his watch \u2014 it runs five minutes fast, so even now, he's still ahead of me."


def main() -> None:
    # Enforce the competition gate before anything is written:
    # one line, 1-200 characters, more than whitespace.
    lines = JOKE.splitlines()
    assert len(lines) == 1 and 1 <= len(JOKE) <= 200 and JOKE.strip(), "joke breaks the gate"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
