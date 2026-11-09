from collections import defaultdict
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


def solve(lines, total_time=2503):
    """Points du renne en tête au fil des secondes."""
    reindeers = parse_input(lines)

    distances = defaultdict(int)  # distance actuelle de chaque renne
    timers = {}                   # temps restant dans l'état actuel (vol/repos)
    flying = {}                   # état actuel
    points = defaultdict(int)     # points cumulés

    # Initialisation
    for name, speed, fly_time, rest_time in reindeers:
        distances[name] = 0
        flying[name] = True
        timers[name] = fly_time
        points[name] = 0

    # Simulation seconde par seconde
    for _ in range(1, total_time + 1):
        for name, speed, fly_time, rest_time in reindeers:
            if flying[name]:
                distances[name] += speed
            timers[name] -= 1
            if timers[name] == 0:
                flying[name] = not flying[name]
                timers[name] = fly_time if flying[name] else rest_time

        # Donner un point aux rennes en tête
        max_dist = max(distances.values())
        for name in distances:
            if distances[name] == max_dist:
                points[name] += 1

    winner = max(points, key=points.get)
    return f"{winner} wins with {points[winner]} points"


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()
