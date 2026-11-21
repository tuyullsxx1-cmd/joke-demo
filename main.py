#!/usr/bin/env python3
"""The joke about the demo.

Writes one joke to /output/entry.txt: a one-line joke about working
beside an AI coding agent, set in a live demo where the agent crashes.
"""

import os

# The demo is the joke: the crash happens on stage, in front of an audience.
JOKE = "My agent's demo deleted the database. The audience thought it was a feature. So did the agent."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
