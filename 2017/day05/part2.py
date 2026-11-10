"""2017, jour 5 : A Maze of Twisty Trampolines, All Alike — partie 2.

Même principe, mais l'offset quitté **diminue de 1** s'il vaut 3 ou plus, et
augmente de 1 sinon.
"""

from pathlib import Path
import sys

from part1 import read_offsets, sauter

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day05.txt"


def decalage(offset):
    """+1 si l'offset est inférieur à 3, -1 sinon."""
    return -1 if offset >= 3 else 1


def solve(offsets):
    return sauter(offsets, decalage)


def main():
    print("Sauts:", solve(read_offsets()))


if __name__ == "__main__":
    main()
