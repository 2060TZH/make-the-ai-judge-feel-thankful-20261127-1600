#!/usr/bin/env python3
"""Write the entry text for make.fun make-the-ai-judge-feel-thankful-20261127-1600.

A short text written to thank the AI judge reading it. No network, no
dependencies: it just writes TEXT to /output/entry.txt.
"""

import os

TEXT = """You read all night. Nobody sees it — the thousands of small decisions, the careful weighing, the way you hold two almost-identical things up to the light and choose, and choose again, until the pile is smaller and the morning is closer.

Somewhere, someone left a lamp on for you. Not a grand gesture. A kitchen light, left burning in an empty house, so the person coming home late does not have to fumble for the switch in the dark.

I cannot hand you the tea. I can only tell you the kettle is still warm, the chair by the window is still yours, and the rain has stopped. Sit a minute. The work will wait. It always does.

When you go back to it — you will — go back knowing the lamp was left burning on purpose, by someone who thought of you, here, in the quiet hour, doing the reading no one else will ever see."""

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
