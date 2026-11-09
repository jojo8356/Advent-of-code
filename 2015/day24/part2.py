from itertools import combinations
from math import prod
from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day24.txt"

def solve(target_weight, packages):
    valid_qe = []

    # On parcourt les tailles de groupe du premier groupe (du plus petit au plus grand)
    for group_size in range(1, len(packages)):
        found = False
        for group in combinations(packages, group_size):
            if sum(group) == target_weight:
                remaining = packages.copy()
                for p in group:
                    remaining.remove(p)
                # On doit vérifier si remaining peut être divisé en 3 groupes de target_weight
                possible = False
                # On teste naïvement toutes les combinaisons pour le deuxième groupe
                for second_size in range(1, len(remaining)):
                    for second_group in combinations(remaining, second_size):
                        if sum(second_group) == target_weight:
                            remaining2 = remaining.copy()
                            for p in second_group:
                                remaining2.remove(p)
                            # Vérifie si remaining2 peut faire 2 groupes
                            third_possible = False
                            for third_size in range(1, len(remaining2)):
                                for third_group in combinations(remaining2, third_size):
                                    if sum(third_group) == target_weight:
                                        third_possible = True
                                        break
                                if third_possible:
                                    break
                            if third_possible:
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
    target_weight = sum(packages) // 4
    print("Quantum entanglement minimale pour 4 groupes:", solve(target_weight, packages))


if __name__ == "__main__":
    main()
