"""2016, jour 8 : Two-Factor Authentication — partie 2.

Les pixels allumés dessinent des lettres de 5 × 6 en haut de l'écran, à raison
de 10 lettres de 5 colonnes (50 / 5). On décode le mot lettre par lettre.
"""

from pathlib import Path
import sys

from part1 import executer, read_lines

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day08.txt"

# Police 5 × 6 des lettres dessinées par l'écran (`#` = pixel allumé)
POLICE = {
    "C": [".##..", "#..#.", "#....", "#....", "#..#.", ".##.."],
    "H": ["#..#.", "#..#.", "####.", "#..#.", "#..#.", "#..#."],
    "J": ["..##.", "...#.", "...#.", "...#.", "#..#.", ".##.."],
    "K": ["#..#.", "#.#..", "##...", "#.#..", "#.#..", "#..#."],
    "L": ["#....", "#....", "#....", "#....", "#....", "####."],
    "P": ["###..", "#..#.", "#..#.", "###..", "#....", "#...."],
    "R": ["###..", "#..#.", "#..#.", "###..", "#.#..", "#..#."],
    "Y": ["#...#", "#...#", ".#.#.", "..#..", "..#..", "..#.."],
    "Z": ["####.", "...#.", "..#..", ".#...", "#....", "####."],
}


def dessiner(ecran):
    """Rendu ASCII de l'écran."""
    return "\n".join("".join("#" if pixel else "." for pixel in ligne) for ligne in ecran)


def lire_code(ecran, largeur_lettre=5):
    """Décode les lettres de l'écran, blocs de `largeur_lettre` colonnes."""
    hauteur = len(ecran)
    largeur = len(ecran[0])
    lignes = ["".join("#" if pixel else "." for pixel in ligne) for ligne in ecran]

    code = []
    for debut in range(0, largeur - largeur_lettre + 1, largeur_lettre):
        motif = [ligne[debut:debut + largeur_lettre] for ligne in lignes[:hauteur]]
        if not any("#" in ligne for ligne in motif):
            continue  # bloc vide (fin d'écran)
        for lettre, reference in POLICE.items():
            if motif == reference:
                code.append(lettre)
                break
        else:
            code.append("?")
    return "".join(code)


def solve(lines):
    return lire_code(executer(lines))


def main():
    ecran = executer(read_lines())
    print(dessiner(ecran))
    print()
    print("Code:", lire_code(ecran))


if __name__ == "__main__":
    main()
