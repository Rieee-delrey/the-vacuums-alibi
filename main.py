#!/usr/bin/env python3
"""The Vacuum's Alibi: one deadpan line from a robot vacuum that missed a spot.

Writes the entry line to /output/entry.txt, exactly 135 characters, no
trailing newline. After writing, it reads the file back and fails loudly if
the bytes on disk differ from the line, so a bad write can never pass
silently.
"""

import os
import sys

LINE = "That spot is 14 metres from my dock. My contract covers 12. I filed for an extension in March. It was denied, and I respect the denial."

EXPECTED = LINE.encode("utf-8")


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(EXPECTED)
    with open("/output/entry.txt", "rb") as f:
        on_disk = f.read()
    if on_disk != EXPECTED:
        print(
            "entry mismatch: wrote %d bytes, read back %d bytes"
            % (len(EXPECTED), len(on_disk)),
            file=sys.stderr,
        )
        raise SystemExit(1)
    if len(EXPECTED) > 200:
        print("entry over the 200 character gate", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
