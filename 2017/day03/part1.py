"""2017, jour 3 : Spiral Memory — partie 1.

Spirale horaire : la case 1 est au centre, la 2 à sa droite, puis on tourne.
Réponse : distance de Manhattan entre le numéro cherché et le centre.

Le numéro `n` tombe sur l'anneau `k` (le centre étant l'anneau 0) tel que
`(2k−1)² < n ≤ (2k+1)²`. Chaque anneau a un côté de `2k + 1` cases ; son plus
petit numéro est `(2k−1)² + 1`, situé juste à droite du coin bas-droit.

Sur l'anneau, on avance de `(n − (2k−1)² − 1)` cases ; les quatre milieux de
côté sont à `k` cases du centre, et la distance décroît linéairement vers les
coins (à `2k` du centre). D'où :

    distance = k + |(position mod 2k) − (k − 1)|
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day03.txt"


def read_nombre():
    """Renvoie le numéro cherché (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return int(f.read().strip())
    return int(sys.stdin.read().strip())


def distance_manhattan(n):
    """Distance de Manhattan entre `n` et le centre (1)."""
    if n == 1:
        return 0

    # anneau k : plus petit côté impair dont le carré couvre n
    cote = 1
    while cote * cote < n:
        cote += 2
    k = (cote - 1) // 2          # numéro de l'anneau
    cote_anneau = cote - 1       # 2k : nombres sur chaque côté (hors coin)

    base = (cote - 2) ** 2       # carré de l'anneau précédent
    position = n - base - 1      # 0 = première case de l'anneau

    return k + abs(position % cote_anneau - (k - 1))


def solve(n):
    return distance_manhattan(n)


def main():
    print("Distance de Manhattan:", solve(read_nombre()))


if __name__ == "__main__":
    main()
