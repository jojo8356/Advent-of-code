"""2016, jour 4 : Security Through Obscurity — partie 2.

On déchiffre le nom de chaque salle valide par un décalage de César valant son
identifiant (modulo 26, les tirets deviennent des espaces) et on cherche la
salle « northpole object storage ». Réponse : son identifiant.
"""

from pathlib import Path
import sys

from part1 import parse_salle, read_lines, somme_de_controle

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day04.txt"

CIBLE = "northpole object storage"


def dechiffrer(nom, decalage):
    """Décale chaque lettre de `decalage` (a→z circulaire) ; les tirets deviennent des espaces."""
    decalage %= 26
    resultat = []
    for caractere in nom:
        if caractere == "-":
            resultat.append(" ")
        else:
            resultat.append(chr((ord(caractere) - ord("a") + decalage) % 26 + ord("a")))
    return "".join(resultat)


def solve(lines, cible=CIBLE):
    """Identifiant de la salle dont le nom déchiffré vaut `cible`."""
    for ligne in lines:
        if not ligne.strip():
            continue
        nom, identifiant, controle = parse_salle(ligne)
        if somme_de_controle(nom) != controle:
            continue
        if dechiffrer(nom, identifiant) == cible:
            return identifiant
    return "salle introuvable"


def main():
    print(f"Identifiant de « {CIBLE} » :", solve(read_lines()))


if __name__ == "__main__":
    main()
