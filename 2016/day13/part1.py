"""2016, jour 13 : A Maze of Twisty Little Cubicles — partie 1.

Le plan est généré par la règle : la case (x, y) est un **mur** si
`x² + 3x + 2xy + y + y² + nombre_favori` a un nombre **impair** de bits à 1,
sinon c'est un espace libre. On part de (1, 1) et l'on cherche la plus courte
distance jusqu'à (31, 39).
"""

from collections import deque
from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day13.txt"
CIBLE = (31, 39)


def read_favori():
    """Renvoie le nombre favori (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return int(f.read().strip())
    return int(sys.stdin.read().strip())


def est_libre(x, y, favori):
    """Vrai si la case (x, y) est un espace ouvert."""
    if x < 0 or y < 0:
        return False
    valeur = x * x + 3 * x + 2 * x * y + y + y * y + favori
    return bin(valeur).count("1") % 2 == 0


def dessiner(favori, largeur=40, hauteur=45):
    """Rendu ASCII du labyrinthe (utile pour les tests et la lisibilité)."""
    return "\n".join(
        "".join("#" if not est_libre(x, y, favori) else "." for x in range(largeur))
        for y in range(hauteur)
    )


def distances(favori, limite=None):
    """Distances BFS depuis (1, 1), éventuellement bornées."""
    depart = (1, 1)
    distances_vues = {depart: 0}
    file = deque([depart])

    while file:
        x, y = file.popleft()
        distance = distances_vues[(x, y)]
        if limite is not None and distance >= limite:
            continue
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            voisin = (x + dx, y + dy)
            if voisin in distances_vues or not est_libre(*voisin, favori):
                continue
            distances_vues[voisin] = distance + 1
            file.append(voisin)

    return distances_vues


def solve(favori, cible=CIBLE):
    return distances(favori).get(cible)


def main():
    favori = read_favori()
    print("Distance minimale jusqu'à (31, 39):", solve(favori))


if __name__ == "__main__":
    main()
