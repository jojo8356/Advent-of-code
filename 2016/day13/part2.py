"""2016, jour 13 : A Maze of Twisty Little Cubicles — partie 2.

Combien de cases sont atteignables en **au plus 50 pas** depuis (1, 1) ?
On relance le BFS en s'arrêtant à la distance 50 et on compte les cases vues.
"""

from pathlib import Path
import sys

from part1 import distances, read_favori

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day13.txt"
LIMITE = 50


def solve(favori, limite=LIMITE):
    return len(distances(favori, limite=limite))


def main():
    print(f"Cases atteignables en au plus {LIMITE} pas:", solve(read_favori()))


if __name__ == "__main__":
    main()
