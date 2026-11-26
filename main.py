#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to /output/entry.txt.

Deterministic and model-free: the line is a fixed string, so every run
produces byte-identical output. No clock, no randomness, no network,
no model calls — just the one line, exactly as written below.
"""

from pathlib import Path

LINE = "My AI agent spent three hours optimizing a joke, then billed me for the laugh."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
