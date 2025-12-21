import sys
import re

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

def main():
    total_time = 2503

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()

    reindeers = parse_input(lines)

    best_distance = 0
    best_name = None
    for name, speed, fly_time, rest_time in reindeers:
        dist = distance_after_time(speed, fly_time, rest_time, total_time)
        if dist > best_distance:
            best_distance = dist
            best_name = name

    print(f"{best_name} wins with {best_distance} km")

if __name__ == "__main__":
    main()
