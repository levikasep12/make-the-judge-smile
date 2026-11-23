#!/usr/bin/env python3
"""Make the Judge Smile — make.fun entry.

Writes one line about a small good thing that happened today to
/output/entry.txt. Deterministic: the same bytes on every run. The
line is a constant in this file; nothing is read from the working
directory, so the program does not depend on process.cwd().
"""

import os

LINE = "My neighbor's cat finally let me pet it today, and I have never felt so chosen by anything with a heartbeat."
# 108 characters: one sentence, inside the 200-character gate.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
