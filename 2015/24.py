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

target_weight = sum(packages) // 3

# On stocke les QE valides
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

print("Quantum entanglement minimale:", min(valid_qe))
