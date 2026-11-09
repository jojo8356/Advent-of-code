from itertools import combinations
from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day21.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def read_boss_stats(lines):
    """Lit les statistiques du boss depuis les lignes de l'entrée du puzzle."""
    stats = {}
    for line in lines:
        if ":" in line:
            name, value = line.split(":", 1)
            stats[name.strip().lower()] = int(value)
    return stats


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


def simulate_fight(boss, player_hp, player_damage, player_armor):
    boss_hp = boss["hit points"]
    # Damage per turn (at least 1)
    player_attack = max(1, player_damage - boss["armor"])
    boss_attack = max(1, boss["damage"] - player_armor)
    
    # Player goes first
    while True:
        boss_hp -= player_attack
        if boss_hp <= 0:
            return True  # player wins
        player_hp -= boss_attack
        if player_hp <= 0:
            return False  # boss wins


def min_cost_to_win(boss):
    min_cost = float('inf')

    # Generate all valid equipment combinations
    ring_combos = list(combinations(rings, 2)) + list(combinations(rings, 1)) + [()]

    for w in weapons:
        for a in armors:
            for r in ring_combos:
                items = [w, a] + list(r)
                total_cost = sum(item["cost"] for item in items)
                total_damage = sum(item["damage"] for item in items)
                total_armor = sum(item["armor"] for item in items)

                if simulate_fight(boss, 100, total_damage, total_armor):
                    if total_cost < min_cost:
                        min_cost = total_cost

    return min_cost
def solve(lines):
    """Résultat du jour 21 pour les statistiques de boss fournies."""
    boss = read_boss_stats(lines)
    return f"Minimum gold to win: {min_cost_to_win(boss)}"


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()
