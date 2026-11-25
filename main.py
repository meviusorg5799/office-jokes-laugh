"""Write the chosen office joke to the make.fun output file.

Reads the joke from entry.txt (kept beside this script, so the text
lives in exactly one place) and writes it, plus a trailing newline,
to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when unset).
Deterministic: no clock, no network, no randomness.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    joke = (HERE / "entry.txt").read_text(encoding="utf-8")
    # Fail loudly rather than emit an entry the sealed gate would refuse:
    # one single line of text, 1-200 characters (trailing newline excluded).
    text = joke.rstrip("\n")
    if not text or not text.strip():
        raise SystemExit("entry.txt is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-200")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(joke, encoding="utf-8")


if __name__ == "__main__":
    main()
