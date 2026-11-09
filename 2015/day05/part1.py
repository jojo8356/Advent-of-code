"""Jour 5, partie 1 : compter les chaînes « gentilles ».

Une chaîne est gentille si elle contient :
  - au moins 3 voyelles (a, e, i, o, u),
  - au moins une lettre doublée (aa, bb, ...),
  - aucune des paires interdites : ab, cd, pq, xy.
"""

from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day05.txt"

VOYELLES = re.compile(r"[aeiou]")
DOUBLE = re.compile(r"(.)\1")
INTERDITES = re.compile(r"ab|cd|pq|xy")


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def is_nice(string):
    """Applique les trois règles de la partie 1."""
    if len(VOYELLES.findall(string)) < 3:
        return False
    if not DOUBLE.search(string):
        return False
    if INTERDITES.search(string):
        return False
    return True


def solve(lines):
    return sum(1 for line in lines if is_nice(line.strip()))


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()
