import sys
from itertools import combinations


def solve(lines):
    # Parse red tile positions
    tiles = []
    for line in lines:
        line = line.strip()
        if line:
            x, y = map(int, line.split(','))
            tiles.append((x, y))

    if len(tiles) < 2:
        return 0

    # Build set of all colored tiles (red and green)
    colored = set(tiles)

    # Add green tiles: lines between consecutive red tiles (including wrap)
    for i in range(len(tiles)):
        x1, y1 = tiles[i]
        x2, y2 = tiles[(i + 1) % len(tiles)]

        # They share either x or y coordinate
        if x1 == x2:
            # Vertical line
            for y in range(min(y1, y2), max(y1, y2) + 1):
                colored.add((x1, y))
        else:
            # Horizontal line
            for x in range(min(x1, x2), max(x1, x2) + 1):
                colored.add((x, y1))

    # Now fill the interior of the loop
    # Find bounding box
    min_x = min(x for x, y in colored)
    max_x = max(x for x, y in colored)
    min_y = min(y for x, y in colored)
    max_y = max(y for x, y in colored)

    # Use ray casting to find interior points
    # A point is inside if crossing the boundary an odd number of times
    # But since we have a polygon made of horizontal/vertical segments,
    # we can use flood fill from outside

    # Create a grid slightly larger than bounding box
    # Flood fill from outside to find all exterior points
    exterior = set()
    to_visit = [(min_x - 1, min_y - 1)]
    visited = set()

    while to_visit:
        x, y = to_visit.pop()
        if (x, y) in visited:
            continue
        if x < min_x - 1 or x > max_x + 1 or y < min_y - 1 or y > max_y + 1:
            continue
        if (x, y) in colored:
            continue

        visited.add((x, y))
        exterior.add((x, y))

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            to_visit.append((x + dx, y + dy))

    # Interior points are those not exterior and not on boundary
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) not in exterior and (x, y) not in colored:
                colored.add((x, y))

    # Now find largest rectangle with red corners where all tiles are colored
    max_area = 0

    for i, j in combinations(range(len(tiles)), 2):
        x1, y1 = tiles[i]
        x2, y2 = tiles[j]

        # Check if all tiles in rectangle are colored
        rx_min, rx_max = min(x1, x2), max(x1, x2)
        ry_min, ry_max = min(y1, y2), max(y1, y2)

        all_colored = True
        for x in range(rx_min, rx_max + 1):
            for y in range(ry_min, ry_max + 1):
                if (x, y) not in colored:
                    all_colored = False
                    break
            if not all_colored:
                break

        if all_colored:
            area = (rx_max - rx_min + 1) * (ry_max - ry_min + 1)
            max_area = max(max_area, area)

    return max_area


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
