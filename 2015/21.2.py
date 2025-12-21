from itertools import combinations

# Items in the shop
weapons = [
    {"name": "Dagger", "cost": 8, "damage": 4, "armor": 0},
    {"name": "Shortsword", "cost": 10, "damage": 5, "armor": 0},
    {"name": "Warhammer", "cost": 25, "damage": 6, "armor": 0},
    {"name": "Longsword", "cost": 40, "damage": 7, "armor": 0},
    {"name": "Greataxe", "cost": 74, "damage": 8, "armor": 0}
]

armors = [
    {"name": "None", "cost": 0, "damage": 0, "armor": 0},  # optional armor
    {"name": "Leather", "cost": 13, "damage": 0, "armor": 1},
    {"name": "Chainmail", "cost": 31, "damage": 0, "armor": 2},
    {"name": "Splintmail", "cost": 53, "damage": 0, "armor": 3},
    {"name": "Bandedmail", "cost": 75, "damage": 0, "armor": 4},
    {"name": "Platemail", "cost": 102, "damage": 0, "armor": 5}
]

rings = [
    {"name": "Damage +1", "cost": 25, "damage": 1, "armor": 0},
    {"name": "Damage +2", "cost": 50, "damage": 2, "armor": 0},
    {"name": "Damage +3", "cost": 100, "damage": 3, "armor": 0},
    {"name": "Defense +1", "cost": 20, "damage": 0, "armor": 1},
    {"name": "Defense +2", "cost": 40, "damage": 0, "armor": 2},
    {"name": "Defense +3", "cost": 80, "damage": 0, "armor": 3}
]

# Boss stats (input)
boss_hitpoints = 103
boss_damage = 9
boss_armor = 2

def simulate_fight(player_hp, player_damage, player_armor):
    boss_hp = boss_hitpoints
    # Damage per turn (at least 1)
    player_attack = max(1, player_damage - boss_armor)
    boss_attack = max(1, boss_damage - player_armor)
    
    # Player goes first
    while True:
        boss_hp -= player_attack
        if boss_hp <= 0:
            return True  # player wins
        player_hp -= boss_attack
        if player_hp <= 0:
            return False  # boss wins

max_cost = 0

# Generate all valid equipment combinations
ring_combos = list(combinations(rings, 2)) + list(combinations(rings, 1)) + [()]

for w in weapons:
    for a in armors:
        for r in ring_combos:
            items = [w, a] + list(r)
            total_cost = sum(item["cost"] for item in items)
            total_damage = sum(item["damage"] for item in items)
            total_armor = sum(item["armor"] for item in items)
            
            if not simulate_fight(100, total_damage, total_armor):
                if total_cost > max_cost:
                    max_cost = total_cost

print("Maximum gold to still lose:", max_cost)
