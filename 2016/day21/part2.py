"""2016, jour 21 : Scrambled Letters and Hash — partie 2.

On cherche le mot de passe qui, une fois brouillé, donne `fbgdceah`. Les
instructions ne sont pas toutes inversibles directement (`rotate based on
position...` ne l'est pas), mais sur **8 lettres** il n'y a que 40320
permutations : on les essaie toutes. C'est immédiat et sans risque d'erreur.
"""

from itertools import permutations
from pathlib import Path
import sys

from part1 import appliquer, read_lines

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day21.txt"
CIBLE = "fbgdceah"
ALPHABET = "abcdefgh"


def solve(lines, cible=CIBLE, alphabet=ALPHABET):
    """Mot de passe d'origine (le plus petit, s'il y en avait plusieurs)."""
    for candidat in permutations(alphabet):
        mot = "".join(candidat)
        if appliquer(mot, lines) == cible:
            return mot
    return "aucun antécédent"


def main():
    print("Mot de passe d'origine:", solve(read_lines()))


if __name__ == "__main__":
    main()
