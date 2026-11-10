"""2017, jour 12 : Digital Plumber — partie 2.

Nombre total de groupes (composantes connexes) dans le graphe.
"""

from pathlib import Path
import sys

from part1 import read_lines, parse, composante

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day12.txt"


def compter_groupes(voisins):
    """Nombre de composantes connexes."""
    restants = set(voisins)
    groupes = 0
    while restants:
        depart = restants.pop()
        groupe = composante(voisins, depart)
        restants -= groupe
        groupes += 1
    return groupes


def solve(lignes):
    return compter_groupes(parse(lignes))


def main():
    print("Nombre de groupes:", solve(read_lines()))


if __name__ == "__main__":
    main()
