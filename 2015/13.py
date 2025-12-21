import sys
import re
from itertools import permutations

def parse_input(lines):
    happiness = {}
    people = set()
    pattern = re.compile(r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.")
    
    for line in lines:
        match = pattern.match(line.strip())
        if not match:
            continue
        person1, gain_or_lose, units, person2 = match.groups()
        units = int(units) if gain_or_lose == "gain" else -int(units)
        happiness[(person1, person2)] = units
        people.add(person1)
        people.add(person2)
    return happiness, people

def total_happiness(order, happiness):
    total = 0
    n = len(order)
    for i in range(n):
        left = order[i]
        right = order[(i + 1) % n]  # table circulaire
        total += happiness[(left, right)]
        total += happiness[(right, left)]
    return total

def find_best_happiness(people, happiness):
    people = list(people)
    first = people[0]
    best = None
    for perm in permutations(people[1:]):
        seating = [first] + list(perm)
        score = total_happiness(seating, happiness)
        if best is None or score > best:
            best = score
    return best

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()
    
    happiness, people = parse_input(lines)
    best_score = find_best_happiness(people, happiness)
    print(best_score)

if __name__ == "__main__":
    main()
