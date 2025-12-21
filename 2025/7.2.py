import sys
from collections import defaultdict


def solve(lines):
    grid = [line.rstrip('\n') for line in lines if line.strip()]

    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    # Find starting position S
    start_col = None
    for c in range(cols):
        if grid[0][c] == 'S':
            start_col = c
            break

    if start_col is None:
        return 0

    # Track beams with their timeline counts
    # beams[col] = number of timelines with a particle at that column
    beams = defaultdict(int)
    beams[start_col] = 1

    # Process each row starting from row 1 (below S)
    for r in range(1, rows):
        new_beams = defaultdict(int)

        for col, count in beams.items():
            if col < 0 or col >= cols:
                continue

            ch = grid[r][col]

            if ch == '^':
                # Splitter: particle goes both left and right
                # Each timeline splits into two timelines
                if col - 1 >= 0:
                    new_beams[col - 1] += count
                if col + 1 < cols:
                    new_beams[col + 1] += count
            else:
                # Empty space: particle continues downward
                new_beams[col] += count

        beams = new_beams

        if not beams:
            break

    # Total timelines is the sum of all timeline counts
    return sum(beams.values())


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
