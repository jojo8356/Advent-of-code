from itertools import combinations
from math import prod

# Liste des poids (exemple, remplace par ton input)
packages = """1
2
3
7
11
13
17
19
23
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113""".split("\n")
packages = [int(x) for x in packages]

target_weight = sum(packages) // 4

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

print("Quantum entanglement minimale pour 4 groupes:", min(valid_qe))