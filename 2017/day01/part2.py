"""2017, jour 1 : Inverse Captcha — partie 2.

Cette fois, on compare chaque chiffre à celui situé **à l'opposé** dans le
cercle, c'est-à-dire à `longueur / 2` positions plus loin. On additionne les
chiffres qui sont égaux à ce partenaire.
"""

from pathlib import Path
import sys

from part1 import read_sequence

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day01.txt"


def somme_opposes(sequence):
    """Somme des chiffres égaux à leur opposé (demi-tour)."""
    longueur = len(sequence)
    if longueur % 2 != 0:
        raise ValueError("la séquence doit avoir une longueur paire")
    demi = longueur // 2

    total = 0
    for i, chiffre in enumerate(sequence):
        if chiffre == sequence[(i + demi) % longueur]:
            total += int(chiffre)
    return total


def solve(sequence):
    return somme_opposes(sequence)


def main():
    print("Somme des opposés identiques:", solve(read_sequence()))


if __name__ == "__main__":
    main()
