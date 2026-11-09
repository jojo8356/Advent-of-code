"""Jour 9, partie 2 : plus long trajet visitant chaque ville une seule fois.

Même parcours exhaustif que la partie 1, mais on cherche le maximum.
"""

from itertools import permutations
from pathlib import Path
import sys

from part1 import longueur, parse_distances

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day09.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def solve(lines):
    distances = parse_distances(lines)
    villes = list(distances)

    # Toutes les permutations : un trajet n'est pas un cycle, on ne peut donc
    # pas fixer arbitrairement la première ville.
    return max(longueur(distances, trajet) for trajet in permutations(villes))


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()
