"""2017, jour 4 : High-Entropy Passphrases — partie 1.

Une phrase est valide si **aucun** de ses mots n'apparaît deux fois.
Réponse : nombre de phrases valides.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day04.txt"


def read_lines():
    """Renvoie les phrases (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def est_valide(phrase):
    """Vrai si aucun mot ne se répète."""
    mots = phrase.split()
    return len(mots) == len(set(mots))


def solve(lines):
    return sum(1 for ligne in lines if ligne.strip() and est_valide(ligne))


def main():
    print("Phrases valides:", solve(read_lines()))


if __name__ == "__main__":
    main()
