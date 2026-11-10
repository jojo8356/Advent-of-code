"""2017, jour 16 : Permutation Promenade — partie 1.

Seize programmes `a`..`p`. Trois mouvements, dans une liste circulaire implicite :
  - `sN`  : rotation à droite de N positions (les N derniers passent devant),
  - `xI/J` : échange des programmes aux positions I et J,
  - `pA/B` : échange des programmes nommés A et B (où qu'ils soient).

Réponse : ordre après **une** danse complète.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day16.txt"
PROGRAMMES = "abcdefghijklmnop"


def read_mouvements():
    """Renvoie la liste des mouvements (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    texte = path.read_text() if path.exists() else sys.stdin.read()
    return [m.strip() for m in texte.replace("\n", "").split(",") if m.strip()]


def danser(depart, mouvements):
    """Applique la suite de mouvements à la liste `depart`."""
    liste = list(depart)
    for mouvement in mouvements:
        type_ = mouvement[0]
        if type_ == "s":
            n = int(mouvement[1:])
            if n:
                liste = liste[-n:] + liste[:-n]
        elif type_ == "x":
            i, j = (int(v) for v in mouvement[1:].split("/"))
            liste[i], liste[j] = liste[j], liste[i]
        elif type_ == "p":
            a, b = mouvement[1], mouvement[3]
            i, j = liste.index(a), liste.index(b)
            liste[i], liste[j] = liste[j], liste[i]
        else:
            raise ValueError(f"mouvement inconnu : {mouvement!r}")
    return "".join(liste)


def solve(mouvements, depart=PROGRAMMES):
    return danser(depart, mouvements)


def main():
    print("Ordre final:", solve(read_mouvements()))


if __name__ == "__main__":
    main()
