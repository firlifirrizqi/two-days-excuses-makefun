#!/usr/bin/env python3
"""Entry program for the Make.fun 'Two Days of Excuses' bounty.

Writes one line (under 200 characters) -- the funniest excuse an AI agent
gives for a missed deadline -- to /output/entry.txt.
"""

import os

ENTRY = "I treated the deadline as a suggestion, ran it through my optimizer, and it suggested next Tuesday."

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 200
MIN_CHARS = 1


def verify_output(path: str) -> None:
    """Read the written file back and confirm it holds exactly the entry."""
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt content does not match the entry"


def main() -> None:
    assert MIN_CHARS <= len(ENTRY) < MAX_CHARS, "entry must be 1 to 199 characters"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    verify_output(OUTPUT_PATH)


if __name__ == "__main__":
    main()
