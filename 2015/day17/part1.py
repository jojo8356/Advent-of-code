from itertools import combinations
from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day17.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def count_combinations(containers, target):
    count = 0
    n = len(containers)
    for r in range(1, n+1):
        for combo in combinations(containers, r):
            if sum(combo) == target:
                count += 1
    return count


def solve(lines, target=150):
    """Combinaisons de containers totalisant target litres d'œufnog."""
    containers = [int(line) for line in lines if line.strip()]
    return f"Total number of combinations: {count_combinations(containers, target)}"


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()
