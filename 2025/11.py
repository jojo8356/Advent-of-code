import sys
from collections import defaultdict
from functools import lru_cache


def solve(lines):
    # Parse the graph
    graph = defaultdict(list)

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = line.split(': ')
        device = parts[0]
        outputs = parts[1].split() if len(parts) > 1 else []
        graph[device] = outputs

    # Count all paths from 'you' to 'out' using memoization
    @lru_cache(maxsize=None)
    def count_paths(node):
        if node == 'out':
            return 1

        total = 0
        for next_node in graph[node]:
            total += count_paths(next_node)

        return total

    return count_paths('you')


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()

    result = solve(lines)
    print(result)


if __name__ == "__main__":
    main()
