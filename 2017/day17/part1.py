"""2017, jour 17 : Spinlock — partie 1.

On part d'un tampon circulaire `[0]`, position 0. Pour chaque valeur `i` de 1 à
2017 : on avance de `pas` cases, puis on insère `i` juste après la case atteinte.

Réponse : valeur qui suit immédiatement **2017** dans le tampon final.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day17.txt"
INSERTIONS = 2017


def read_pas():
    """Renvoie le pas (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    texte = path.read_text() if path.exists() else sys.stdin.read()
    return int(texte.strip().split()[0])


def construire(pas, insertions=INSERTIONS):
    """Construit le tampon après `insertions` insertions."""
    tampon = [0]
    position = 0
    for valeur in range(1, insertions + 1):
        position = (position + pas) % len(tampon) + 1
        tampon.insert(position, valeur)
    return tampon


def apres(tampon, cible):
    """Valeur qui suit `cible` dans le tampon (cyclique)."""
    i = tampon.index(cible)
    return tampon[(i + 1) % len(tampon)]


def solve(pas, insertions=INSERTIONS):
    return apres(construire(pas, insertions), insertions)


def main():
    print("Valeur après 2017:", solve(read_pas()))


if __name__ == "__main__":
    main()
