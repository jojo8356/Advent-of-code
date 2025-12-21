import math

def house_presents(target):
    # On fait une estimation supérieure raisonnable
    limit = target // 10
    houses = [0] * (limit+1)

    for elf in range(1, limit+1):
        for house in range(elf, limit+1, elf):
            houses[house] += elf * 10

    for i, total in enumerate(houses):
        if total >= target:
            return i

target = 33100000
print("Lowest house number with at least", target, "presents is:", house_presents(target))
