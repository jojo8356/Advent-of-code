"""2017, jour 19 : A Series of Tubes — partie 1.

Le paquet part du `|` de la première ligne et descend. Il suit le tube :
  - `|` et `-` : on continue tout droit,
  - `+` : on tourne (la seule direction perpendiculaire qui n'est pas vide),
  - une lettre : on la note, on continue,
  - un espace : le parcours est terminé.

Réponse : les lettres traversées, dans l'ordre.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day19.txt"

# (ligne, colonne) : bas, haut, droite, gauche
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def read_grille():
    """Renvoie la grille en liste de chaînes (longueur uniformisée)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    texte = path.read_text() if path.exists() else sys.stdin.read()
    lignes = texte.split("\n")
    if lignes and lignes[-1] == "":
        lignes.pop()
    largeur = max(len(ligne) for ligne in lignes) if lignes else 0
    return [ligne.ljust(largeur) for ligne in lignes]


def trouver_depart(grille):
    """Position du `|` de la première ligne."""
    for colonne, caractere in enumerate(grille[0]):
        if caractere == "|":
            return (0, colonne)
    raise ValueError("aucun point de départ sur la première ligne")


def dans_la_grille(grille, ligne, colonne):
    return 0 <= ligne < len(grille) and 0 <= colonne < len(grille[0])


def case(grille, ligne, colonne):
    """Caractère de la case, ou espace hors de la grille."""
    if dans_la_grille(grille, ligne, colonne):
        return grille[ligne][colonne]
    return " "


def parcourir(grille):
    """Renvoie (lettres traversées, nombre de cases parcourues)."""
    ligne, colonne = trouver_depart(grille)
    direction = (1, 0)                      # on descend au départ
    lettres = []
    pas = 0

    while True:
        caractere = case(grille, ligne, colonne)
        if caractere == " ":
            break
        pas += 1
        if caractere.isalpha():
            lettres.append(caractere)

        # où aller ensuite ?
        dl, dc = direction
        if caractere == "+":
            # on tourne : seule la perpendiculaire non vide est possible
            for candidat in (perpendiculaire(direction)):
                nl, nc = ligne + candidat[0], colonne + candidat[1]
                if case(grille, nl, nc) != " ":
                    direction = candidat
                    break
            else:
                break
            dl, dc = direction

        suite_l, suite_c = ligne + dl, colonne + dc
        if case(grille, suite_l, suite_c) == " ":
            break
        ligne, colonne = suite_l, suite_c

    return "".join(lettres), pas


def perpendiculaire(direction):
    """Les deux directions perpendiculaires à `direction`."""
    dl, dc = direction
    if dl == 0:                             # on va horizontalement
        return [(1, 0), (-1, 0)]
    return [(0, 1), (0, -1)]                # on va verticalement


def solve(grille):
    return parcourir(grille)[0]


def main():
    print("Lettres:", solve(read_grille()))


if __name__ == "__main__":
    main()
