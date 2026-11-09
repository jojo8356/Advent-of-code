from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day03.txt"


def solve(data):
    x, y = 0, 0
    visited = {(0, 0)}

    for ch in data:
        if ch == '^':
            y += 1
        elif ch == 'v':
            y -= 1
        elif ch == '>':
            x += 1
        elif ch == '<':
            x -= 1
        visited.add((x, y))

    return len(visited)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT
    with open(path, "r", encoding="utf-8") as f:
        data = f.read().strip()

    result = solve(data)
    print(result)


if __name__ == "__main__":
    main()
