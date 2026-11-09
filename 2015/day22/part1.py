from copy import deepcopy
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
boss_hitpoints = 0
boss_damage = 0

# Player stats
player_hitpoints = 50
player_mana = 500

# Sorts
spells = {
    "Magic Missile": {"cost": 53, "damage": 4, "heal": 0, "timer": 0},
    "Drain": {"cost": 73, "damage": 2, "heal": 2, "timer": 0},
    "Shield": {"cost": 113, "damage": 0, "heal": 0, "timer": 6, "armor": 7},
    "Poison": {"cost": 173, "damage": 3, "heal": 0, "timer": 6},
    "Recharge": {"cost": 229, "damage": 0, "heal": 0, "timer": 5, "mana": 101},
}

# Minimum mana used to win
min_mana = float('inf')


def apply_effects(state):
    """Applique tous les effets actifs au début du tour"""
    state['player_armor'] = 0
    for effect in list(state['effects'].keys()):
        timer = state['effects'][effect]
        if effect == "Shield":
            state['player_armor'] = spells[effect]["armor"]
        if effect == "Poison":
            state['boss_hp'] -= spells[effect]["damage"]
        if effect == "Recharge":
            state['player_mana'] += spells[effect]["mana"]
        state['effects'][effect] -= 1
        if state['effects'][effect] == 0:
            del state['effects'][effect]


def dfs(state, mana_spent):
    global min_mana

    # Si le mana déjà dépensé dépasse le min, arrêter
    if mana_spent >= min_mana:
        return

    # Appliquer les effets
    apply_effects(state)

    # Si le boss est mort, mise à jour du min_mana
    if state['boss_hp'] <= 0:
        min_mana = min(min_mana, mana_spent)
        return

    # Joueur peut caster un sort
    for spell_name, spell in spells.items():
        # Vérifier si le sort peut être lancé
        if spell["cost"] > state['player_mana']:
            continue
        if spell_name in state['effects'] and spell["timer"] > 0:
            continue  # effet déjà actif

        # Nouvel état
        new_state = deepcopy(state)
        new_state['player_mana'] -= spell["cost"]
        new_mana_spent = mana_spent + spell["cost"]

        # Effets immédiats
        if spell_name in ["Magic Missile", "Drain"]:
            new_state['boss_hp'] -= spell["damage"]
            new_state['player_hp'] += spell["heal"]
        else:
            new_state['effects'][spell_name] = spell["timer"]

        # Vérifier si le boss est mort après le sort
        if new_state['boss_hp'] <= 0:
            min_mana = min(min_mana, new_mana_spent)
            continue

        # Tour du boss
        apply_effects(new_state)
        if new_state['boss_hp'] <= 0:
            min_mana = min(min_mana, new_mana_spent)
            continue

        # Boss attaque
        damage = max(1, boss_damage - new_state['player_armor'])
        new_state['player_hp'] -= damage

        if new_state['player_hp'] > 0:
            dfs(new_state, new_mana_spent)

def search_min_mana(boss_hp, boss_attack):
    """Cherche le mana minimal pour gagner contre ce boss."""
    global boss_hitpoints, boss_damage, min_mana

    boss_hitpoints = boss_hp
    boss_damage = boss_attack
    min_mana = float('inf')

    initial_state = {
        "player_hp": player_hitpoints,
        "player_mana": player_mana,
        "player_armor": 0,
        "boss_hp": boss_hitpoints,
        "effects": {}  # effets actifs
    }

    dfs(initial_state, 0)
    return min_mana


def solve(lines):
    """Mana minimal pour gagner, pour les statistiques de boss fournies."""
    boss = read_boss_stats(lines)
    return f"Minimum mana to win: {search_min_mana(boss['hit points'], boss['damage'])}"


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()

