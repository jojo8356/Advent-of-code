"""2017, jour 6 : Memory Reallocation — partie 2.

Une fois la configuration répétée trouvée, on mesure la **taille de la boucle** :
nombre de cycles entre les deux apparitions de cette configuration.
"""

from pathlib import Path
import sys

from part1 import read_bancs, cycles, redistribuer

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day06.txt"


def taille_boucle(bancs):
    """Nombre de cycles qui séparent les deux occurrences de la configuration."""
    _, repetee = cycles(bancs)
    courant = tuple(redistribuer(repetee))
    n = 1
    while courant != repetee:
        courant = tuple(redistribuer(courant))
        n += 1
    return n


def solve(bancs):
    return taille_boucle(bancs)


def main():
    print("Taille de la boucle:", solve(read_bancs()))


if __name__ == "__main__":
    main()
