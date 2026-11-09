"""2016, jour 6 : Signals and Noise — partie 2.

Le vrai message est celui qui apparaît **le moins souvent** dans chaque
colonne (les erreurs de transmission étant plus fréquentes que la vérité).
"""

from collections import Counter
from pathlib import Path
import sys

from part1 import colonnes, read_lines

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day06.txt"


def caractere_minoritaire(colonne):
    """Caractère le moins fréquent ; à égalité, le plus petit alphabétiquement."""
    return min(Counter(colonne).items(), key=lambda paire: (paire[1], paire[0]))[0]


def solve(lines):
    return "".join(caractere_minoritaire(colonne) for colonne in colonnes(lines))


def main():
    print("Message corrigé (caractère minoritaire):", solve(read_lines()))


if __name__ == "__main__":
    main()
