"""2017, jour 9 : Stream Processing — partie 1.

Un flux contient des groupes `{...}`, des déchets `<...>` et des annulations `!`
qui neutralisent le caractère suivant.

- `!` : on saute le caractère suivant (partout, groupe ou déchet).
- `{` hors déchet : on entre dans un groupe, profondeur + 1.
- `}` hors déchet : le groupe vaut sa **profondeur**, qu'on ajoute au score.
- `<` hors déchet : début d'un déchet ; `>` hors déchet : fin du déchet.

Réponse : score total des groupes.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day09.txt"


def read_stream():
    """Renvoie le flux complet (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    texte = path.read_text() if path.exists() else sys.stdin.read()
    return texte.strip()


def analyser(flux):
    """Renvoie (score total des groupes, nombre de caractères de déchet)."""
    profondeur = 0
    score = 0
    dechets = 0
    dans_dechet = False
    i = 0
    while i < len(flux):
        c = flux[i]
        if c == "!":  # annulation : on saute le caractère suivant
            i += 2
            continue
        if dans_dechet:
            if c == ">":
                dans_dechet = False
            else:
                dechets += 1
        elif c == "<":
            dans_dechet = True
        elif c == "{":
            profondeur += 1
        elif c == "}":
            score += profondeur
            profondeur -= 1
        i += 1
    return score, dechets


def solve(flux):
    return analyser(flux)[0]


def main():
    print("Score total:", solve(read_stream()))


if __name__ == "__main__":
    main()
