from copy import deepcopy

# Boss stats (input)
boss_hitpoints = 58  # remplacer par ton input
boss_damage = 9  # remplacer par ton input

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

# État initial
initial_state = {
    "player_hp": player_hitpoints,
    "player_mana": player_mana,
    "player_armor": 0,
    "boss_hp": boss_hitpoints,
    "effects": {}  # effets actifs
}

dfs(initial_state, 0)
print("Minimum mana to win:", min_mana)
