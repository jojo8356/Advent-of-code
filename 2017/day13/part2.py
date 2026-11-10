"""2017, jour 13 : Packet Scanners — partie 2.

Plus petit délai permettant de traverser **sans aucune** collision : plus petit
`d` tel que `(d + profondeur) % periode != 0` pour chaque scanner.

On teste les délais dans l'ordre croissant et, pour chaque délai, on évalue les
scanners par **période croissante** : les petites fenêtres éliminent presque
tous les délais, donc la boucle interne sort en un ou deux tests. C'est un
balayage exhaustif — contrairement à une progression par PPCM, il ne peut pas
sauter la bonne réponse.
"""

from pathlib import Path
import sys

from part1 import read_lignes, parse, periode

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day13.txt"


def est_sur(scanners, delai):
    """Vrai si aucune collision pour ce délai."""
    return all((delai + profondeur) % periode(fenetre) != 0
               for profondeur, fenetre in scanners)


def premier_delai(scanners):
    """Plus petit délai sans collision."""
    ordre = sorted(scanners, key=lambda s: periode(s[1]))
    delai = 0
    while not est_sur(ordre, delai):
        delai += 1
    return delai


def solve(lignes):
    return premier_delai(parse(lignes))


def main():
    print("Premier délai sûr:", solve(read_lignes()))


if __name__ == "__main__":
    main()
