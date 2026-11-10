"""2017, jour 15 : Dueling Generators — partie 1.

Générateurs à congruences linéaires :
    valeur = (valeur * facteur) mod 2147483647
    A : facteur 16807        B : facteur 48271

On compare les 16 bits de poids faible de **40 millions** de paires.
Réponse : nombre de paires où ces 16 bits sont identiques.

Le calcul est découpé en tranches réparties sur plusieurs processus : chaque
tranche repart de la valeur de départ élevée à la bonne puissance (le générateur
est déterministe), puis on additionne les comptes.
"""

from pathlib import Path
import sys
from concurrent.futures import ProcessPoolExecutor

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day15.txt"

MODULO = 2147483647
FACTEUR_A = 16807
FACTEUR_B = 48271
MASQUE = (1 << 16) - 1          # 65535
PAIRES = 40_000_000
TRANCHES = 16


def read_departs():
    """Renvoie (départ A, départ B) depuis le fichier ou stdin."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    texte = path.read_text() if path.exists() else sys.stdin.read()
    valeurs = [int(mot) for mot in texte.split() if mot.lstrip("-").isdigit()]
    if len(valeurs) != 2:
        raise ValueError(f"deux valeurs attendues, obtenu {valeurs}")
    return valeurs[0], valeurs[1]


def avancer(valeur, facteur, n):
    """Valeur après `n` itérations, par exponentiation modulaire rapide."""
    resultat = valeur
    base = facteur
    while n:
        if n & 1:
            resultat = (resultat * base) % MODULO
        base = (base * base) % MODULO
        n >>= 1
    return resultat


def _tranche(arguments):
    """Compte les coïncidences sur une tranche (fonction de haut niveau)."""
    depart_a, depart_b, nombre = arguments
    total = 0
    a, b = depart_a, depart_b
    for _ in range(nombre):
        a = (a * FACTEUR_A) % MODULO
        b = (b * FACTEUR_B) % MODULO
        if (a & MASQUE) == (b & MASQUE):
            total += 1
    return total


def tranches(depart_a, depart_b, paires):
    """Découpe les `paires` en tranches égales, avec leurs valeurs de départ."""
    base, reste = divmod(paires, TRANCHES)
    decalage_a = decalage_b = 0
    for i in range(TRANCHES):
        nombre = base + (1 if i < reste else 0)
        yield (avancer(depart_a, FACTEUR_A, decalage_a),
               avancer(depart_b, FACTEUR_B, decalage_b),
               nombre)
        decalage_a += nombre
        decalage_b += nombre


def compter_egaux(a, b, paires=PAIRES):
    """Nombre de paires dont les 16 bits de poids faible coïncident."""
    with ProcessPoolExecutor() as executeur:
        return sum(executeur.map(_tranche, list(tranches(a, b, paires))))


def solve(departs, paires=PAIRES):
    return compter_egaux(departs[0], departs[1], paires)


def main():
    print("Paires identiques:", solve(read_departs()))


if __name__ == "__main__":
    main()
