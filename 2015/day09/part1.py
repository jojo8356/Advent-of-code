"""Jour 9, partie 1 : plus court trajet visitant chaque ville une seule fois.

Les distances ne sont pas forcément symétriques ni complètes : on parcourt donc
les permutations (8 villes = 40 320 ordres, très raisonnable).
"""

from itertools import permutations
from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day09.txt"

DISTANCE = re.compile(r"(\w+) to (\w+) = (\d+)")


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def parse_distances(lines):
    """Construit {ville: {ville: distance}} à partir des lignes du puzzle."""
    distances = {}
    for line in lines:
        m = DISTANCE.search(line)
        if not m:
            continue
        depart, arrivee, km = m.group(1), m.group(2), int(m.group(3))
        distances.setdefault(depart, {})[arrivee] = km
        distances.setdefault(arrivee, {})[depart] = km
    return distances


def longueur(distances, trajet):
    return sum(distances[a][b] for a, b in zip(trajet, trajet[1:]))


def solve(lines):
    distances = parse_distances(lines)
    villes = list(distances)

    # Toutes les permutations : un trajet n'est pas un cycle, on ne peut donc
    # pas fixer arbitrairement la première ville.
    return min(longueur(distances, trajet) for trajet in permutations(villes))


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()
