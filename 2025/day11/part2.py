from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day11.txt"


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

    # Count paths from 'svr' to 'out' that visit both 'dac' and 'fft'
    # State: (current_node, visited_dac, visited_fft)
    @lru_cache(maxsize=None)
    def count_paths(node, has_dac, has_fft):
        # Update flags if we're at dac or fft
        if node == 'dac':
            has_dac = True
        if node == 'fft':
            has_fft = True

        if node == 'out':
            # Only count if we visited both
            return 1 if (has_dac and has_fft) else 0

        total = 0
        for next_node in graph[node]:
            total += count_paths(next_node, has_dac, has_fft)

        return total

    return count_paths('svr', False, False)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    result = solve(lines)
    print(result)

if __name__ == "__main__":
    main()
