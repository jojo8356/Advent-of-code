"""2016, jour 20 : Firewall Rules — partie 1.

Chaque ligne du fichier décrit une plage d'adresses IP **interdites**,
au format `début-fin` (bornes incluses). Réponse : la plus petite adresse IP
non bloquée par aucune plage.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day20.txt"
MAX_IP = 4294967295


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def parse_plages(lines):
    """Liste de (début, fin) triée par début."""
    plages = []
    for ligne in lines:
        ligne = ligne.strip()
        if not ligne:
            continue
        debut, fin = map(int, ligne.split("-"))
        plages.append((debut, fin))
    return sorted(plages)


def fusionner(plages):
    """Fusionne les plages qui se chevauchent ou se touchent."""
    fusionnees = []
    for debut, fin in plages:
        if fusionnees and debut <= fusionnees[-1][1] + 1:
            fusionnees[-1] = (fusionnees[-1][0], max(fusionnees[-1][1], fin))
        else:
            fusionnees.append((debut, fin))
    return fusionnees


def premiere_libre(plages):
    """Plus petite adresse non couverte."""
    fusionnees = fusionner(plages)
    if not fusionnees or fusionnees[0][0] > 0:
        return 0
    return fusionnees[0][1] + 1


def solve(lines):
    return premiere_libre(parse_plages(lines))


def main():
    print("Plus petite adresse non bloquée:", solve(read_lines()))


if __name__ == "__main__":
    main()
