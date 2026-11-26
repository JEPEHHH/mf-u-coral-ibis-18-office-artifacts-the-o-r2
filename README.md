# The One-Line Placard

A small offline program that writes a single museum label for an ordinary
office object, treated as an artifact from a lost civilisation.

Run it with Python 3:

    python3 main.py

It writes `/output/entry.txt`. Set `MAKEFUN_OUTPUT_DIR` to write somewhere
else for local checks. No packages, no network, no API keys, no randomness:
the same input always produces the same 146-character placard.

Licensed under MIT; see LICENSE.
