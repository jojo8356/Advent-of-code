"""2017, jour 10 : Knot Hash — partie 2.

- Longueurs = codes ASCII de la chaîne d'entrée, suivis de `[17, 31, 73, 47, 23]`.
- On effectue **64 tours** en conservant position et saut d'un tour à l'autre.
- Hash dense : XOR des 16 nombres de chaque bloc (16 blocs).
- Sortie : 32 caractères hexadécimaux (2 par bloc).
"""

from pathlib import Path
import sys

from part1 import read_texte, un_tour

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day10.txt"
TAILLE = 256
SUFFIXE = [17, 31, 73, 47, 23]
TOURS = 64


def longueurs_hash(texte):
    """Codes ASCII de la chaîne + suffixe."""
    return [ord(c) for c in texte] + SUFFIXE


def hash_dense(liste):
    """XOR par blocs de 16 puis hexadécimal sur 32 caractères."""
    blocs = []
    for debut in range(0, len(liste), 16):
        valeur = 0
        for v in liste[debut:debut + 16]:
            valeur ^= v
        blocs.append(valeur)
    return "".join(f"{b:02x}" for b in blocs)


def hasher(texte, taille=TAILLE):
    """Hash Knot complet (64 tours) de la chaîne."""
    liste = list(range(taille))
    position = saut = 0
    longueurs = longueurs_hash(texte)
    for _ in range(TOURS):
        liste, position, saut = un_tour(liste, longueurs, position, saut)
    return hash_dense(liste)


def solve(texte):
    return hasher(texte)


def main():
    print("Knot hash:", solve(read_texte()))


if __name__ == "__main__":
    main()
