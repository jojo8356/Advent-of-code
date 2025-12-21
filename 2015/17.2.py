import sys
from itertools import combinations

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

def main():
    target = 150  # litres d’œufnog
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            containers = [int(line.strip()) for line in f.readlines()]
    else:
        containers = [int(line.strip()) for line in sys.stdin.readlines()]

    min_count, combos = find_min_combinations(containers, target)
    print(f"Minimum containers needed: {min_count}")
    print(f"Number of ways using minimum containers: {len(combos)}")

if __name__ == "__main__":
    main()
