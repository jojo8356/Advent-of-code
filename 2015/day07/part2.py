"""Jour 7, partie 2 : on réinjecte la valeur du fil `a` sur le fil `b`.

On calcule d'abord `a` comme en partie 1, puis on remplace l'instruction qui
alimente `b` par cette valeur constante, et on relit `a`.
"""

from pathlib import Path
import sys

from part1 import evaluate, parse_lines

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day07.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def solve(lines):
    instructions = parse_lines(lines)

    # 1) valeur initiale du fil a
    valeur_a = evaluate(instructions, "a")

    # 2) on force b = valeur_a, puis on relit a
    instructions["b"] = [str(valeur_a)]
    return evaluate(instructions, "a")


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()
