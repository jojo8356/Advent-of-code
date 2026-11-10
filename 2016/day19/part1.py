"""2016, jour 19 : An Elephant Named Joseph — partie 1.

Les elfes sont en cercle ; à tour de rôle, chaque elfe encore en jeu élimine
son voisin de gauche, puis c'est au suivant. Réponse : numéro de l'elfe qui
garde tous les cadeaux.

Cas classique du **problème de Josèphe** avec k = 2 : la solution se calcule
directement. Si `n = 2^m + r` (avec r < 2^m), le survivant est `2r + 1`.
La simulation en cercle est gardée comme vérification.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day19.txt"


def read_nombre():
    """Renvoie le nombre d'elfes (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return int(f.read().strip())
    return int(sys.stdin.read().strip())


def josephe_formule(n):
    """Formule fermée du survivant pour k = 2."""
    if n <= 0:
        raise ValueError("il faut au moins un elfe")
    puissance = 1
    while puissance * 2 <= n:
        puissance *= 2
    reste = n - puissance
    return 2 * reste + 1


def josephe_simulation(n):
    """Simulation explicite en cercle, pour les petites valeurs."""
    elfes = list(range(1, n + 1))
    courant = 0
    while len(elfes) > 1:
        # l'elfe courant élimine son voisin de gauche (l'index suivant)
        elfes.pop((courant + 1) % len(elfes))
        if (courant + 1) > len(elfes) - 1:
            courant = 0
        else:
            courant = (courant + 1) % len(elfes)
    return elfes[0]


def solve(n):
    return josephe_formule(n)


def main():
    print("Elfe survivant:", solve(read_nombre()))


if __name__ == "__main__":
    main()
