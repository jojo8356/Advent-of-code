"""2017, jour 19 : A Series of Tubes — partie 2.

Nombre de cases parcourues (lettres, tubes et virages compris) avant de sortir.
"""

from pathlib import Path
import sys

from part1 import read_grille, parcourir

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day19.txt"


def solve(grille):
    return parcourir(grille)[1]


def main():
    print("Cases parcourues:", solve(read_grille()))


if __name__ == "__main__":
    main()
