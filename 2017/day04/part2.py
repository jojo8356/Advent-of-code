"""2017, jour 4 : High-Entropy Passphrases — partie 2.

Une phrase est valide si aucun mot n'est une **anagramme** d'un autre. On
compare donc l'ensemble des mots triés lettre par lettre.
"""

from pathlib import Path
import sys

from part1 import read_lines

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day04.txt"


def est_valide(phrase):
    """Vrai si les mots sont distincts à une permutation des lettres près."""
    mots = ["".join(sorted(mot)) for mot in phrase.split()]
    return len(mots) == len(set(mots))


def solve(lines):
    return sum(1 for ligne in lines if ligne.strip() and est_valide(ligne))


def main():
    print("Phrases valides (sans anagrammes):", solve(read_lines()))


if __name__ == "__main__":
    main()
