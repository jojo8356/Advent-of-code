"""2016, jour 8 : Two-Factor Authentication — partie 1.

Écran de 50 × 6 pixels, tous éteints au départ. Trois instructions :

  - `rect AxB`              allume un rectangle de A × B en haut à gauche ;
  - `rotate row y=A by B`   décale la ligne A de B vers la droite (circulaire) ;
  - `rotate column x=A by B` décale la colonne A de B vers le bas (circulaire).

Réponse : nombre de pixels allumés à la fin.
"""

from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day08.txt"
LARGEUR, HAUTEUR = 50, 6


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def ecran_vide(largeur=LARGEUR, hauteur=HAUTEUR):
    return [[False] * largeur for _ in range(hauteur)]


def executer(instructions, largeur=LARGEUR, hauteur=HAUTEUR):
    """Applique toutes les instructions et renvoie l'écran final."""
    ecran = ecran_vide(largeur, hauteur)

    for instruction in instructions:
        instruction = instruction.strip()
        if not instruction:
            continue

        if instruction.startswith("rect"):
            a, b = map(int, re.match(r"rect (\d+)x(\d+)", instruction).groups())
            for y in range(b):
                for x in range(a):
                    ecran[y][x] = True

        elif instruction.startswith("rotate row"):
            y, decalage = map(int, re.match(r"rotate row y=(\d+) by (\d+)", instruction).groups())
            ecran[y] = ecran[y][-decalage % largeur:] + ecran[y][:-decalage % largeur]

        elif instruction.startswith("rotate column"):
            x, decalage = map(int, re.match(r"rotate column x=(\d+) by (\d+)", instruction).groups())
            colonne = [ecran[y][x] for y in range(hauteur)]
            decalage %= hauteur
            colonne = colonne[-decalage:] + colonne[:-decalage]
            for y in range(hauteur):
                ecran[y][x] = colonne[y]

    return ecran


def solve(lines):
    """Nombre de pixels allumés."""
    return sum(pixel for ligne in executer(lines) for pixel in ligne)


def main():
    print("Pixels allumés:", solve(read_lines()))


if __name__ == "__main__":
    main()
