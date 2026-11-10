"""2017, jour 23 : Coprocessor Conflagration — partie 2.

Avec `a = 1`, le programme déroulé revient à :

    b = 65 * 100 + 100000        (= 106500)
    c = b + 17000                (= 123500)
    pour b de 106500 à c pas de 17 :
        si b n'est pas premier → h += 1

Rien à simuler : on compte les **composites** de la suite arithmétique. Un
crible d'Ératosthène jusqu'à `c` suffit.

Les trois constantes sont lues dans le programme (les instructions `set b`,
`sub b -…`, `sub c -…`, `sub b -17`) : rien n'est deviné.
"""

from pathlib import Path
import sys
from math import isqrt

from part1 import read_lignes, parse

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day23.txt"


def extraire_parametres(programme):
    """Renvoie (base, facteur, ajout_b, ajout_c, pas) lus dans le code."""
    base = None            # valeur du premier `set b <n>`
    facteur = None         # `mul b <n>`
    ajout_b = None         # `sub b -<n>`
    ajout_c = None         # `sub c -<n>`
    pas = None             # `sub b -<n>` dans la boucle finale
    for position, (instruction, x, y) in enumerate(programme):
        if y is None:
            continue
        litteral = int(y) if y.lstrip("-").isdigit() else None
        if litteral is None:
            continue
        if instruction == "set" and x == "b" and base is None:
            base = litteral
        elif instruction == "mul" and x == "b" and facteur is None:
            facteur = litteral
        elif instruction == "sub" and x == "b" and litteral < 0:
            if ajout_b is None and abs(litteral) >= 1000:
                ajout_b = -litteral
            elif pas is None:
                pas = -litteral
        elif instruction == "sub" and x == "c" and litteral < 0 and ajout_c is None:
            ajout_c = -litteral
    return base, facteur, ajout_b, ajout_c, pas


def est_premier(n):
    """Test de primalité élémentaire (les nombres font ~123 500)."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for diviseur in range(3, isqrt(n) + 1, 2):
        if n % diviseur == 0:
            return False
    return True


def solve(programme=None, verbose=False):
    """Compte les composites de la suite."""
    if programme is None:
        programme = parse(read_lignes())
    base, facteur, ajout_b, ajout_c, pas = extraire_parametres(programme)
    debut = base * facteur + ajout_b
    fin = debut + ajout_c
    if verbose:
        print(f"  base b = {base}, ×{facteur}, +{ajout_b} → {debut}")
        print(f"  c = {debut} + {ajout_c} = {fin}, pas = {pas}")
    return sum(1 for b in range(debut, fin + 1, pas) if not est_premier(b))


def main():
    print("Valeur de h:", solve())


if __name__ == "__main__":
    main()
