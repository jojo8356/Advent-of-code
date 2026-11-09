"""2016, jour 9 : Explosives in Cyberspace — partie 1.

Le fichier est compressé avec des marqueurs `(LxF)` : les `L` caractères qui
suivent le marqueur sont répétés `F` fois. Les marqueurs ne comptent pas dans
la longueur décompressée et une **seule passe** est appliquée : le contenu
répété n'est pas ré-examiné (les marqueurs qu'il contient restent du texte).
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day09.txt"


def read_data():
    """Renvoie la ligne compressée (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    return sys.stdin.read().strip()


def longueur_decompressee(donnees):
    """Longueur après une seule décompression."""
    longueur = 0
    i = 0
    n = len(donnees)

    while i < n:
        if donnees[i] == "(":
            fin = donnees.index(")", i)
            taille, repetitions = map(int, donnees[i + 1:fin].split("x"))
            longueur += taille * repetitions
            i = fin + 1 + taille
        else:
            longueur += 1
            i += 1

    return longueur


def solve(donnees):
    return longueur_decompressee(donnees)


def main():
    print("Longueur décompressée:", solve(read_data()))


if __name__ == "__main__":
    main()
