import sys


def solve(lines):
    total = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        dims = sorted(map(int, line.split('x')))
        # Smallest perimeter: 2 * (smallest + second smallest)
        ribbon_wrap = 2 * (dims[0] + dims[1])
        # Bow: volume
        ribbon_bow = dims[0] * dims[1] * dims[2]
        total += ribbon_wrap + ribbon_bow
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
