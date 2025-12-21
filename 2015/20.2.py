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

target = 33100000
print("Lowest house number with at least", target, "presents is:", house_presents_part2(target))
