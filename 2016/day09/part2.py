"""2016, jour 9 : Explosives in Cyberspace — partie 2.

Cette fois la décompression est **récursive** : le contenu répété par un
marqueur est lui-même décompressé. On ne construit jamais la chaîne (elle
serait énorme) : on calcule seulement sa longueur, mémorisée par position.
"""

from functools import lru_cache
from pathlib import Path
import sys

from part1 import read_data

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day09.txt"


def longueur_recursive(donnees):
    """Longueur après décompression complète (récursive), sans construire la chaîne."""
    n = len(donnees)

    @lru_cache(maxsize=None)
    def longueur(depart, fin):
        """Longueur décompressée de `donnees[depart:fin]`."""
        total = 0
        i = depart
        while i < fin:
            if donnees[i] == "(":
                fermeture = donnees.index(")", i)
                taille, repetitions = map(int, donnees[i + 1:fermeture].split("x"))
                debut_bloc = fermeture + 1
                total += repetitions * longueur(debut_bloc, debut_bloc + taille)
                i = debut_bloc + taille
            else:
                total += 1
                i += 1
        return total

    return longueur(0, n)


def solve(donnees):
    return longueur_recursive(donnees)


def main():
    print("Longueur décompressée (récursive):", solve(read_data()))


if __name__ == "__main__":
    main()
