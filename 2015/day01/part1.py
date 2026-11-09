from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day01.txt"


def solve(data):
    floor = 0
    for ch in data:
        if ch == '(':
            floor += 1
        elif ch == ')':
            floor -= 1
    return floor


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT
    with open(path, "r", encoding="utf-8") as f:
        data = f.read().strip()

    result = solve(data)
    print(result)


if __name__ == "__main__":
    main()
