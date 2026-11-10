"""2017, jour 14 : Disk Defragmentation — partie 2.

Nombre de **régions** : composantes connexes de cases `1` reliées
orthogonalement (haut, bas, gauche, droite).
"""

from pathlib import Path
import sys

from part1 import read_sel, grille

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day14.txt"


def compter_regions(grille):
    """Nombre de composantes connexes de 1 (parcours en profondeur par pile)."""
    hauteur = len(grille)
    largeur = len(grille[0])
    vus = [[False] * largeur for _ in range(hauteur)]
    regions = 0
    for y in range(hauteur):
        for x in range(largeur):
            if grille[y][x] != 1 or vus[y][x]:
                continue
            regions += 1
            vus[y][x] = True
            pile = [(x, y)]
            while pile:
                cx, cy = pile.pop()
                for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
                    if 0 <= nx < largeur and 0 <= ny < hauteur:
                        if grille[ny][nx] == 1 and not vus[ny][nx]:
                            vus[ny][nx] = True
                            pile.append((nx, ny))
    return regions


def solve(sel):
    return compter_regions(grille(sel))


def main():
    print("Régions:", solve(read_sel()))


if __name__ == "__main__":
    main()
