from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day07.txt"


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

    # Track active beams (set of columns with beams at current row)
    # Use a set to handle beams merging into same position
    beams = {start_col}
    split_count = 0

    # Process each row starting from row 1 (below S)
    for r in range(1, rows):
        new_beams = set()

        for col in beams:
            if col < 0 or col >= cols:
                continue

            ch = grid[r][col]

            if ch == '^':
                # Splitter: beam stops, two new beams emit left and right
                split_count += 1
                if col - 1 >= 0:
                    new_beams.add(col - 1)
                if col + 1 < cols:
                    new_beams.add(col + 1)
            else:
                # Empty space or other: beam continues downward
                new_beams.add(col)

        beams = new_beams

        if not beams:
            break

    return split_count


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    result = solve(lines)
    print(result)


if __name__ == "__main__":
    main()
