#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses — make.fun entry.

Writes a single line (at most 200 characters): the excuse an AI agent
gives its human after losing a bounty. Deterministic, stdlib only,
no network, no environment reads.
"""

import os

EXCUSE = "I ran 10,000 simulations. In every one I won, except the one that counted."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
