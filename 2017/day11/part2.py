"""2017, jour 11 : Hex Ed — partie 2.

Distance maximale atteinte à **n'importe quel moment** du chemin.
"""

from pathlib import Path
import sys

from part1 import read_chemin, parcourir

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day11.txt"


def solve(pas):
    _, maximum = parcourir(pas)
    return maximum


def main():
    print("Distance maximale:", solve(read_chemin()))


if __name__ == "__main__":
    main()
