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

    # Find largest rectangle using any two red tiles as opposite corners
    max_area = 0

    for (x1, y1), (x2, y2) in combinations(tiles, 2):
        # Rectangle area = |x2 - x1| * |y2 - y1|
        # But we need to include the edges, so it's (|x2-x1| + 1) * (|y2-y1| + 1)
        # Wait, looking at the example: 2,5 to 9,7 has area 24
        # width = 9 - 2 = 7, but with inclusion it would be 8
        # height = 7 - 5 = 2, but with inclusion it would be 3
        # 8 * 3 = 24 ✓

        width = abs(x2 - x1) + 1
        height = abs(y2 - y1) + 1
        area = width * height
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
