"""Jour 5, partie 2 : compter les chaînes « gentilles » avec les nouvelles règles.

Une chaîne est gentille si elle contient :
  - une paire de deux lettres identiques séparées par exactement une lettre
    (par exemple `x?x` avec n'importe quel caractère au milieu),
  - une paire de deux lettres qui réapparaît plus loin sans se chevaucher
    (par exemple `ab...ab`).
"""

from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day05.txt"

PAIRE_ESPACEE = re.compile(r"(.)(.)\1")
PAIRE_REPETEE = re.compile(r"(..).*\1")


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def is_nice(string):
    """Applique les deux règles de la partie 2."""
    if not PAIRE_ESPACEE.search(string):
        return False
    if not PAIRE_REPETEE.search(string):
        return False
    return True


def solve(lines):
    return sum(1 for line in lines if is_nice(line.strip()))


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()
