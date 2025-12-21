import sys
from functools import lru_cache


def max_joltage(bank):
    """Find the maximum joltage by selecting exactly 12 batteries."""
    bank = bank.strip()
    n = len(bank)

    if n < 12:
        return 0

    # Use dynamic programming / memoization
    # State: (position, batteries_selected)
    # Choose greedily: at each position, decide whether to include this digit

    @lru_cache(maxsize=None)
    def best(pos, remaining):
        """Return the best digits string selecting 'remaining' batteries from pos onwards."""
        if remaining == 0:
            return ""
        if pos >= n:
            return None  # Can't select enough
        if n - pos < remaining:
            return None  # Not enough batteries left

        # Option 1: Take this battery
        take = best(pos + 1, remaining - 1)
        if take is not None:
            take = bank[pos] + take

        # Option 2: Skip this battery
        skip = best(pos + 1, remaining)

        # Choose the larger result
        if take is None:
            return skip
        if skip is None:
            return take

        # Compare as numbers (same length, so string comparison works)
        return take if take >= skip else skip

    result = best(0, 12)
    return int(result) if result else 0


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
