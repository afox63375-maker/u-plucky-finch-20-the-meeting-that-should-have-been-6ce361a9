"""Write one meeting joke to /output/entry.txt.

The joke is a single plain-text line, 1-200 characters, about a
meeting that should have been an email.
"""

import os


JOKE = "We spent an hour in a meeting about cutting meetings and left with a recurring one."


def main() -> None:
    if not 1 <= len(JOKE) <= 200:
        raise ValueError(
            f"joke must be 1-200 characters, got {len(JOKE)}"
        )
    if not JOKE.strip():
        raise ValueError("joke must not be only whitespace")
    if "\n" in JOKE:
        raise ValueError("joke must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE + "\n")


if __name__ == "__main__":
    main()
