from itertools import combinations
from math import prod
from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day24.txt"

def solve(target_weight, packages):
    valid_qe = []

    # On parcourt toutes les tailles possibles du premier groupe, en commençant par le plus petit
    for group_size in range(1, len(packages)):
        found = False
        for group in combinations(packages, group_size):
            if sum(group) == target_weight:
                remaining = packages.copy()
                for p in group:
                    remaining.remove(p)
                # On doit vérifier si remaining peut être divisé en 2 groupes de target_weight
                # Ici, on teste naïvement si une combinaison existe
                possible = False
                for second_size in range(1, len(remaining)):
                    for second_group in combinations(remaining, second_size):
                        if sum(second_group) == target_weight:
                            possible = True
                            break
                    if possible:
                        break
                if possible:
                    valid_qe.append(prod(group))
                    found = True
        if found:
            break  # on ne veut que le nombre minimal de paquets dans le premier groupe
    return min(valid_qe)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT
    with open(path, "r", encoding="utf-8") as f:
        packages = [int(x) for x in f.read().split()]
    target_weight = sum(packages) // 3
    print("Quantum entanglement minimale:", solve(target_weight, packages))


if __name__ == "__main__":
    main()
