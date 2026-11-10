"""2016, jour 18 : Like a Rogue — partie 1.

Une rangée est fabriquée à partir de la précédente : une tuile devient un
piège (`^`) si ses deux parents **extérieurs** sont différents (l'un `^`,
l'autre `.`). Le parent du centre n'intervient pas. Hors de la rangée, les
voisins sont considérés sûrs (`.`).

Réponse : nombre de tuiles sûres (`.`) sur **40** rangées, rangée initiale
comprise.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day18.txt"
LIGNES = 40


def read_ligne():
    """Renvoie la rangée initiale (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    return sys.stdin.read().strip()


def rangee_suivante(rangée):
    """Rangée suivante : piège si les deux parents extérieurs diffèrent.

    Le parent du centre est sans effet. On compare donc, pour chaque position,
    les voisins gauche et droit (`.` hors des bords).
    """
    etendue = "." + rangée + "."
    suivante = []
    for i in range(len(rangée)):
        gauche, _centre, droite = etendue[i:i + 3]
        suivante.append("^" if gauche != droite else ".")
    return "".join(suivante)


def compter_sures(rangée, lignes=LIGNES):
    """Nombre de tuiles sûres sur `lignes` rangées."""
    total = rangée.count(".")
    for _ in range(lignes - 1):
        rangée = rangee_suivante(rangée)
        total += rangée.count(".")
    return total


def solve(ligne, lignes=LIGNES):
    return compter_sures(ligne, lignes)


def main():
    print(f"Tuiles sûres sur {LIGNES} rangées :", solve(read_ligne()))


if __name__ == "__main__":
    main()
