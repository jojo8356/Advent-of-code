"""2017, jour 22 : Sporifica Virus — partie 2.

Quatre états par nœud : sain (`.`) → **affaibli** (`W`) → **infecté** (`#`) →
**drapeau** (`F`) → sain, avec pour chacun un comportement propre :
  - sain     : tourne à gauche, devient affaibli,
  - affaibli : ne tourne pas, devient infecté (**compte** comme infection),
  - infecté  : tourne à droite, devient drapeau,
  - drapeau   : demi-tour, redevient sain.
Réponse : infections comptées, sur 10 000 000 de rafales.
"""

from pathlib import Path
import sys

from part1 import read_grille, resoudre

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day22.txt"
RAFALES = 10_000_000


def solve():
    """Il faut un état à 4 valeurs : on remplace la table des nœuds."""
    from part1 import DIRECTIONS
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    texte = path.read_text() if path.exists() else sys.stdin.read()
    lignes = texte.split("\n")
    if lignes and lignes[-1] == "":
        lignes.pop()
    lignes = [ligne.ljust(max(len(l) for l in lignes)) for ligne in lignes]
    noeuds = {}
    for y, ligne in enumerate(lignes):
        for x, caractere in enumerate(ligne):
            if caractere == "#":
                noeuds[(x, y)] = "infecte"

    centre = (len(lignes) // 2, len(lignes[0]) // 2)
    position = centre
    direction = 0
    infections = 0

    for _ in range(RAFALES):
        etat = noeuds.get(position, "sain")
        if etat == "sain":
            nouvelle_direction = (direction - 1) % 4
            noeuds[position] = "affaibli"
        elif etat == "affaibli":
            nouvelle_direction = direction
            noeuds[position] = "infecte"
            infections += 1
        elif etat == "infecte":
            nouvelle_direction = (direction + 1) % 4
            noeuds[position] = "drapeau"
        else:                                       # drapeau
            nouvelle_direction = (direction + 2) % 4
            del noeuds[position]                        # redevient sain
        direction = nouvelle_direction
        dx, dy = DIRECTIONS[direction]
        position = (position[0] + dx, position[1] + dy)

    return infections


def main():
    print("Infections:", solve())


if __name__ == "__main__":
    main()
