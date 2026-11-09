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


def find_min_combinations(containers, target):
    n = len(containers)
    # Stocke les combinaisons valides par taille
    valid_combos = {}
    
    for r in range(1, n+1):
        for combo in combinations(containers, r):
            if sum(combo) == target:
                if r not in valid_combos:
                    valid_combos[r] = []
                valid_combos[r].append(combo)
    
    if not valid_combos:
        return 0, []
    
    min_containers = min(valid_combos.keys())
    return min_containers, valid_combos[min_containers]


def solve(lines, target=150):
    """Combinaisons de containers totalisant target litres d'œufnog."""
    containers = [int(line) for line in lines if line.strip()]
    min_count, combos = find_min_combinations(containers, target)
    return f"Minimum containers needed: {min_count}\nNumber of ways using minimum containers: {len(combos)}"


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()
