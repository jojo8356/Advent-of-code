import sys


def solve(lines):
    grid = [line.rstrip('\n') for line in lines if line.strip()]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            # Count adjacent rolls of paper
            adjacent = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '@':
                            adjacent += 1

            # Accessible if fewer than 4 adjacent rolls
            if adjacent < 4:
                count += 1

    return count


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
