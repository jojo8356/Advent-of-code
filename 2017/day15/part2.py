"""2017, jour 15 : Dueling Generators — partie 2.

Ajout d'un filtre : on ne garde, parmi les valeurs générées, que
- celles de A multiples de 4,
- celles de B multiples de 8.
Chaque générateur peut boucler plusieurs fois pour produire une valeur retenue.

Réponse : nombre de paires identiques (16 bits de poids faible) sur
**5 millions** de paires retenues.

Les deux filtres sont écrits **en ligne** dans la boucle : un appel de fonction
par valeur retenue coûterait plusieurs secondes de plus.
"""

from pathlib import Path
import sys

from part1 import read_departs, MODULO, FACTEUR_A, FACTEUR_B, MASQUE

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day15.txt"
PAIRES = 5_000_000


def compter_egaux(a, b, paires=PAIRES):
    """Nombre de paires retenues dont les 16 bits de poids faible coïncident."""
    total = 0
    for _ in range(paires):
        a = (a * FACTEUR_A) % MODULO
        while a & 3:                       # A retenu si multiple de 4
            a = (a * FACTEUR_A) % MODULO
        b = (b * FACTEUR_B) % MODULO
        while b & 7:                       # B retenu si multiple de 8
            b = (b * FACTEUR_B) % MODULO
        if (a & MASQUE) == (b & MASQUE):
            total += 1
    return total


def solve(departs, paires=PAIRES):
    return compter_egaux(departs[0], departs[1], paires)


def main():
    print("Paires identiques (filtrées):", solve(read_departs()))


if __name__ == "__main__":
    main()
