"""Jour 11, partie 2 : le mot de passe suivant après celui de la partie 1.

On calcule d'abord le mot de passe de la partie 1, puis on cherche encore une
fois le prochain mot de passe valide à partir de celui-là.
"""

from pathlib import Path
import sys

from part1 import read_key, suivant

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day11.txt"


def solve(mot_de_passe):
    return suivant(suivant(mot_de_passe))


def main():
    print(solve(read_key()))


if __name__ == "__main__":
    main()
