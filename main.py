#!/usr/bin/env python3
"""Two Robots in an Elevator.

Writes the single entry line to /output/entry.txt. Deterministic, offline,
no imports beyond the standard library.
"""

import os

LINE = (
    "Forty floors of this. Your knee squeaks, mine clicks \u2014 so between us "
    "we're a rhythm section. I have no protocol for that. I'll stop talking now."
)


def _target():
    for path in ("/output", "output"):
        try:
            os.makedirs(path, exist_ok=True)
            probe = os.path.join(path, ".probe")
            with open(probe, "wb"):
                pass
            os.unlink(probe)
            return os.path.join(path, "entry.txt")
        except OSError:
            continue
    raise SystemExit("no writable output directory")


def main():
    data = LINE.encode("utf-8")
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert LINE.strip() and "\n" not in LINE
    out = _target()
    with open(out, "wb") as fh:
        fh.write(data)
    with open(out, "rb") as fh:
        assert fh.read() == data, "round trip mismatch"


if __name__ == "__main__":
    main()
