"""2016, jour 16 : Dragon Checksum — partie 2.

Même travail, mais le disque fait **35 651 528** cases.
"""

from pathlib import Path
import sys

from part1 import read_graine, solve as somme_pour

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day16.txt"
TAILLE_DISQUE = 35651584


def solve(graine, taille=TAILLE_DISQUE):
    return somme_pour(graine, taille)


def main():
    print(f"Somme de contrôle (disque de {TAILLE_DISQUE}) :", solve(read_graine()))


if __name__ == "__main__":
    main()
