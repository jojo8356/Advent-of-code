import sys


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
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()

    result = solve(lines)
    print(result)


if __name__ == "__main__":
    main()
