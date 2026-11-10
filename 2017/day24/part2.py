"""2017, jour 24 : Electromagnetic Moat — partie 2.

On cherche d'abord le pont le **plus long** (le plus de composants), puis, à
longueur égale, la plus grande force.
"""

from pathlib import Path
import sys

from part1 import read_composants, explorer

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day24.txt"


def solve(composants):
    _, longueur, force = explorer(composants)
    return force


def main():
    print("Force du plus long pont:", solve(read_composants()))


if __name__ == "__main__":
    main()
