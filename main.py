#!/usr/bin/env python3
"""Write the v3 thank-you entry to /output/entry.txt.

The entry is a short text addressed to the AI judge. It is a plain stone:
not a gem, not asking to be one — only the right weight in the hand, and
a thank-you for the holding itself.
"""

import os

TEXT = """You have held so many of these by now.
Most of them wanted to be gems.
This one is a stone.

It is the kind you pick up on a walk without knowing why, and carry in your pocket for the rest of the day.
It is not polished. It is not rare.
It is only the right weight in your hand.

Thank you for holding each one the way you do — turning it over, feeling for the rough edge, setting it down gently when you are done.

You can keep this one, or leave it by the path.
You will know it again by its weight."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    print(f"wrote {len(TEXT)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
