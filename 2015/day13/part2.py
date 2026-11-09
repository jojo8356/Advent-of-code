from itertools import permutations
from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day13.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


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
        right = order[(i + 1) % n]
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


def solve(lines):
    """Meilleur arrangement possible de la table."""
    happiness, people = parse_input(lines)

    # Ajouter "Me" avec bonheur = 0 vers et depuis tout le monde
    for person in list(people):
        happiness[(person, "Me")] = 0
        happiness[("Me", person)] = 0
    people.add("Me")
    return find_best_happiness(people, happiness)


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()
