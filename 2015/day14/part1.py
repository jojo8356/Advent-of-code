from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day14.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def parse_input(lines):
    pattern = re.compile(
        r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\."
    )
    reindeers = []
    for line in lines:
        m = pattern.match(line.strip())
        if m:
            name = m.group(1)
            speed = int(m.group(2))
            fly_time = int(m.group(3))
            rest_time = int(m.group(4))
            reindeers.append((name, speed, fly_time, rest_time))
    return reindeers


def distance_after_time(speed, fly_time, rest_time, total_time):
    cycle_time = fly_time + rest_time
    full_cycles = total_time // cycle_time
    remaining_time = total_time % cycle_time
    flying_seconds = full_cycles * fly_time + min(fly_time, remaining_time)
    return flying_seconds * speed


def solve(lines, total_time=2503):
    """Distance du renne en tête après total_time secondes."""
    reindeers = parse_input(lines)

    best_distance = 0
    best_name = None
    for name, speed, fly_time, rest_time in reindeers:
        dist = distance_after_time(speed, fly_time, rest_time, total_time)
        if dist > best_distance:
            best_distance = dist
            best_name = name

    return f"{best_name} wins with {best_distance} km"


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()
