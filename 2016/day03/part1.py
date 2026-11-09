"""2016, jour 3 : Squares With Three Sides — partie 1.

Chaque ligne du fichier donne les trois côtés d'un triangle. Un triangle est
valide si la somme de deux côtés quelconques dépasse le troisième — il suffit
de tester les deux plus petits contre le plus grand.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day03.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def est_valide(a, b, c):
    """Un triangle est valide si ses deux plus petits côtés dépassent le plus grand."""
    a, b, c = sorted((a, b, c))
    return a + b > c


def solve(lines):
    """Nombre de triangles valides, un par ligne."""
    total = 0
    for ligne in lines:
        nombres = [int(x) for x in ligne.split()]
        if len(nombres) == 3 and est_valide(*nombres):
            total += 1
    return total


def main():
    print("Triangles valides:", solve(read_lines()))


if __name__ == "__main__":
    main()
