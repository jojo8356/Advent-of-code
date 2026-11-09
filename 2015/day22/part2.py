from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day22.txt"


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


# Statistiques du boss, renseignées par main() depuis l'entrée du puzzle
boss_hp = 0
boss_damage = 0

# Spells
spells = {
    "Magic Missile": {"cost": 53, "damage": 4, "heal": 0, "effect": None, "duration": 0},
    "Drain": {"cost": 73, "damage": 2, "heal": 2, "effect": None, "duration": 0},
    "Shield": {"cost": 113, "damage": 0, "heal": 0, "effect": "Shield", "duration": 6},
    "Poison": {"cost": 173, "damage": 0, "heal": 0, "effect": "Poison", "duration": 6},
    "Recharge": {"cost": 229, "damage": 0, "heal": 0, "effect": "Recharge", "duration": 5}
}

min_mana = float('inf')


def dfs(player_hp, player_mana, boss_hp, effects, mana_spent):
    global min_mana

    # Hard Mode: lose 1 HP at start of player's turn
    player_hp -= 1
    if player_hp <= 0:
        return

    # Apply effects
    armor = 0
    new_effects = {}
    for eff, timer in effects.items():
        if eff == "Shield":
            armor = 7
        elif eff == "Poison":
            boss_hp -= 3
        elif eff == "Recharge":
            player_mana += 101
        if timer > 1:
            new_effects[eff] = timer - 1
    effects = new_effects

    # Check boss death
    if boss_hp <= 0:
        if mana_spent < min_mana:
            min_mana = mana_spent
        return

    # Try all spells
    for name, spell in spells.items():
        # Can't cast effect that's active
        if spell["effect"] and spell["effect"] in effects:
            continue
        if player_mana < spell["cost"]:
            continue

        # Prepare next state
        next_player_hp = player_hp + spell["heal"]
        next_player_mana = player_mana - spell["cost"]
        next_boss_hp = boss_hp - spell["damage"]
        next_effects = effects.copy()
        if spell["effect"]:
            next_effects[spell["effect"]] = spell["duration"]
        next_mana_spent = mana_spent + spell["cost"]

        # Check boss death after player's spell
        if next_boss_hp <= 0:
            if next_mana_spent < min_mana:
                min_mana = next_mana_spent
            continue

        # Boss turn: apply effects first
        boss_armor = 0
        new_effects_boss = {}
        for eff, timer in next_effects.items():
            if eff == "Shield":
                boss_armor = 7
            elif eff == "Poison":
                next_boss_hp -= 3
            elif eff == "Recharge":
                next_player_mana += 101
            if timer > 1:
                new_effects_boss[eff] = timer - 1
        next_effects = new_effects_boss

        if next_boss_hp <= 0:
            if next_mana_spent < min_mana:
                min_mana = next_mana_spent
            continue

        # Boss attacks
        damage = max(1, boss_damage - boss_armor)
        next_player_hp -= damage
        if next_player_hp <= 0:
            continue

        # Recurse
        dfs(next_player_hp, next_player_mana, next_boss_hp, next_effects, next_mana_spent)

def search_min_mana(boss_hit_points, boss_attack, player_hp=50, player_mana=500):
    """Cherche le mana minimal pour gagner en mode difficile."""
    global boss_hp, boss_damage, min_mana

    boss_hp = boss_hit_points
    boss_damage = boss_attack
    min_mana = float('inf')

    dfs(player_hp=player_hp, player_mana=player_mana, boss_hp=boss_hp, effects={}, mana_spent=0)
    return min_mana


def solve(lines):
    """Mana minimal pour gagner en mode difficile, pour ces statistiques de boss."""
    boss = read_boss_stats(lines)
    result = search_min_mana(boss["hit points"], boss["damage"])
    if result == float("inf"):
        return "Impossible to win in Hard Mode with these stats."
    return f"Minimum mana to win in Hard Mode: {result}"


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()

