"""2017, jour 12 : Digital Plumber — partie 1.

Chaque ligne a la forme `a <-> b, c, d`. Les liens sont **symétriques** (le
fichier les liste des deux côtés, mais on ne s'appuie pas dessus : on ajoute
toujours les deux sens).

Réponse : taille de la composante connexe contenant le programme 0.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day12.txt"


def read_lines():
    """Renvoie les lignes brutes (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        return path.read_text().splitlines()
    return sys.stdin.read().splitlines()


def parse(lignes):
    """Renvoie {programme: [voisins]} avec les liens dans les deux sens."""
    voisins = {}
    for ligne in lignes:
        if not ligne.strip():
            continue
        gauche, droite = ligne.split("<->")
        source = int(gauche.strip())
        cibles = [int(x) for x in droite.split(",") if x.strip()]
        voisins.setdefault(source, [])
        for cible in cibles:
            voisins[source].append(cible)
            voisins.setdefault(cible, []).append(source)
    return voisins


def composante(voisins, depart):
    """Ensemble des programmes reliés à `depart` (parcours en largeur)."""
    vus = {depart}
    pile = [depart]
    while pile:
        courant = pile.pop()
        for v in voisins.get(courant, []):
            if v not in vus:
                vus.add(v)
                pile.append(v)
    return vus


def solve(lignes):
    return len(composante(parse(lignes), 0))


def main():
    print("Programmes du groupe de 0:", solve(read_lines()))


if __name__ == "__main__":
    main()
