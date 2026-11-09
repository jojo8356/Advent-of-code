"""2016, jour 1 : No Time for a Taxicab — partie 2.

Même parcours, mais on s'arrête à la **première position visitée deux fois**
(le point de départ compte comme visité). Réponse : distance de Manhattan de
cette position.
"""

from pathlib import Path
import sys

from part1 import DIRECTIONS, parse_instructions, read_lines

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day01.txt"


def premiere_position_revisitee(instructions):
    """Coordonnées de la première case franchie deux fois (ou None)."""
    x = y = 0
    cap = 0
    vues = {(0, 0)}

    for sens, distance in instructions:
        cap = (cap + (1 if sens == "R" else -1)) % 4
        dx, dy = DIRECTIONS[cap]
        # on avance d'un pâté de maisons à la fois pour détecter chaque case
        for _ in range(distance):
            x += dx
            y += dy
            if (x, y) in vues:
                return x, y
            vues.add((x, y))
    return None


def solve(lines):
    """Distance de Manhattan de la première position visitée deux fois."""
    position = premiere_position_revisitee(parse_instructions(" ".join(lines)))
    if position is None:
        return "aucune position visitée deux fois"
    return abs(position[0]) + abs(position[1])


def main():
    print("Distance de Manhattan du premier doublon:", solve(read_lines()))


if __name__ == "__main__":
    main()
