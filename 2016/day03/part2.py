"""2016, jour 3 : Squares With Three Sides — partie 2.

Les nombres se lisent **par colonnes** : en prenant les trois lignes d'un bloc,
chaque colonne forme un triangle. Bloc 1 → colonne 1, puis colonne 2, puis
colonne 3.
"""

from pathlib import Path
import sys

from part1 import est_valide, read_lines

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day03.txt"


def triangles_par_colonnes(lignes):
    """Découpe les nombres en triangles lus verticalement, 3 lignes par bloc."""
    nombres = [[int(x) for x in ligne.split()] for ligne in lignes if ligne.strip()]
    triangles = []
    for debut in range(0, len(nombres) - 2, 3):
        bloc = nombres[debut:debut + 3]
        for colonne in range(3):
            triangles.append(tuple(bloc[ligne][colonne] for ligne in range(3)))
    return triangles


def solve(lines):
    """Nombre de triangles valides lus par colonnes."""
    return sum(1 for triangle in triangles_par_colonnes(lines) if est_valide(*triangle))


def main():
    print("Triangles valides (lecture par colonnes):", solve(read_lines()))


if __name__ == "__main__":
    main()
