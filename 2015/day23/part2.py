"""Jour 23, partie 2 : même programme, mais le registre `a` démarre à 1.

Tout le reste est identique à la partie 1 : on réutilise `run` et `solve`.
"""

from pathlib import Path
import sys

from part1 import read_lines, solve as executer

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day23.txt"


def solve(lines):
    """Valeur du registre b avec a = 1 (au lieu de a = 0)."""
    return executer(lines, a=1)


def main():
    print("Valeur du registre b (a = 1) :", solve(read_lines()))


if __name__ == "__main__":
    main()
