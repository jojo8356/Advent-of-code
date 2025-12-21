import sys


def solve(data):
    floor = 0
    for i, ch in enumerate(data, 1):
        if ch == '(':
            floor += 1
        elif ch == ')':
            floor -= 1
        if floor == -1:
            return i
    return -1


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
