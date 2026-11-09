"""2016, jour 5 : How About a Nice Game of Chess? — partie 2.

Même principe, mais les hachages doivent commencer par **six zéros** à partir
du 4ᵉ. Le 6ᵉ caractère hexadécimal (0–7) donne la **position**, le 7ᵉ donne le
caractère. On ignore les positions déjà remplies et celles hors de 0–7.
"""

from hashlib import md5
from pathlib import Path
import sys

from part1 import read_key

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day05.txt"
PREFIXE = "00000"


def mot_de_passe_positionnel(sel, longueur=8):
    """Mot de passe où chaque hachage valide remplit une position imposée."""
    resultat = [None] * longueur
    trouves = 0
    indice = 0

    while trouves < longueur:
        empreinte = md5(f"{sel}{indice}".encode()).hexdigest()
        indice += 1
        if not empreinte.startswith(PREFIXE):
            continue

        position = empreinte[5]
        if position in "89abcdef":  # hors de la plage 0–7
            continue
        position = int(position)
        if resultat[position] is not None:  # position déjà remplie
            continue

        resultat[position] = empreinte[6]
        trouves += 1

    return "".join(resultat)


def solve(sel):
    return mot_de_passe_positionnel(sel)


def main():
    print("Password:", solve(read_key()))


if __name__ == "__main__":
    main()
