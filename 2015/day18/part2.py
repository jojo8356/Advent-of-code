from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day18.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def parse_input(lines):
    return [[c == '#' for c in line.strip()] for line in lines]


def count_on_neighbors(grid, x, y):
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny]:
                count += 1
    return count


def step(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [[False]*cols for _ in range(rows)]
    for x in range(rows):
        for y in range(cols):
            # Les coins restent toujours allumés
            if (x, y) in [(0,0), (0,cols-1), (rows-1,0), (rows-1,cols-1)]:
                new_grid[x][y] = True
                continue

            on_neighbors = count_on_neighbors(grid, x, y)
            if grid[x][y]:
                new_grid[x][y] = on_neighbors in (2, 3)
            else:
                new_grid[x][y] = on_neighbors == 3
    return new_grid


def solve(lines, steps=100, stuck_corners=True):
    """Nombre de lumières allumées après `steps` générations."""
    grid = parse_input(lines)

    if stuck_corners:
        rows = len(grid)
        cols = len(grid[0])
        for x, y in [(0, 0), (0, cols - 1), (rows - 1, 0), (rows - 1, cols - 1)]:
            grid[x][y] = True

    for _ in range(steps):
        grid = step(grid)

    return sum(sum(1 for cell in row if cell) for row in grid)


def main():
    print("Lights on after 100 steps with stuck corners:", solve(read_lines()))


if __name__ == "__main__":
    main()
