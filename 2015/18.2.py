import sys

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

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()

    grid = parse_input(lines)

    # Allumer les coins au départ
    rows = len(grid)
    cols = len(grid[0])
    for x, y in [(0,0), (0,cols-1), (rows-1,0), (rows-1,cols-1)]:
        grid[x][y] = True

    for _ in range(100):
        grid = step(grid)

    total_on = sum(sum(1 for cell in row if cell) for row in grid)
    print(f"Lights on after 100 steps with stuck corners: {total_on}")

if __name__ == "__main__":
    main()
