from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day20.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def house_presents_part2(target):
    limit = target // 11  # estimation supérieure
    houses = [0] * (limit + 1)

    for elf in range(1, limit + 1):
        count = 0
        for house in range(elf, limit + 1, elf):
            houses[house] += elf * 11
            count += 1
            if count == 50:  # chaque elfe s'arrête après 50 maisons
                break

    for i, total in enumerate(houses):
        if total >= target:
            return i


def solve(lines):
    """Plus petit numéro de maison recevant au moins la cible de cadeaux."""
    target = int("".join(lines).strip())
    return f"Lowest house number with at least {target} presents is: {house_presents_part2(target)}"


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()
