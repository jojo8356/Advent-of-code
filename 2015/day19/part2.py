"""Jour 19, partie 2 : nombre minimal d'étapes pour fabriquer la molécule.

Deux méthodes, dans cet ordre :

1. **Remontée gloutonne** (exacte sur les entrées d'Advent of Code) : on
   applique les règles à l'envers (`AB -> A`) en prenant à chaque tour celle
   dont le membre droit est le plus long, jusqu'à revenir à `e`.
2. **Formule fermée**, utilisée si la remontée se bloque : chaque atome de la
   molécule coûte une étape, sauf `Rn`/`Ar` qui referment une branche déjà
   comptée et `Y` qui en sépare deux :

       étapes = atomes - 1 - (nombre de Rn) - (nombre de Ar) - 2 * (nombre de Y)

Les deux méthodes donnent 200 sur l'entrée du puzzle.
"""

from pathlib import Path
import re
import sys

from part1 import parse_input

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day19.txt"
ATOME = re.compile(r"[A-Z][a-z]?")


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def remonter(replacements, molecule):
    """Remontée gloutonne de la molécule vers `e` ; renvoie None si elle bloque."""
    inverses = sorted(
        ((droite, gauche) for gauche, droite in replacements),
        key=lambda regle: -len(regle[0]),
    )

    etapes = 0
    while molecule != "e":
        for motif, remplacement in inverses:
            position = molecule.find(motif)
            if position != -1:
                molecule = (
                    molecule[:position] + remplacement + molecule[position + len(motif):]
                )
                etapes += 1
                break
        else:
            return None  # impasse : on laisse la formule fermée trancher
    return etapes


def formule(atomes):
    """Nombre d'étapes déduit de la structure de la molécule."""
    return (
        len(atomes)
        - 1
        - atomes.count("Rn")
        - atomes.count("Ar")
        - 2 * atomes.count("Y")
    )


def compter_etapes(replacements, molecule):
    etapes = remonter(replacements, molecule)
    if etapes is not None:
        return etapes
    return formule(ATOME.findall(molecule))


def solve(lines):
    replacements, molecule = parse_input(lines)
    return compter_etapes(replacements, molecule)


def main():
    print("Minimum number of steps to make the medicine:", solve(read_lines()))


if __name__ == "__main__":
    main()
