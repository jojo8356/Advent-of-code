"""2016, jour 24 : Air Duct Spelunking — partie 1.

Le plan est une grille (`#` = mur, `.` = couloir, `0`–`7` = points d'intérêt).
On part du point `0` et l'on doit visiter **tous** les autres points.

Méthode : BFS sur la grille depuis chaque point pour obtenir les distances
deux à deux, puis parcours des permutations pour trouver le tour le plus court.
"""

from collections import deque
from itertools import permutations
from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day24.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.read().splitlines()
    return sys.stdin.read().splitlines()


def parse_carte(lines):
    """Renvoie (grille, points) où points associe un numéro à sa position."""
    grille = [list(ligne) for ligne in lines if ligne.strip()]
    points = {}
    for y, ligne in enumerate(grille):
        for x, case in enumerate(ligne):
            if case.isdigit():
                points[int(case)] = (x, y)
    return grille, points


def distances_depuis(grille, depart, hauteur, largeur):
    """Distances BFS depuis `depart` vers toutes les cases atteignables."""
    distances = {depart: 0}
    file = deque([depart])

    while file:
        x, y = file.popleft()
        d = distances[(x, y)]
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if not (0 <= ny < hauteur and 0 <= nx < largeur):
                continue
            if grille[ny][nx] == "#" or (nx, ny) in distances:
                continue
            distances[(nx, ny)] = d + 1
            file.append((nx, ny))

    return distances


def matrice_distances(grille, points):
    """Distances deux à deux entre les points d'intérêt."""
    hauteur, largeur = len(grille), len(grille[0])
    numeros = sorted(points)
    distances = {}

    for numero in numeros:
        atteignables = distances_depuis(grille, points[numero], hauteur, largeur)
        for autre in numeros:
            if autre != numero:
                distances[(numero, autre)] = atteignables[points[autre]]

    return distances


def plus_court_tour(distances, numeros, retour=False):
    """Coût du plus court parcours visitant tous les points depuis 0."""
    autres = [n for n in numeros if n != 0]
    meilleur = None

    for ordre in permutations(autres):
        cout = 0
        courant = 0
        for suivant in ordre:
            cout += distances[(courant, suivant)]
            courant = suivant
        if retour:
            cout += distances[(courant, 0)]
        if meilleur is None or cout < meilleur:
            meilleur = cout

    return meilleur


def solve(lines, retour=False):
    grille, points = parse_carte(lines)
    distances = matrice_distances(grille, points)
    return plus_court_tour(distances, sorted(points), retour=retour)


def main():
    print("Plus court parcours:", solve(read_lines()))


if __name__ == "__main__":
    main()
