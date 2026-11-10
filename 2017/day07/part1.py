"""2017, jour 7 : Recursive Circus — partie 1.

Chaque ligne décrit un programme : `nom (poids)` puis éventuellement
`-> enfants`. La racine est le **seul** programme qui n'est jamais enfant
d'un autre.
"""

from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day07.txt"

LIGNE = re.compile(r"^(\w+)\s+\((\d+)\)(?:\s*->\s*(.*))?$")


def read_lines():
    """Renvoie les lignes brutes (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        return path.read_text().splitlines()
    return sys.stdin.read().splitlines()


def parse(lignes):
    """Renvoie {nom: (poids, [enfants])}."""
    programme = {}
    for ligne in lignes:
        ligne = ligne.strip()
        if not ligne:
            continue
        m = LIGNE.match(ligne)
        if not m:
            raise ValueError(f"ligne illisible : {ligne!r}")
        nom, poids, enfants = m.groups()
        liste = [e.strip() for e in enfants.split(",")] if enfants else []
        programme[nom] = (int(poids), liste)
    return programme


def trouver_racine(programme):
    """Le programme qui n'apparaît dans aucune liste d'enfants."""
    enfants = {e for _, liste in programme.values() for e in liste}
    racines = [nom for nom in programme if nom not in enfants]
    if len(racines) != 1:
        raise ValueError(f"{len(racines)} racines candidates : {racines}")
    return racines[0]


def solve(lignes):
    return trouver_racine(parse(lignes))


def main():
    print("Racine:", solve(read_lines()))


if __name__ == "__main__":
    main()
