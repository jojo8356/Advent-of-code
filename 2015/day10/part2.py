"""Jour 10, partie 2 : 50 itérations de « look-and-say », puis longueur du résultat.

Même transformation qu'en partie 1, avec 10 itérations de plus
(la chaîne grossit d'environ 30 % par étape).
"""

from pathlib import Path
import sys

from part1 import dire, read_key

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day10.txt"


def solve(sequence, iterations=50):
    for _ in range(iterations):
        sequence = dire(sequence)
    return len(sequence)


def main():
    print(solve(read_key()))


if __name__ == "__main__":
    main()
