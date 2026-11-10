"""2016, jour 17 : Two Steps Forward — partie 1.

Le labyrinthe est 4 × 4, entrée (0, 0), sortie (3, 3). Pour chaque état, on
hache MD5 de `sel + chemin` : les quatre premiers caractères hexadécimaux
donnent, dans l'ordre `U`, `D`, `L`, `R`, si la porte est **ouverte**
(`b`, `c`, `d`, `e`, `f`).

Réponse : plus court chemin (suite de `U`/`D`/`L`/`R`) de l'entrée à la sortie.
"""

from collections import deque
from hashlib import md5
from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day17.txt"
TAILLE = 4
OUVERTES = set("bcdef")
DEPLACEMENTS = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
}
ORDRE = "UDLR"


def read_key():
    """Renvoie le sel du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    return sys.stdin.read().strip()


def portes_ouvertes(sel, chemin):
    """Directions autorisées depuis la position courante."""
    empreinte = md5(f"{sel}{chemin}".encode()).hexdigest()
    return [direction for direction, lettre in zip(ORDRE, empreinte) if lettre in OUVERTES]


def voisins(sel, x, y, chemin):
    """Positions atteignables depuis (x, y) avec le chemin donné."""
    for direction in portes_ouvertes(sel, chemin):
        dx, dy = DEPLACEMENTS[direction]
        nx, ny = x + dx, y + dy
        if 0 <= nx < TAILLE and 0 <= ny < TAILLE:
            yield nx, ny, chemin + direction


def plus_court_chemin(sel):
    """Chemin le plus court vers (3, 3), ou None s'il n'y en a pas."""
    file = deque([(0, 0, "")])

    while file:
        x, y, chemin = file.popleft()
        for nx, ny, nouveau in voisins(sel, x, y, chemin):
            if (nx, ny) == (TAILLE - 1, TAILLE - 1):
                return nouveau
            file.append((nx, ny, nouveau))

    return None


def chemins(sel, jusqua=None):
    """Génère tous les chemins menant à la sortie (parcours en largeur)."""
    file = deque([(0, 0, "")])
    while file:
        x, y, chemin = file.popleft()
        for nx, ny, nouveau in voisins(sel, x, y, chemin):
            if (nx, ny) == (TAILLE - 1, TAILLE - 1):
                yield nouveau
            else:
                file.append((nx, ny, nouveau))


def solve(key):
    return plus_court_chemin(key)


def main():
    print("Plus court chemin:", solve(read_key()))


if __name__ == "__main__":
    main()
