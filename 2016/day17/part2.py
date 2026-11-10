"""2016, jour 17 : Two Steps Forward — partie 2.

Parmi **tous** les chemins qui mènent à la sortie, on cherche la **longueur**
du plus long. On explore exhaustivement, sans jamais s'arrêter au premier
chemin trouvé.
"""

from pathlib import Path
import sys

from part1 import chemins, read_key

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day17.txt"


def solve(key):
    """Longueur du plus long chemin vers la sortie."""
    return max(len(chemin) for chemin in chemins(key))


def main():
    print("Longueur du plus long chemin:", solve(read_key()))


if __name__ == "__main__":
    main()
