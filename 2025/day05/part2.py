from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day05.txt"


def solve(lines):
    # Parse input: only ranges (before blank line)
    ranges = []

    for line in lines:
        line = line.strip()
        if not line:
            break
        start, end = map(int, line.split('-'))
        ranges.append((start, end))

    # Merge overlapping ranges to count unique IDs
    if not ranges:
        return 0

    # Sort by start
    ranges.sort()

    # Merge overlapping ranges
    merged = [ranges[0]]
    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            # Overlapping or adjacent, merge
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    # Count total IDs
    total = 0
    for start, end in merged:
        total += end - start + 1

    return total


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    result = solve(lines)
    print(result)


if __name__ == "__main__":
    main()
