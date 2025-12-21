import sys


def parse_shape(lines):
    """Parse a shape from lines, return list of (row, col) offsets."""
    cells = []
    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if ch == '#':
                cells.append((r, c))
    return cells


def solve(lines):
    # Parse input
    shapes = {}
    regions = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if not line:
            i += 1
            continue

        # Shape definition: "N:"
        if line.endswith(':') and line[:-1].isdigit():
            shape_idx = int(line[:-1])
            i += 1
            shape_lines = []
            while i < len(lines) and lines[i].strip() and not lines[i].strip().endswith(':') and 'x' not in lines[i]:
                shape_lines.append(lines[i].rstrip('\n'))
                i += 1
            shape = parse_shape(shape_lines)
            shapes[shape_idx] = len(shape)  # Just store the size

        # Region definition: "WxH: counts..."
        elif 'x' in line:
            parts = line.split(': ')
            dims = parts[0].split('x')
            width, height = int(dims[0]), int(dims[1])
            counts = list(map(int, parts[1].split()))
            regions.append((width, height, counts))
            i += 1
        else:
            i += 1

    # Check each region: can it fit all presents?
    # It fits if total cells of presents <= area of region
    fit_count = 0
    for width, height, counts in regions:
        area = width * height
        total_cells = sum(count * shapes[idx] for idx, count in enumerate(counts))

        if total_cells <= area:
            fit_count += 1

    return fit_count


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
