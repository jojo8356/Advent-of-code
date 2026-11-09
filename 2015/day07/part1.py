"""Jour 7, partie 1 : simuler le circuit et lire le fil `a`.

Chaque ligne est une affectation `expression -> fil`, où l'expression est :
  - un nombre ou un autre fil                 (`123 -> x`, `y -> x`)
  - `NOT fil`                                  (complément à 16 bits)
  - `fil AND fil`, `fil OR fil`                (opérations bit à bit)
  - `fil LSHIFT n`, `fil RSHIFT n`             (décalages)
Les opérandes peuvent aussi être des constantes. Les fils non encore calculés
sont évalués à la demande (mémoïsation), donc l'ordre des lignes n'importe pas.
"""

from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day07.txt"
MASQUE = 0xFFFF


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def parse_lines(lines):
    """Donne {fil: expression} où l'expression est une chaîne de tokens."""
    instructions = {}
    for line in lines:
        line = line.strip()
        if not line or "->" not in line:
            continue
        expression, fil = line.split("->")
        instructions[fil.strip()] = expression.split()
    return instructions


def evaluate(instructions, fil, memo=None):
    """Valeur du fil, en évaluant récursivement ce qui est nécessaire."""
    if memo is None:
        memo = {}
    if fil in memo:
        return memo[fil]

    if fil.isdigit():
        return int(fil)

    tokens = instructions[fil]

    if len(tokens) == 1:                       # `x -> f` ou `123 -> f`
        valeur = evaluate(instructions, tokens[0], memo)
    elif tokens[0] == "NOT":                   # `NOT x -> f`
        valeur = ~evaluate(instructions, tokens[1], memo) & MASQUE
    else:                                      # `x OP y -> f`
        gauche = evaluate(instructions, tokens[0], memo)
        droite = evaluate(instructions, tokens[2], memo)
        operateur = tokens[1]
        if operateur == "AND":
            valeur = gauche & droite
        elif operateur == "OR":
            valeur = gauche | droite
        elif operateur == "LSHIFT":
            valeur = (gauche << droite) & MASQUE
        elif operateur == "RSHIFT":
            valeur = gauche >> droite
        else:
            raise ValueError(f"opérateur inconnu : {operateur}")
        valeur &= MASQUE

    memo[fil] = valeur
    return valeur


def solve(lines, fil="a"):
    instructions = parse_lines(lines)
    return evaluate(instructions, fil)


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()
