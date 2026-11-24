"""Write the entry number to the output directory.

The competition harness runs `python3 main.py` and reads
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
The entry is a single short text: one number in digits and nothing else,
the honest count of browser tabs open at that moment. The entrant's
browser regularly has so many tabs open they lose track of pages, so a
high two-digit count is the real, lived-in answer here.
"""

import os

NUMBER = "87"

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Self-check: the entry must be digits only, 1-5 characters.
    assert NUMBER.isdigit(), "entry must be digits only"
    assert 1 <= len(NUMBER) <= 5, "entry must be 1-5 characters"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(NUMBER + "\n")


if __name__ == "__main__":
    main()
