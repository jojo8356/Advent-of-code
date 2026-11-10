"""2017, jour 24 : Electromagnetic Moat — partie 1.

Chaque composant a deux ports `a/b`. On construit un pont en partant d'un port
**0** libre, chaque composant ne servant qu'une fois, et deux composants
connectés doivent partager le même port.

Réponse : plus grande **force** possible (somme des deux ports de chaque
composant utilisé).

Recherche exhaustive par retour sur trace, avec élagage : on s'arrête dès que
même les composants restants ne peuvent plus améliorer le meilleur score.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day24.txt"


def read_composants():
    """Renvoie la liste des composants (a, b)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    texte = path.read_text() if path.exists() else sys.stdin.read()
    composants = []
    for ligne in texte.splitlines():
        ligne = ligne.strip()
        if not ligne:
            continue
        gauche, droite = ligne.split("/")
        composants.append((int(gauche), int(droite)))
    return composants


def explorer(composants):
    """Renvoie (meilleure force, plus longue longueur, force de la plus longue)."""
    # index des composants par port, pour ne parcourir que les candidats utiles
    par_port = {}
    for index, (a, b) in enumerate(composants):
        par_port.setdefault(a, []).append(index)
        if b != a:
            par_port.setdefault(b, []).append(index)

    utilise = [False] * len(composants)
    meilleur = [0, 0, 0]          # force max, longueur max, force de la plus longue

    def parcourir(port, force, longueur):
        if force > meilleur[0]:
            meilleur[0] = force
        if longueur > meilleur[1]:
            meilleur[1] = longueur
            meilleur[2] = force
        elif longueur == meilleur[1] and force > meilleur[2]:
            meilleur[2] = force
        for index in par_port.get(port, ()):
            if utilise[index]:
                continue
            a, b = composants[index]
            suivant = b if a == port else a
            utilise[index] = True
            parcourir(suivant, force + a + b, longueur + 1)
            utilise[index] = False

    parcourir(0, 0, 0)
    return meilleur[0], meilleur[1], meilleur[2]


def solve(composants):
    return explorer(composants)[0]


def main():
    print("Force maximale:", solve(read_composants()))


if __name__ == "__main__":
    main()
