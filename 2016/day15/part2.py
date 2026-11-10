"""2016, jour 15 : Timing is Everything — partie 2.

On ajoute un disque #7 de **11 positions**, en position 0 à t = 0, puis on
recalcule le premier instant possible.
"""

from pathlib import Path
import sys

from part1 import parse_disques, read_lines, resoudre

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day15.txt"
DISQUE_SUPPLEMENTAIRE = (7, 11, 0)  # (numéro, positions, départ)


def solve(lines, disque=DISQUE_SUPPLEMENTAIRE):
    disques = parse_disques(lines)
    disques.append(disque)
    return resoudre(sorted(disques))


def main():
    print("Premier instant possible avec le disque #7:", solve(read_lines()))


if __name__ == "__main__":
    main()
