"""2016, jour 6 : Signals and Noise — partie 1.

Chaque ligne est un message bruité de même longueur. Le message corrigé
s'obtient en prenant, **colonne par colonne**, le caractère le plus fréquent.
"""

from collections import Counter
from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day06.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def colonnes(lignes):
    """Transpose : liste des colonnes du tableau de caractères."""
    messages = [ligne.strip() for ligne in lignes if ligne.strip()]
    return list(zip(*messages))


def caractere_dominant(colonne):
    """Caractère le plus fréquent ; à égalité, le plus petit alphabétiquement."""
    return min(Counter(colonne).items(), key=lambda paire: (-paire[1], paire[0]))[0]


def solve(lines):
    return "".join(caractere_dominant(colonne) for colonne in colonnes(lines))


def main():
    print("Message corrigé:", solve(read_lines()))


if __name__ == "__main__":
    main()
