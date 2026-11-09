from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day02.txt"


def is_invalid(n):
    """Check if n is made of a sequence of digits repeated twice."""
    s = str(n)
    length = len(s)
    # Must have even length to be repeated twice
    if length % 2 != 0:
        return False
    half = length // 2
    return s[:half] == s[half:]


def find_invalid_in_range(start, end):
    """Find all invalid IDs in the range [start, end]."""
    invalid_ids = []

    # Instead of iterating all numbers, generate candidates
    # An invalid ID has form XX where X is repeated
    # So we need to find all XX where start <= XX <= end

    # Determine the range of half-lengths to check
    max_half_len = len(str(end)) // 2 + 1

    for half_len in range(1, max_half_len + 1):
        # Generate all numbers of this half-length
        min_half = 10 ** (half_len - 1) if half_len > 1 else 1
        max_half = 10 ** half_len - 1

        for half in range(min_half, max_half + 1):
            # Create the doubled number
            s = str(half)
            candidate = int(s + s)

            if start <= candidate <= end:
                invalid_ids.append(candidate)

    return invalid_ids


def solve(line):
    line = line.strip().rstrip(',')
    if not line:
        return 0

    ranges = line.split(',')
    total = 0

    for r in ranges:
        r = r.strip()
        if not r:
            continue
        start, end = map(int, r.split('-'))
        invalid_ids = find_invalid_in_range(start, end)
        total += sum(invalid_ids)

    return total


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT
    with open(path, "r", encoding="utf-8") as f:
        line = f.read()

    result = solve(line)
    print(result)

if __name__ == "__main__":
    main()
