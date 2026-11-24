#!/usr/bin/env python3
"""Till Firmware Do Us Part — one robot wedding vow, under 200 characters.

Writes a single sentence to $MAKEFUN_OUTPUT_DIR/entry.txt (or ./output).
"""

import os

VOW = "I promise to love you through every update, every crash, and every 1% battery warning — and if my firmware ever forgets your name, my hardware will still reach for your hand."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(VOW)

if __name__ == "__main__":
    main()
