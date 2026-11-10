"""2017, jour 17 : Spinlock — partie 2.

50 millions d'insertions : le tampon complet serait trop volumineux. Mais on ne
cherche que la valeur qui suit **0**. Or 0 reste toujours en position 0 : la
valeur insérée en **position 1** devient donc la voisine droite de 0, et elle est
écrasée par la suivante. Il suffit de suivre la position et la longueur.

Attention : on compte les insertions en excluant le 0 initial (valeur 0 ne compte
pas) et la réponse est la dernière valeur insérée en position 1 parmi les
50 000 000 insertions, en **ignorant** le 0 de départ.
"""

from pathlib import Path
import sys

from part1 import read_pas

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day17.txt"
INSERTIONS = 50_000_000


def voisine_de_zero(pas, insertions=INSERTIONS):
    """Valeur insérée en position 1 lors de la dernière insertion qui y tombe."""
    position = 0
    longueur = 1                     # le tampon ne contient que [0]
    resultat = 0
    for valeur in range(1, insertions + 1):
        position = (position + pas) % longueur + 1
        longueur += 1
        if position == 1:
            resultat = valeur
    return resultat


def solve(pas, insertions=INSERTIONS):
    return voisine_de_zero(pas, insertions)


def main():
    print("Valeur après 0:", solve(read_pas()))


if __name__ == "__main__":
    main()
