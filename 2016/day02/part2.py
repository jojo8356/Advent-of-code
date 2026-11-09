"""2016, jour 2 : Bathroom Security — partie 2.

Même principe, mais le pavé est le losange à 13 boutons (`1`–`9`, `A`–`D`) ;
on part du bouton 5 au centre. Les déplacements hors du losange sont ignorés.
"""

from pathlib import Path
import sys

from part1 import code, read_lines

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day02.txt"

LIGNES = [
    "..1..",
    ".234.",
    "56789",
    ".ABC.",
    "..D..",
]

PAVE = {
    (x, y): bouton
    for y, ligne in enumerate(LIGNES)
    for x, bouton in enumerate(ligne)
    if bouton != "."
}
DEPART = (0, 2)  # le bouton 5, au centre du losange


def solve(lines):
    return code(lines, pave=PAVE, depart=DEPART)


def main():
    print("Code:", solve(read_lines()))


if __name__ == "__main__":
    main()
