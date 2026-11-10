"""2017, jour 8 : I Heard You Like Registers — partie 2.

Plus grande valeur atteinte par **n'importe quel** registre pendant l'exécution.
"""

from pathlib import Path
import sys

from part1 import read_lines, executer

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day08.txt"


def solve(lignes):
    _, maximum_vu = executer(lignes)
    return maximum_vu


def main():
    print("Plus grande valeur jamais atteinte:", solve(read_lines()))


if __name__ == "__main__":
    main()
