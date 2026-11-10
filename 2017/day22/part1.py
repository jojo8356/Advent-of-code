"""2017, jour 22 : Sporifica Virus — partie 1.

Le virus démarre au centre de la grille, orienté vers le haut. À chaque rafale :
  - nœud infecté (`#`) → on tourne à **droite**, on nettoie le nœud ;
  - nœud sain (`.`)     → on tourne à **gauche**, on infecte le nœud ;
  - puis on avance d'une case.
Tout ce qui sort de la grille de départ est considéré comme sain.

Coordonnées : `(x, y)` avec `y` vers le bas (comme les lignes du fichier).
Réponse : nombre de rafales qui **infectent** un nœud, sur 10 000 rafales.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day22.txt"
RAFALES = 10_000

# (dx, dy) : haut, droite, bas, gauche  — attention `y` descend
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def read_grille():
    """Renvoie (ensemble des nœuds infectés, position initiale)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    texte = path.read_text() if path.exists() else sys.stdin.read()
    lignes = texte.split("\n")
    if lignes and lignes[-1] == "":
        lignes.pop()
    lignes = [ligne.ljust(max(len(l) for l in lignes)) for ligne in lignes]
    infectes = set()
    for y, ligne in enumerate(lignes):
        for x, caractere in enumerate(ligne):
            if caractere == "#":
                infectes.add((x, y))
    centre = (len(lignes) // 2, len(lignes[0]) // 2)
    return infectes, centre


def resoudre(infectes, centre, rafales=RAFALES, etats=None):
    """Fait tourner le virus ; renvoie le nombre de rafales infectantes.

    `etats` est une fonction (infecte, direction) -> (nouvel_état_départ,
    nouvelle_direction, infection_comptée) ; par défaut, la règle de la partie 1.
    """
    if etats is None:
        etats = regle_partie1
    position = centre
    direction = 0                     # 0 = haut
    infections = 0
    for _ in range(rafales):
        infecte = position in infectes
        infecte_apres, direction, compte = etats(infecte, direction)
        if infecte_apres:
            infectes.add(position)
        else:
            infectes.discard(position)
        infections += compte
        dx, dy = DIRECTIONS[direction]
        position = (position[0] + dx, position[1] + dy)
    return infections


def regle_partie1(infecte, direction):
    """Infecté → droite + nettoyage ; sain → gauche + infection."""
    if infecte:
        return False, (direction + 1) % 4, 0
    return True, (direction - 1) % 4, 1


def solve(lignes_ou_rien=None):
    infectes, centre = read_grille()
    return resoudre(infectes, centre)


def main():
    print("Rafales infectantes:", solve())


if __name__ == "__main__":
    main()
