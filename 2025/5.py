import sys


def solve(lines):
    # Parse input: ranges, then blank line, then ingredient IDs
    ranges = []
    ingredients = []
    parsing_ranges = True

    for line in lines:
        line = line.strip()
        if not line:
            parsing_ranges = False
            continue

        if parsing_ranges:
            start, end = map(int, line.split('-'))
            ranges.append((start, end))
        else:
            ingredients.append(int(line))

    # Count fresh ingredients
    fresh_count = 0
    for ing in ingredients:
        for start, end in ranges:
            if start <= ing <= end:
                fresh_count += 1
                break

    return fresh_count


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
