"""2016, jour 18 : Like a Rogue — partie 2.

Même génération, mais sur **400 000** rangées.
"""

from pathlib import Path
import sys

from part1 import compter_sures, read_ligne

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day18.txt"
LIGNES = 400_000


def solve(ligne, lignes=LIGNES):
    return compter_sures(ligne, lignes)


def main():
    print(f"Tuiles sûres sur {LIGNES} rangées :", solve(read_ligne()))


if __name__ == "__main__":
    main()
