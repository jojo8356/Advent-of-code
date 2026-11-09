"""2016, jour 12 : Leonardo's Monorail — partie 2.

Même programme, mais le registre `c` démarre à 1 (les autres à 0).
"""

from pathlib import Path
import sys

from part1 import REGISTRES, read_lines, solve as executer_programme

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day12.txt"


def solve(lines):
    registres = {r: 0 for r in REGISTRES}
    registres["c"] = 1
    return executer_programme(lines, registres)


def main():
    print("Valeur du registre a (c = 1):", solve(read_lines()))


if __name__ == "__main__":
    main()
