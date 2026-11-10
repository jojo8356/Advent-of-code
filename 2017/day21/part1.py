"""2017, jour 21 : Fractal Art — partie 1.

La grille démarre en `.#./..#/###`. À chaque itération :
  - si la taille est divisible par 2, on découpe en blocs 2×2,
  - sinon (divisible par 3), en blocs 3×3,
  - chaque bloc est remplacé par la règle correspondante, en tenant compte des
    **8 symétries** (rotations et réflexions) du motif source,
  - les blocs remplacés sont réassemblés en une grille de taille supérieure.

Réponse : nombre de `#` après 5 itérations.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day21.txt"
DEPART = (".#.", "..#", "###")
ITERATIONS = 5


def read_regles():
    """Renvoie {motif (tuple de lignes): remplacement (tuple de lignes)}."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    texte = path.read_text() if path.exists() else sys.stdin.read()
    regles = {}
    for ligne in texte.splitlines():
        ligne = ligne.strip()
        if not ligne or "=>" not in ligne:
            continue
        gauche, droite = (partie.strip() for partie in ligne.split("=>"))
        motif = tuple(ligne_bloc.strip() for ligne_bloc in gauche.split("/"))
        remplacement = tuple(ligne_bloc.strip() for ligne_bloc in droite.split("/"))
        for variante in symetries(motif):
            regles[variante] = remplacement
    return regles


def symetries(bloc):
    """Les 8 variantes d'un bloc (4 rotations × 2 réflexions), dédupliquées."""
    variantes = []
    courant = tuple(bloc)
    for _ in range(4):
        variantes.append(courant)
        variantes.append(tuple(ligne[::-1] for ligne in courant))  # miroir
        courant = tuple("".join(colonne) for colonne in zip(*courant[::-1]))
    # déduplication en conservant l'ordre
    vues = set()
    uniques = []
    for v in variantes:
        if v not in vues:
            vues.add(v)
            uniques.append(v)
    return uniques


def decouper(grille, taille_bloc):
    """Découpe la grille en blocs de `taille_bloc` × `taille_bloc`."""
    taille = len(grille)
    blocs = []
    for ligne_bloc in range(taille // taille_bloc):
        rangee = []
        for colonne_bloc in range(taille // taille_bloc):
            bloc = tuple(
                grille[ligne_bloc * taille_bloc + r][
                    colonne_bloc * taille_bloc:(colonne_bloc + 1) * taille_bloc]
                for r in range(taille_bloc)
            )
            rangee.append(bloc)
        blocs.append(rangee)
    return blocs


def assembler(blocs):
    """Réassemble une grille à partir d'une matrice de blocs de même taille."""
    lignes = []
    for rangee in blocs:
        hauteur = len(rangee[0])
        for r in range(hauteur):
            lignes.append("".join(bloc[r] for bloc in rangee))
    return tuple(lignes)


def une_iteration(grille, regles):
    """Applique une itération de l'algorithme fractal."""
    taille = len(grille)
    taille_bloc = 2 if taille % 2 == 0 else 3
    blocs = decouper(grille, taille_bloc)
    remplaces = []
    for rangee in blocs:
        nouvelle_rangee = []
        for bloc in rangee:
            if bloc not in regles:
                raise KeyError(f"aucune règle pour le bloc {bloc}")
            nouvelle_rangee.append(regles[bloc])
        remplaces.append(nouvelle_rangee)
    return assembler(remplaces)


def solve(grille=DEPART, iterations=ITERATIONS, regles=None):
    if regles is None:
        regles = read_regles()
    for _ in range(iterations):
        grille = une_iteration(grille, regles)
    return sum(ligne.count("#") for ligne in grille)


def main():
    print("Pixels allumés:", solve())


if __name__ == "__main__":
    main()
