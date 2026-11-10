"""2017, jour 11 : Hex Ed — partie 1.

Grille hexagonale « pointue » : six directions `n, ne, se, s, sw, nw`.
En coordonnées cube (x + y + z = 0), la distance est
`(abs(x) + abs(y) + abs(z)) / 2`.

Réponse : distance après avoir suivi tout le chemin.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day11.txt"

# déplacements en coordonnées cube (x, y, z) avec x + y + z = 0
DIRECTIONS = {
    "n": (0, 1, -1),
    "ne": (1, 0, -1),
    "se": (1, -1, 0),
    "s": (0, -1, 1),
    "sw": (-1, 0, 1),
    "nw": (-1, 1, 0),
}


def read_chemin():
    """Renvoie la liste des pas (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    texte = path.read_text() if path.exists() else sys.stdin.read()
    return [pas for pas in texte.replace("\n", "").split(",") if pas.strip()]


def distance(position):
    """Distance en pas depuis l'origine, en coordonnées cube."""
    return (abs(position[0]) + abs(position[1]) + abs(position[2])) // 2


def parcourir(pas, depart=(0, 0, 0)):
    """Renvoie (position finale, distance maximale atteinte en chemin)."""
    x, y, z = depart
    maximum = distance((x, y, z))
    for p in pas:
        dx, dy, dz = DIRECTIONS[p]
        x += dx
        y += dy
        z += dz
        maximum = max(maximum, distance((x, y, z)))
    return (x, y, z), maximum


def solve(pas):
    position, _ = parcourir(pas)
    return distance(position)


def main():
    print("Distance finale:", solve(read_chemin()))


if __name__ == "__main__":
    main()
