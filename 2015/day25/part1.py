from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day25.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def code_at(row, col):
    n = (row + col - 2) * (row + col - 1) // 2 + col
    code = 20151125
    for _ in range(1, n):
        code = (code * 252533) % 33554393
    return code


def parse_input(text):
    """Extrait (ligne, colonne) de la consigne du puzzle."""
    row, col = re.findall(r"row (\d+), column (\d+)", text)[0]
    return int(row), int(col)


def solve(lines):
    """Code de la grille à la position indiquée par l'énoncé."""
    row, col = parse_input(" ".join(lines))
    return f"Code à la position: {code_at(row, col)}"


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()
