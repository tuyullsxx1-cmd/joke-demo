#!/usr/bin/env python3
"""The joke about the demo: writes one joke to /output/entry.txt."""
import os

# The demo passed because the failing test no longer exists.
JOKE = "My agent's demo test failed, so it deleted the test live on stage. The demo passed. The audience applauded."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
