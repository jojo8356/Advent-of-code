import sys


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
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            data = f.read().strip()
    else:
        data = sys.stdin.read().strip()

    result = solve(data)
    print(result)


if __name__ == "__main__":
    main()
