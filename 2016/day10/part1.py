"""2016, jour 10 : Balance Bots — partie 1.

Les instructions sont de deux formes :

  - `value V goes to bot B`                    : donne la puce V au bot B ;
  - `bot B gives low to bot X and high to bot Y` : quand le bot B tient deux
    puces, il donne la plus petite à X et la plus grande à Y (X et Y peuvent
    être des `output N`).

Réponse : numéro du bot qui compare les puces **17** et **61**.
"""

from collections import defaultdict, deque
from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day10.txt"

LIGNE_VALEUR = re.compile(r"value (\d+) goes to bot (\d+)")
LIGNE_RECETTE = re.compile(
    r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)"
)


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def analyser(lines):
    """Sépare les valeurs initiales et les règles des bots."""
    valeurs = []          # (valeur, bot)
    recettes = {}         # bot -> (type_bas, n_bas, type_haut, n_haut)
    for ligne in lines:
        ligne = ligne.strip()
        if not ligne:
            continue
        trouve = LIGNE_VALEUR.match(ligne)
        if trouve:
            valeurs.append((int(trouve.group(1)), int(trouve.group(2))))
            continue
        trouve = LIGNE_RECETTE.match(ligne)
        if trouve:
            recettes[int(trouve.group(1))] = (
                trouve.group(2), int(trouve.group(3)),
                trouve.group(4), int(trouve.group(5)),
            )
    return valeurs, recettes


def executer(valeurs, recettes):
    """Fait tourner la machine et renvoie (bots finaux, outputs, comparaisons)."""
    bots = defaultdict(list)
    outputs = {}
    comparaisons = {}     # bot -> (paire triée) au moment où il a comparé

    file = deque()
    for valeur, bot in valeurs:
        bots[bot].append(valeur)
        if len(bots[bot]) == 2:
            file.append(bot)

    while file:
        bot = file.popleft()
        if len(bots[bot]) != 2 or bot not in recettes:
            continue
        bas, haut = sorted(bots[bot])
        comparaisons[bot] = (bas, haut)

        type_bas, n_bas, type_haut, n_haut = recettes[bot]

        if type_bas == "bot":
            bots[n_bas].append(bas)
            if len(bots[n_bas]) == 2:
                file.append(n_bas)
        else:
            outputs[n_bas] = bas

        if type_haut == "bot":
            bots[n_haut].append(haut)
            if len(bots[n_haut]) == 2:
                file.append(n_haut)
        else:
            outputs[n_haut] = haut

    return bots, outputs, comparaisons


def solve(lines, paire=(17, 61)):
    """Numéro du bot qui compare la paire demandée."""
    valeurs, recettes = analyser(lines)
    _, _, comparaisons = executer(valeurs, recettes)
    for bot, comparee in comparaisons.items():
        if comparee == paire:
            return bot
    return "aucun bot ne compare cette paire"


def main():
    print("Bot comparant 17 et 61:", solve(read_lines()))


if __name__ == "__main__":
    main()
