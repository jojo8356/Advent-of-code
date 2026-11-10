"""2016, jour 23 : Safe Cracking — partie 2.

Même programme, mais le registre `a` démarre à **12** : le programme calcule
`12!` puis y ajoute une constante. Grâce aux motifs optimisés de la partie 1,
le calcul se fait en quelques centaines d'étapes.
"""

from pathlib import Path
import sys

from part1 import REGISTRES, read_lines, solve as executer_programme

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day23.txt"


def solve(lines):
    return executer_programme(lines, a=12)


def main():
    print("Valeur du registre a (a=12):", solve(read_lines()))


if __name__ == "__main__":
    main()
