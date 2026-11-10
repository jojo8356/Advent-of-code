"""2017, jour 2 : Corruption Checksum — partie 1.

Le tableur est une grille de nombres. Pour chaque ligne, on prend la
différence entre la plus grande et la plus petite valeur, puis on additionne
ces différences.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day02.txt"


def read_lignes():
    """Renvoie les lignes du tableur (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def parse_lignes(lines):
    """Liste de listes d'entiers."""
    return [[int(x) for x in ligne.split()] for ligne in lines if ligne.strip()]


def solve(lines):
    """Somme des écarts max − min de chaque ligne."""
    total = 0
    for ligne in parse_lignes(lines):
        total += max(ligne) - min(ligne)
    return total


def main():
    print("Somme des écarts:", solve(read_lignes()))


if __name__ == "__main__":
    main()
