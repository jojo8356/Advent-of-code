"""2017, jour 7 : Recursive Circus — partie 2.

Chaque disque doit supporter des tours de **même poids total**. On descend depuis
la racine en suivant l'enfant dont le poids de tour diffère de celui de ses
frères. Quand ses propres enfants sont équilibrés (ou qu'il n'en a pas), c'est
lui qui est mal taré : on renvoie le poids qu'il devrait avoir.
"""

from pathlib import Path
import sys

from part1 import read_lines, parse, trouver_racine

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day07.txt"


def poids_tours(programme):
    """Poids total de la tour de chaque programme (mémoïsé, sans récursion)."""
    total = {}
    for depart in programme:
        pile = [depart]
        while pile:
            nom = pile[-1]
            poids, enfants = programme[nom]
            if nom in total:
                pile.pop()
            elif all(e in total for e in enfants):
                total[nom] = poids + sum(total[e] for e in enfants)
                pile.pop()
            else:
                pile.extend(e for e in enfants if e not in total)
    return total


def poids_majoritaire(poids):
    """Poids qui revient le plus souvent parmi les frères."""
    return max(set(poids), key=poids.count)


def poids_corrige(programme):
    """Poids que devrait avoir le seul programme mal taré."""
    total = poids_tours(programme)
    nom = trouver_racine(programme)
    while True:
        _, enfants = programme[nom]
        if not enfants:
            raise ValueError("aucun déséquilibre trouvé")
        poids_enfants = [total[e] for e in enfants]
        cible = poids_majoritaire(poids_enfants)
        if all(p == cible for p in poids_enfants):
            raise ValueError("aucun déséquilibre trouvé")
        # l'enfant dont le poids de tour est unique parmi ses frères
        fautif = next(e for e in enfants if total[e] != cible)
        petits = [total[g] for g in programme[fautif][1]]
        if len(set(petits)) <= 1:  # équilibré, ou feuille
            return programme[fautif][0] + (cible - total[fautif])
        nom = fautif


def solve(lignes):
    return poids_corrige(parse(lignes))


def main():
    print("Poids corrigé:", solve(read_lines()))


if __name__ == "__main__":
    main()
