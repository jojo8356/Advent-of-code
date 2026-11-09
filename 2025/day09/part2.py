"""Jour 9, partie 2 : plus grande zone rectangulaire entièrement verte.

Au lieu de colorier toute la grille (impossible à l'échelle du puzzle),
on teste chaque rectangle candidat : un rectangle est valide si ses quatre
coins sont dans le polygone et si aucune arête du polygone ne le traverse.
Même approche que `part2.rs`.
"""

from itertools import combinations
from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day09.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def point_in_polygon(x, y, vertices):
    """Test d'appartenance (ray casting) au polygone rectiligne des tuiles rouges."""
    n = len(vertices)
    inside = False

    j = n - 1
    for i in range(n):
        xi, yi = vertices[i]
        xj, yj = vertices[j]

        # Sur une arête horizontale
        if yi == yj and yi == y and min(xi, xj) <= x <= max(xi, xj):
            return True
        # Sur une arête verticale
        if xi == xj and xi == x and min(yi, yj) <= y <= max(yi, yj):
            return True

        if (yi > y) != (yj > y):
            x_intersect = (xj - xi) * (y - yi) // (yj - yi) + xi
            if x < x_intersect:
                inside = not inside
        j = i
    return inside


def rectangle_in_polygon(rx_min, ry_min, rx_max, ry_max, vertices):
    """Vrai si le rectangle est entièrement contenu dans le polygone."""
    corners = [
        (rx_min, ry_min),
        (rx_min, ry_max),
        (rx_max, ry_min),
        (rx_max, ry_max),
    ]
    for cx, cy in corners:
        if not point_in_polygon(cx, cy, vertices):
            return False

    # Aucune arête du polygone ne doit traverser l'intérieur du rectangle
    n = len(vertices)
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]

        if x1 == x2:
            ey_min, ey_max = sorted((y1, y2))
            if rx_min < x1 < rx_max and ey_min < ry_max and ey_max > ry_min:
                return False
        else:
            ex_min, ex_max = sorted((x1, x2))
            if ry_min < y1 < ry_max and ex_min < rx_max and ex_max > rx_min:
                return False

    return True


def solve(lines):
    tiles = []
    for line in lines:
        line = line.strip()
        if line:
            x, y = map(int, line.split(","))
            tiles.append((x, y))

    if len(tiles) < 2:
        return 0

    # Du plus grand rectangle au plus petit, avec sortie anticipée
    pairs = []
    for i, j in combinations(range(len(tiles)), 2):
        (x1, y1), (x2, y2) = tiles[i], tiles[j]
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        pairs.append((area, i, j))
    pairs.sort(reverse=True)

    max_area = 0
    for area, i, j in pairs:
        if area <= max_area:
            break
        (x1, y1), (x2, y2) = tiles[i], tiles[j]
        if rectangle_in_polygon(
            min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2), tiles
        ):
            max_area = area

    return max_area


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()
