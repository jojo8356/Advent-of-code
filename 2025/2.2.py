import sys


def is_invalid(n):
    """Check if n is made of a sequence of digits repeated at least twice."""
    s = str(n)
    length = len(s)

    # Try all possible pattern lengths that divide the total length
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            repetitions = length // pattern_len
            if repetitions >= 2 and pattern * repetitions == s:
                return True
    return False


def find_invalid_in_range(start, end):
    """Find all invalid IDs in the range [start, end]."""
    invalid_ids = set()

    # Generate candidates by creating repeated patterns
    # For each pattern length and repetition count, generate all patterns
    max_digits = len(str(end))

    for pattern_len in range(1, max_digits + 1):
        min_pattern = 10 ** (pattern_len - 1) if pattern_len > 1 else 1
        max_pattern = 10 ** pattern_len - 1

        for pattern in range(min_pattern, max_pattern + 1):
            pattern_str = str(pattern)

            # Try different repetition counts (at least 2)
            for reps in range(2, max_digits // pattern_len + 1):
                candidate = int(pattern_str * reps)

                if candidate > end:
                    break
                if candidate >= start:
                    invalid_ids.add(candidate)

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
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            line = f.read()
    else:
        line = sys.stdin.read()

    result = solve(line)
    print(result)


if __name__ == "__main__":
    main()
