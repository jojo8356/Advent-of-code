"""2017, jour 1 : Inverse Captcha — partie 1.

La séquence de chiffres est circulaire. On additionne chaque chiffre qui est
égal à **celui qui le suit immédiatement** (le dernier est comparé au premier).
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day01.txt"


def read_sequence():
    """Renvoie la séquence de chiffres (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    return sys.stdin.read().strip()


def somme_paires(sequence):
    """Somme des chiffres égaux à leur voisin de droite (circulaire)."""
    total = 0
    longueur = len(sequence)
    for i, chiffre in enumerate(sequence):
        if chiffre == sequence[(i + 1) % longueur]:
            total += int(chiffre)
    return total


def solve(sequence):
    return somme_paires(sequence)


def main():
    print("Somme des paires identiques:", solve(read_sequence()))


if __name__ == "__main__":
    main()
