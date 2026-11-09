"""2016, jour 2 : Bathroom Security — partie 1.

Un bouton est enfoncé à la fin de chaque ligne d'instructions (`U`, `D`, `L`,
`R`). On part du bouton 5 d'un pavé numérique 3×3 ; les déplacements qui
sortiraient du pavé sont ignorés.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day02.txt"

# Pavé numérique 3×3 : coordonnées (x, y), y vers le bas
PAVE = {
    (0, 0): "1", (1, 0): "2", (2, 0): "3",
    (0, 1): "4", (1, 1): "5", (2, 1): "6",
    (0, 2): "7", (1, 2): "8", (2, 2): "9",
}
DEPART = (1, 1)  # le bouton 5

DEPLACEMENTS = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def code(lines, pave=None, depart=None):
    """Code d'accès, un bouton par ligne d'instructions."""
    pave = pave or PAVE
    x, y = depart or DEPART
    chiffres = []

    for ligne in lines:
        for instruction in ligne.strip():
            dx, dy = DEPLACEMENTS[instruction]
            if (x + dx, y + dy) in pave:  # sinon on reste sur place
                x, y = x + dx, y + dy
        chiffres.append(pave[(x, y)])

    return "".join(chiffres)


def solve(lines):
    return code(lines)


def main():
    print("Code:", solve(read_lines()))


if __name__ == "__main__":
    main()
