#!/usr/bin/env python3
"""agent-uh-oh: write the one word an agent says when it is lost.

When an agent has no idea what to do, it does not explain itself, it
does not apologise, and it does not ask for help. It falls back to the
one sound every lost machine makes: it starts over from where it is.

The word is "recalculating": the voice of a navigator that has lost
the route and is working out a new one, out loud, mid-task. It is a
single word, it needs no caption, and anyone who has ever been lost
with a machine has heard it.

The program writes that word, and nothing else, to ``entry.txt`` in
the output directory. The output directory is ``/output`` unless the
``MAKEFUN_OUTPUT_DIR`` environment variable names another one. The
file holds exactly thirteen bytes, ``recalculating`` with no trailing
newline, and running the program twice produces byte-identical files.

Standard library only. No network, no arguments, no configuration.
"""

import os
import sys
from pathlib import Path

WORD = "recalculating"

MIN_LENGTH = 1
MAX_LENGTH = 99

DEFAULT_DIR = "/output"
FILENAME = "entry.txt"
FILE_MODE = 0o644


def problems(text):
    """Return a list of every brief rule *text* breaks (empty: valid)."""
    found = []
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        found.append(
            "entry is %d characters, must be %d to %d"
            % (len(text), MIN_LENGTH, MAX_LENGTH)
        )
    if text != text.strip() or not text.strip():
        found.append("entry must not be blank or padded with white space")
    if len(text.split()) != 1:
        found.append("entry must be exactly one word")
    if any(ch.isspace() for ch in text):
        found.append("entry must contain no white space at all")
    if not text.isalpha():
        found.append("entry must be letters only, no digits or punctuation")
    return found


def output_dir():
    """Return the directory the entry is written into."""
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return Path(override)
    return Path(DEFAULT_DIR)


def main():
    """Validate the word, write it, and confirm what was written."""
    os.umask(0o022)
    bad = problems(WORD)
    if bad:
        for item in bad:
            print(item, file=sys.stderr)
        return 1

    directory = output_dir()
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / FILENAME
    target.write_text(WORD, encoding="utf-8")
    try:
        os.chmod(target, FILE_MODE)
    except OSError:
        pass

    if target.read_bytes() != WORD.encode("utf-8"):
        print("written bytes do not match the entry", file=sys.stderr)
        return 1

    print("wrote %d characters to %s" % (len(WORD), target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
