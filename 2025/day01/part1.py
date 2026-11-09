from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day01.txt"


def solve(lines):
    position = 50
    count_zero = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        distance = int(line[1:])

        if direction == 'L':
            position = (position - distance) % 100
        else:  # R
            position = (position + distance) % 100

        if position == 0:
            count_zero += 1

    return count_zero


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    result = solve(lines)
    print(result)

if __name__ == "__main__":
    main()
