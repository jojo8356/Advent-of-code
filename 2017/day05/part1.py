"""2017, jour 5 : A Maze of Twisty Trampolines, All Alike — partie 1.

On part de l'instruction 0. On lit l'offset, on saute de cet offset, puis on
incrémente de 1 l'offset qu'on vient de quitter. On compte les sauts jusqu'à
sortir du tableau.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day05.txt"


def read_offsets():
    """Renvoie la liste des offsets (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            lignes = f.readlines()
    else:
        lignes = sys.stdin.readlines()
    return [int(l) for l in lignes if l.strip()]


def sauter(offsets, decalage=None):
    """Compte les sauts pour sortir. `decalage(offset)` donne l'incrément."""
    if decalage is None:
        decalage = lambda o: 1
    offsets = list(offsets)
    position = 0
    sauts = 0
    while 0 <= position < len(offsets):
        offset = offsets[position]
        offsets[position] = offset + decalage(offset)
        position += offset
        sauts += 1
    return sauts


def solve(offsets):
    return sauter(offsets)


def main():
    print("Sauts:", solve(read_offsets()))


if __name__ == "__main__":
    main()
