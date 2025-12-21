import sys


def max_joltage(bank):
    """Find the maximum joltage by selecting exactly 2 batteries."""
    bank = bank.strip()
    if len(bank) < 2:
        return 0

    max_val = 0
    # Try all pairs of positions (i, j) where i < j
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            # Form the two-digit number from digits at positions i and j
            joltage = int(bank[i] + bank[j])
            max_val = max(max_val, joltage)

    return max_val


def solve(lines):
    total = 0
    for line in lines:
        line = line.strip()
        if line:
            total += max_joltage(line)
    return total


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
