"""2016, jour 19 : An Elephant Named Joseph — partie 2.

Variante : chaque elfe élimine l'elfe **assis en face de lui** dans le cercle
(le cercle se rétrécissant à chaque tour), puis le tour passe au suivant.

La solution a une forme fermée. Soit `p = 3^m` la plus grande puissance de 3
inférieure ou égale à `n` :

  - si `n == p`      -> `n`
  - si `n - p <= p`  -> `n - p`
  - sinon            -> `2n - 3p`

`simuler()` est une simulation naïve (O(n²)), volontairement écrite de la
manière la plus directe possible : elle sert de référence pour valider la
formule sur les petites valeurs. La formule évite la simulation pour les
3 millions d'elfes du puzzle.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day19.txt"


def lire_entree():
    """Renvoie le nombre d'elfes (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return int(f.read().strip())
    return int(sys.stdin.read().strip())


def survivant_formule(n):
    """Formule fermée pour la variante « en face »."""
    if n <= 0:
        raise ValueError("il faut au moins un elfe")
    puissance = 1
    while puissance * 3 <= n:
        puissance *= 3
    if n == puissance:
        return n
    if n - puissance <= puissance:
        return n - puissance
    return 2 * n - 3 * puissance


def simuler(n):
    """Simulation naïve : l'elfe courant élimine celui qui est à l'opposé.

    Coût O(n²) : à réserver aux petites valeurs (vérification).
    """
    elfes = list(range(1, n + 1))
    courant = 0

    while len(elfes) > 1:
        face = (courant + len(elfes) // 2) % len(elfes)
        elfes.pop(face)
        if face < courant:          # l'elfe courant a reculé d'une place
            courant -= 1
        courant = (courant + 1) % len(elfes)

    return elfes[0]


def solve(n):
    return survivant_formule(n)


def main():
    print("Elfe survivant (en face):", solve(lire_entree()))


if __name__ == "__main__":
    main()
