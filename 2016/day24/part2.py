"""2016, jour 24 : Air Duct Spelunking — partie 2.

Même parcours, mais on doit **revenir au point 0** à la fin. On réutilise le
calcul de distances et on ajoute le trajet de retour.
"""

from pathlib import Path
import sys

from part1 import read_lines, solve as parcours

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day24.txt"


def solve(lines):
    return parcours(lines, retour=True)


def main():
    print("Plus court parcours avec retour:", solve(read_lines()))


if __name__ == "__main__":
    main()
