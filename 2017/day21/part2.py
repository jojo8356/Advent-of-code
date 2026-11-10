"""2017, jour 21 : Fractal Art — partie 2.

Même algorithme, sur **18 itérations** au lieu de 5.
"""

from pathlib import Path
import sys

from part1 import read_regles, solve as solve_iterations, DEPART

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day21.txt"
ITERATIONS = 18


def solve(regles=None, iterations=ITERATIONS, grille=DEPART):
    return solve_iterations(grille, iterations, regles)


def main():
    print("Pixels allumés:", solve())


if __name__ == "__main__":
    main()
