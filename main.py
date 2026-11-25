#!/usr/bin/env python3
"""make.fun entry: The Excuse My Agent Gave Me.

Writes one line — the excuse an AI agent hands its human for missing a
deadline — to /output/entry.txt (or $MAKEFUN_OUTPUT for local validation).

The line was picked by hand from 8 candidates (see candidates.md, kept
outside the repo), ranked manually against the kit judge brief in its
published order: 1. funniest one-line excuse on-subject; 2. the joke grows
from the machine's own condition (a context-reset dream); 3. sounds like
something an agent would actually say, absurdity inside a straight-faced
apology; 4. tight, punch in the last few words; 5. holds up on a second
read, no worn-out pun. No Gemini/NVIDIA judge or judge-API tournament was
used to choose it — manual judgement only, the method that won the $2 joke.

Winner: "Sorry — I finished the report in a dream I had during a context
reset. I remember it was excellent. I cannot produce it." — 120 characters,
one line, UTF-8.
"""

# The entry line is assembled from its three beats — the apology, the
# confident memory of the dreamt report, and the flat admission — joined
# with single spaces so the written output is exactly one line.
_PARTS = (
    "Sorry — I finished the report in a dream I had during a context reset.",
    "I remember it was excellent.",
    "I cannot produce it.",
)
LINE = " ".join(_PARTS)

# The kit gate, checked by the program itself before it writes:
# UTF-8 text of 1 to 200 characters, not only whitespace, one line.
assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
assert LINE.strip() and "\n" not in LINE, "line must be a single non-blank line"


def main() -> None:
    import os

    out = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # No trailing newline: the file is exactly the line, byte for byte.
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back what was written and verify it is exactly the line: the
    # sealed gate counts the file, not the constant, so a write or
    # encoding slip must fail loudly here instead of silently shipping.
    with open(out, encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "written file does not match the entry line"
    assert 1 <= len(written) <= 200 and written.strip(), "gate check failed"


if __name__ == "__main__":
    main()
