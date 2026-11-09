"""Jour 10, partie 1 : 40 itérations de « look-and-say », puis longueur du résultat.

Une itération décrit la chaîne précédente en groupes de chiffres identiques :
`1` -> `11`, `11` -> `21`, `21` -> `1211`, `1211` -> `111221`, ...
On renvoie la longueur de la chaîne après 40 itérations.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day10.txt"


def read_key():
    """Renvoie la séquence de départ (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    return sys.stdin.read().strip()


def dire(sequence):
    """Applique une itération look-and-say."""
    morceaux = []
    i = 0
    while i < len(sequence):
        chiffre = sequence[i]
        j = i
        while j < len(sequence) and sequence[j] == chiffre:
            j += 1
        morceaux.append(str(j - i))
        morceaux.append(chiffre)
        i = j
    return "".join(morceaux)


def solve(sequence, iterations=40):
    for _ in range(iterations):
        sequence = dire(sequence)
    return len(sequence)


def main():
    print(solve(read_key()))


if __name__ == "__main__":
    main()
