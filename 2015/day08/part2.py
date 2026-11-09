"""Jour 8, partie 2 : écart entre la longueur ré-encodée et la longueur code.

On encode à nouveau chaque littéral pour qu'il soit une chaîne valide :
  - chaque `"` et chaque `\\` est précédé d'un antislash,
  - on entoure le tout de guillemets.
On renvoie la somme des longueurs ré-encodées moins la somme des longueurs code.
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


def encoder(litteral):
    """Ré-encode un littéral : antislash devant `"` et `\\`, puis guillemets."""
    morceaux = []
    for caractere in litteral:
        if caractere in ('"', "\\"):
            morceaux.append("\\")
        morceaux.append(caractere)
    return '"' + "".join(morceaux) + '"'


def solve(lines):
    litteraux = [line.strip() for line in lines if line.strip()]
    code = sum(len(l) for l in litteraux)
    encodee = sum(len(encoder(l)) for l in litteraux)
    return encodee - code


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()
