"""2016, jour 10 : Balance Bots — partie 2.

Après stabilisation, on multiplie les valeurs des sorties **0, 1 et 2**.
"""

from pathlib import Path
import sys

from part1 import analyser, executer, read_lines

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day10.txt"


def solve(lines, sorties=(0, 1, 2)):
    valeurs, recettes = analyser(lines)
    _, outputs, _ = executer(valeurs, recettes)

    produit = 1
    for sortie in sorties:
        produit *= outputs[sortie]
    return produit


def main():
    print("Produit des sorties 0 × 1 × 2 :", solve(read_lines()))


if __name__ == "__main__":
    main()
