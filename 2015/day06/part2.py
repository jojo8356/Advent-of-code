"""Jour 6, partie 2 : luminosité totale de la grille.

Chaque lumière a un niveau de luminosité (0 minimum) :
  - `turn on`  -> +1
  - `turn off` -> -1 (sans descendre sous 0)
  - `toggle`   -> +2
On renvoie la somme des luminosités de la grille 1000 x 1000.
"""

from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day06.txt"

TAILLE = 1000
INSTRUCTION = re.compile(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def parse_instructions(lines):
    """Donne la liste (action, x1, y1, x2, y2) pour chaque ligne valide."""
    for line in lines:
        m = INSTRUCTION.search(line)
        if not m:
            continue
        action, x1, y1, x2, y2 = m.groups()
        yield action, int(x1), int(y1), int(x2), int(y2)


def solve(lines):
    grille = [[0] * TAILLE for _ in range(TAILLE)]

    for action, x1, y1, x2, y2 in parse_instructions(lines):
        for x in range(x1, x2 + 1):
            ligne = grille[x]
            for y in range(y1, y2 + 1):
                if action == "turn on":
                    ligne[y] += 1
                elif action == "turn off":
                    if ligne[y] > 0:
                        ligne[y] -= 1
                else:  # toggle
                    ligne[y] += 2

    return sum(sum(ligne) for ligne in grille)


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()
