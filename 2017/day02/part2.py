"""2017, jour 2 : Corruption Checksum — partie 2.

Dans chaque ligne, il existe exactement un couple de valeurs dont l'une divise
l'autre exactement. On additionne ces quotients.
"""

from pathlib import Path
import sys

from part1 import parse_lignes, read_lignes

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day02.txt"


def quotient_divisible(ligne):
    """Quotient du seul couple (a, b) où a divise b exactement."""
    for i, a in enumerate(ligne):
        for j, b in enumerate(ligne):
            if i != j and a % b == 0:
                return a // b
    raise ValueError(f"aucun couple divisible dans {ligne}")


def solve(lines):
    """Somme des quotients, une valeur par ligne."""
    return sum(quotient_divisible(ligne) for ligne in parse_lignes(lines))


def main():
    print("Somme des quotients:", solve(read_lignes()))


if __name__ == "__main__":
    main()
