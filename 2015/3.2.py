import sys


def solve(data):
    # Santa and Robo-Santa positions
    positions = [[0, 0], [0, 0]]
    visited = {(0, 0)}

    for i, ch in enumerate(data):
        who = i % 2  # 0 = Santa, 1 = Robo-Santa

        if ch == '^':
            positions[who][1] += 1
        elif ch == 'v':
            positions[who][1] -= 1
        elif ch == '>':
            positions[who][0] += 1
        elif ch == '<':
            positions[who][0] -= 1

        visited.add(tuple(positions[who]))

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
