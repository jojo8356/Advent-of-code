"""2017, jour 3 : Spiral Memory — partie 2.

Variante : chaque case reçoit la **somme de ses 8 voisines** déjà remplies (la
case 1 valant 1). On construit la spirale jusqu'à dépasser le numéro cherché
et l'on renvoie la première valeur supérieure.
"""

from pathlib import Path
import sys

from part1 import read_nombre

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day03.txt"

# directions dans le sens horaire : droite, haut, gauche, bas
DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def spirale_sommes(limite):
    """Première valeur de la spirale de sommes strictement supérieure à `limite`."""
    grille = {(0, 0): 1}
    x = y = 0
    longueur_cote = 1     # longueur du côté courant
    etapes_dans_cote = 0  # cases parcourues sur le côté courant
    index_direction = 0   # 0 = droite, 1 = haut, 2 = gauche, 3 = bas

    while True:
        dx, dy = DIRECTIONS[index_direction]
        x, y = x + dx, y + dy

        # somme des voisines déjà remplies
        total = 0
        for ox in (-1, 0, 1):
            for oy in (-1, 0, 1):
                if ox == 0 and oy == 0:
                    continue
                total += grille.get((x + ox, y + oy), 0)
        grille[(x, y)] = total

        if total > limite:
            return total

        # progression de la spirale : on change de côté tous les `longueur_cote`
        etapes_dans_cote += 1
        if etapes_dans_cote == longueur_cote:
            etapes_dans_cote = 0
            index_direction = (index_direction + 1) % 4
            if index_direction in (0, 2):   # on allonge tous les deux côtés
                longueur_cote += 1


def solve(n):
    return spirale_sommes(n)


def main():
    print("Première valeur supérieure:", solve(read_nombre()))


if __name__ == "__main__":
    main()
