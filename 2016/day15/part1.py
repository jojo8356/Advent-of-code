"""2016, jour 15 : Timing is Everything — partie 1.

Le disque i (1-indexé) a `positions` cases et se trouve en `depart` à t = 0.
Il tourne d'une case par seconde. La capsule arrive devant le disque i à
l'instant `t + i`, donc la case doit y être vide :

    (depart + t + i) mod positions == 0

Réponse : le plus petit `t` qui satisfait **tous** les disques.
"""

from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day15.txt"

MOTIF = re.compile(
    r"Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+)\."
)


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def parse_disques(lines):
    """Liste de (numéro, positions, position_de_départ)."""
    disques = []
    for ligne in lines:
        trouve = MOTIF.search(ligne)
        if trouve:
            numero, positions, depart = (int(groupe) for groupe in trouve.groups())
            disques.append((numero, positions, depart))
    return sorted(disques)


def aligne(t, disques):
    """Vrai si tous les disques sont à la case 0 au moment où la capsule passe."""
    return all((depart + t + numero) % positions == 0 for numero, positions, depart in disques)


def resoudre(disques):
    """Plus petit t satisfaisant tous les disques.

    La période globale est le PPCM des nombres de positions : on teste les
    candidats par pas croissants plutôt que de tous les essayer.
    """
    from math import lcm

    periode = 1
    for _, positions, _ in disques:
        periode = lcm(periode, positions)

    t = 0
    while t < periode * 100:  # garde-fou
        if aligne(t, disques):
            return t
        t += 1
    return None


def solve(lines):
    return resoudre(parse_disques(lines))


def main():
    print("Premier instant possible:", solve(read_lines()))


if __name__ == "__main__":
    main()
