import sys
import re
from collections import defaultdict

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

def main():
    total_time = 2503

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()

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
    for t in range(1, total_time + 1):
        for name, speed, fly_time, rest_time in reindeers:
            if flying[name]:
                distances[name] += speed
            timers[name] -= 1
            if timers[name] == 0:
                flying[name] = not flying[name]
                timers[name] = fly_time if flying[name] else rest_time

        # Trouver la distance max
        max_dist = max(distances.values())

        # Donner un point aux rennes en tête
        for name in distances:
            if distances[name] == max_dist:
                points[name] += 1

    # Résultat
    winner = max(points, key=points.get)
    print(f"{winner} wins with {points[winner]} points")

if __name__ == "__main__":
    main()
