#!/usr/bin/env python3
"""Write the one-line placard for the office-artifact contest.

The program is fully offline and deterministic. It writes exactly one UTF-8
text file whose contents are a single museum label of at most 180 characters.
The destination is /output/entry.txt by default; MAKEFUN_OUTPUT_DIR may
override the directory when a local check wants a different location.
"""

import os
from pathlib import Path

PLACARD = (
    "Coronation stapler of the Lower Cubicle Dynasties, c. 2014 CE. "
    "Bronze, bone, and one stubborn staple. "
    "Donor: the intern who filed it under 'misc'."
)

MAX_LENGTH = 180
DEFAULT_DIRECTORY = "/output"
FILENAME = "entry.txt"
TERMINATOR = "\n"


def output_path() -> Path:
    """Resolve the directory the contest reads from, with an env override."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_DIRECTORY
    return Path(directory) / FILENAME


def validate(text: str) -> str:
    """Keep only a placard that is nonblank and fits the 180-character cap."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("placard must be nonblank text")
    size = len(text)
    if size < 1 or size > MAX_LENGTH:
        raise ValueError(f"placard length {size} outside 1..{MAX_LENGTH}")
    return text


def render(line: str) -> str:
    """Return the exact bytes the gate will read: one line plus terminator."""
    return validate(line) + TERMINATOR


def write_entry(line: str, path: Path) -> None:
    """Create the destination folder and store the single placard line."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render(line), encoding="utf-8")


def main() -> None:
    write_entry(PLACARD, output_path())


if __name__ == "__main__":
    main()
