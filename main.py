"""One-line excuse entry.

Writes a single line to /output/entry.txt: the excuse an AI agent
gives its human for missing a deadline. Standard library only,
deterministic, no network.
"""

import os

ENTRY = "I delegated it to a second agent. It delegated it to a third. We now have a committee and no deliverable."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")


def main():
    assert 1 <= len(ENTRY) <= 160, "entry must be 1 to 160 characters"
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
