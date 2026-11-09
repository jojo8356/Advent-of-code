"""2016, jour 4 : Security Through Obscurity — partie 1.

Une ligne a la forme `nom-chiffre[somme]` où `nom` est fait de lettres et de
tirets. Une salle est valide si la somme de contrôle est constituée des cinq
lettres les plus fréquentes du nom (tirets exclus), départagées par ordre
alphabétique. Réponse : somme des identifiants des salles valides.
"""

from collections import Counter
from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day04.txt"

MOTIF = re.compile(r"^([a-z-]+)-(\d+)\[([a-z]{5})\]$")


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def parse_salle(ligne):
    """`nom-123[abcde]` -> ('nom', 123, 'abcde')."""
    trouve = MOTIF.match(ligne.strip())
    if not trouve:
        raise ValueError(f"ligne illisible : {ligne!r}")
    return trouve.group(1), int(trouve.group(2)), trouve.group(3)


def somme_de_controle(nom):
    """Cinq lettres les plus fréquentes (tirets exclus), à fréquence égale : ordre alphabétique."""
    lettres = Counter(nom.replace("-", ""))
    return "".join(
        lettre for lettre, _ in sorted(lettres.items(), key=lambda paire: (-paire[1], paire[0]))
    )[:5]


def est_valide(nom, identifiant, controle):
    return somme_de_controle(nom) == controle


def solve(lines):
    """Somme des identifiants des salles dont la somme de contrôle est correcte."""
    total = 0
    for ligne in lines:
        if not ligne.strip():
            continue
        nom, identifiant, controle = parse_salle(ligne)
        if est_valide(nom, identifiant, controle):
            total += identifiant
    return total


def main():
    print("Somme des identifiants valides:", solve(read_lines()))


if __name__ == "__main__":
    main()
