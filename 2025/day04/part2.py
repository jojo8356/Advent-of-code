from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day04.txt"


def count_adjacent(grid, r, c, rows, cols):
    adjacent = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == '@':
                    adjacent += 1
    return adjacent


def solve(lines):
    grid = [list(line.rstrip('\n')) for line in lines if line.strip()]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    total_removed = 0

    while True:
        # Find all accessible rolls (fewer than 4 adjacent)
        to_remove = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '@':
                    continue
                if count_adjacent(grid, r, c, rows, cols) < 4:
                    to_remove.append((r, c))

        if not to_remove:
            break

        # Remove all accessible rolls
        for r, c in to_remove:
            grid[r][c] = '.'

        total_removed += len(to_remove)

    return total_removed


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    result = solve(lines)
    print(result)


if __name__ == "__main__":
    main()
