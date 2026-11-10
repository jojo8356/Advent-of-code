"""2016, jour 20 : Firewall Rules — partie 2.

Réponse : nombre d'adresses IP de 0 à 4 294 967 295 qui **ne sont bloquées par
aucune** plage. On fusionne les plages puis on additionne les trous, bornes de
l'espace d'adressage comprises.
"""

from pathlib import Path
import sys

from part1 import MAX_IP, fusionner, parse_plages, read_lines

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day20.txt"


def compter_libres(plages, maximum=MAX_IP):
    """Nombre d'adresses autorisées dans [0, maximum]."""
    fusionnees = fusionner(plages)
    libres = 0
    curseur = 0

    for debut, fin in fusionnees:
        if debut > curseur:
            libres += debut - curseur  # trou avant cette plage
        curseur = max(curseur, fin + 1)
        if curseur > maximum:
            break

    if curseur <= maximum:
        libres += maximum - curseur + 1  # trou après la dernière plage

    return libres


def solve(lines, maximum=MAX_IP):
    return compter_libres(parse_plages(lines), maximum)


def main():
    print("Adresses autorisées:", solve(read_lines()))


if __name__ == "__main__":
    main()
