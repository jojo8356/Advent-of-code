"""2016, jour 11 : Radioisotope Thermoelectric Generators — partie 2.

On ajoute, au premier étage, un générateur et une puce **elerium** ainsi
qu'un générateur et une puce **dilithium**, puis on recalcule la distance
minimale avec le même BFS canonisé.
"""

from pathlib import Path
import sys

from part1 import distance_minimale, parse_etages, read_lines

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day11.txt"


def solve(lines, nb_etages=4):
    objets = parse_etages(lines)
    objets["elerium"] = (1, 1)
    objets["dilithium"] = (1, 1)
    return distance_minimale(objets, nb_etages)


def main():
    print("Trajets minimaux avec elerium et dilithium:", solve(read_lines()))


if __name__ == "__main__":
    main()
