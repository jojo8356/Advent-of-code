"""Jour 8, partie 1 : écart entre la longueur écrite et la longueur en mémoire.

Chaque ligne est un littéral entre guillemets. Sa longueur « code » est le
nombre de caractères écrits ; sa longueur « mémoire » est celle de la chaîne
une fois interprétée :
  - `\\"` et `\\\\` comptent pour un caractère,
  - `\\xNN` (deux chiffres hexadécimaux) compte pour un caractère,
  - les guillemets qui encadrent ne comptent pas.
On renvoie la somme des longueurs code moins la somme des longueurs mémoire.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day08.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def longueur_memoire(litteral):
    """Nombre de caractères réellement contenus dans la chaîne."""
    corps = litteral[1:-1]  # sans les guillemets d'encadrement
    i = 0
    n = 0
    while i < len(corps):
        if corps[i] == "\\":
            if corps[i + 1] == "x":
                i += 4  # \\xNN
            else:
                i += 2  # \\" ou \\\\
        else:
            i += 1
        n += 1
    return n


def solve(lines):
    litteraux = [line.strip() for line in lines if line.strip()]
    code = sum(len(l) for l in litteraux)
    memoire = sum(longueur_memoire(l) for l in litteraux)
    return code - memoire


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()
