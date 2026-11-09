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
            # Moving left (decreasing)
            new_position = (position - distance) % 100

            # Going left from position by distance
            # We hit 0 when we've moved exactly 'position' steps (landing on 0)
            # Then every 100 steps after that
            # position=50, distance=68: after 50 steps we're at 0 -> count 1
            # position=82, distance=30: 82-30=52, never hits 0
            if position == 0:
                # Starting at 0, we hit 0 again after 100 steps
                count_zero += distance // 100
            elif distance >= position:
                # We reach 0 after 'position' steps
                remaining = distance - position
                count_zero += 1 + (remaining // 100)
        else:  # R
            # Moving right (increasing)
            new_position = (position + distance) % 100

            # Going right from position by distance
            # We hit 0 when we've moved (100 - position) steps
            if position == 0:
                count_zero += distance // 100
            else:
                distance_to_zero = 100 - position
                if distance >= distance_to_zero:
                    remaining = distance - distance_to_zero
                    count_zero += 1 + (remaining // 100)

        position = new_position

    return count_zero


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    result = solve(lines)
    print(result)

if __name__ == "__main__":
    main()
