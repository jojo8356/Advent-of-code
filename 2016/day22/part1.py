"""2016, jour 22 : Grid Computing — partie 1.

Chaque ligne `df` décrit un nœud : coordonnées, taille, utilisé, disponible.
Un couple de nœuds (A, B) est **viable** si A n'est pas vide et si les données
de A tiennent dans l'espace libre de B. Réponse : nombre de couples viables.
"""

from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day22.txt"

MOTIF = re.compile(
    r"/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%"
)


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def parse_noeuds(lines):
    """Liste de dictionnaires (x, y, taille, utilise, libre)."""
    noeuds = []
    for ligne in lines:
        trouve = MOTIF.search(ligne)
        if not trouve:
            continue
        x, y, taille, utilise, libre, _pct = (int(groupe) for groupe in trouve.groups())
        noeuds.append({"x": x, "y": y, "taille": taille, "utilise": utilise, "libre": libre})
    return noeuds


def compter_viables(noeuds):
    """Nombre de couples (A, B) avec A non vide et utilise(A) <= libre(B)."""
    viables = 0
    for a in noeuds:
        if a["utilise"] == 0:
            continue  # A doit contenir des données
        for b in noeuds:
            if a is b:
                continue
            if a["utilise"] <= b["libre"]:
                viables += 1
    return viables


def solve(lines):
    return compter_viables(parse_noeuds(lines))


def main():
    print("Couples viables:", solve(read_lines()))


if __name__ == "__main__":
    main()
