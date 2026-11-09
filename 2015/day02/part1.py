from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day02.txt"


def solve(lines):
    total = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        l, w, h = map(int, line.split('x'))
        sides = [l*w, w*h, h*l]
        surface = 2 * sum(sides)
        slack = min(sides)
        total += surface + slack
    return total


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    result = solve(lines)
    print(result)


if __name__ == "__main__":
    main()
