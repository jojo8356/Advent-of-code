"""2016, jour 1 : No Time for a Taxicab — partie 1.

On part face au nord. Chaque instruction est une rotation (R = droite,
L = gauche) suivie d'une distance en pâtés de maisons. Réponse : distance de
Manhattan entre l'arrivée et le point de départ.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day01.txt"

# (dx, dy) dans l'ordre : nord, est, sud, ouest
DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def parse_instructions(text):
    """`R2, L3` -> [('R', 2), ('L', 3)]."""
    instructions = []
    for morceau in text.replace("\n", " ").split(","):
        morceau = morceau.strip()
        if morceau:
            instructions.append((morceau[0], int(morceau[1:])))
    return instructions


def solve(lines):
    """Distance de Manhattan parcourue jusqu'au point d'arrivée."""
    x = y = 0
    cap = 0  # 0 = nord, 1 = est, 2 = sud, 3 = ouest

    for sens, distance in parse_instructions(" ".join(lines)):
        cap = (cap + (1 if sens == "R" else -1)) % 4
        dx, dy = DIRECTIONS[cap]
        x += dx * distance
        y += dy * distance

    return abs(x) + abs(y)


def main():
    print("Distance de Manhattan:", solve(read_lines()))


if __name__ == "__main__":
    main()
