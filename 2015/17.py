import sys
from itertools import combinations

def count_combinations(containers, target):
    count = 0
    n = len(containers)
    for r in range(1, n+1):
        for combo in combinations(containers, r):
            if sum(combo) == target:
                count += 1
    return count

def main():
    target = 150  # litres d’œufnog
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            containers = [int(line.strip()) for line in f.readlines()]
    else:
        containers = [int(line.strip()) for line in sys.stdin.readlines()]

    total = count_combinations(containers, target)
    print(f"Total number of combinations: {total}")

if __name__ == "__main__":
    main()
