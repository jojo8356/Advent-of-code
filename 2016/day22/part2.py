"""2016, jour 22 : Grid Computing — partie 2.

Amener les données du nœud en haut à droite (`x_max`, 0) jusqu'à `(0, 0)`.

Un transfert déplace **tout** l'occupant d'un nœud A vers un voisin B, à
condition que `utilise(A) <= libre(B)` (et A non vide).

**Preuve que le modèle « déplacer le trou » est exact pour ce puzzle :**

  - les données à déplacer pèsent 66 T ;
  - le seul nœud offrant assez de place est le nœud **vide** (92 T libres) ;
    tous les autres nœuds ont au plus 30 T libres ;
  - les nœuds « pleins » (used ≥ 490 T) ne peuvent jamais bouger.

Il n'y a donc aucune alternative : chaque transfert consiste à faire passer un
nœud adjacent dans la case vide, et l'unique objectif est d'amener le trou
jusqu'aux données puis de le faire « tracter » la cible vers la gauche.

Le coût se calcule alors en trois termes :

  1. distance du trou jusqu'à la case juste à **gauche** de la cible ;
  2. + 1 transfert pour y amener les données ;
  3. + 5 transferts par case de progression vers la gauche
     (le trou doit repasser derrière les données à chaque pas).

Un **BFS** sur l'état `(trou, position des données)` sert de vérification
croisée : il retrouve exactement le même total.
"""

from collections import deque
from pathlib import Path
import sys

from part1 import parse_noeuds, read_lines

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day22.txt"
SEUIL_PLEIN = 100  # un nœud utilisé au-delà ne peut bouger nulle part


def construire(noeuds):
    """Renvoie (largeur, hauteur, trou, cible, murs)."""
    grille = {(n["x"], n["y"]): n for n in noeuds}
    largeur = max(x for x, _ in grille) + 1
    hauteur = max(y for _, y in grille) + 1
    trou = next((pos for pos, n in grille.items() if n["utilise"] == 0), None)
    cible = (largeur - 1, 0)
    murs = {pos for pos, n in grille.items() if n["utilise"] > SEUIL_PLEIN}
    return largeur, hauteur, trou, cible, murs


def voisins(pos, largeur, hauteur):
    x, y = pos
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < largeur and 0 <= ny < hauteur:
            yield nx, ny


def distance(trou, but, largeur, hauteur, murs):
    """Distance du trou à `but` en évitant les murs (BFS)."""
    if trou == but:
        return 0
    vus = {trou}
    file = deque([(trou, 0)])
    while file:
        pos, d = file.popleft()
        for voisin in voisins(pos, largeur, hauteur):
            if voisin in murs or voisin in vus:
                continue
            if voisin == but:
                return d + 1
            vus.add(voisin)
            file.append((voisin, d + 1))
    return None


def bfs(trou, cible, largeur, hauteur, murs):
    """Vérification croisée : BFS sur (trou, position des données)."""
    if cible == (0, 0):
        return 0
    vus = {(trou, cible)}
    file = deque([(trou, cible, 0)])
    while file:
        trou_courant, donnees, pas = file.popleft()
        for voisin in voisins(trou_courant, largeur, hauteur):
            if voisin in murs:
                continue
            nouvelles = trou_courant if voisin == donnees else donnees
            if nouvelles == (0, 0):
                return pas + 1
            etat = (voisin, nouvelles)
            if etat in vus:
                continue
            vus.add(etat)
            file.append((voisin, nouvelles, pas + 1))
    return None


def cout_analytique(trou, cible, largeur, hauteur, murs):
    """Formule en trois termes (valable quand seul le trou peut bouger)."""
    gauche_de_la_cible = (cible[0] - 1, cible[1])
    d = distance(trou, gauche_de_la_cible, largeur, hauteur, murs)
    if d is None:
        return None
    return d + 1 + 5 * (cible[0] - 1)


def solve(lines):
    largeur, hauteur, trou, cible, murs = construire(parse_noeuds(lines))
    return cout_analytique(trou, cible, largeur, hauteur, murs)


def main():
    largeur, hauteur, trou, cible, murs = construire(parse_noeuds(read_lines()))
    print("Transferts minimaux:", cout_analytique(trou, cible, largeur, hauteur, murs))
    print("Contrôle par BFS   :", bfs(trou, cible, largeur, hauteur, murs))


if __name__ == "__main__":
    main()
