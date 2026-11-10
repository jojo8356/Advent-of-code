"""2017, jour 10 : Knot Hash — partie 1.

Une liste circulaire de 256 nombres (0..255). Pour chaque longueur L :
  - on inverse le segment de L éléments à partir de la position courante,
  - la position avance de L + saut,
  - le saut augmente de 1.
On renvoie le produit des deux premiers éléments.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day10.txt"
TAILLE = 256


def read_texte():
    """Renvoie la ligne d'entrée brute (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    texte = path.read_text() if path.exists() else sys.stdin.read()
    return texte.strip()


def lire_longueurs(texte):
    """Longueurs de la partie 1 : les nombres séparés par des virgules."""
    return [int(x) for x in texte.split(",") if x.strip()]


def un_tour(liste, longueurs, position=0, saut=0):
    """Applique les longueurs une fois ; renvoie (liste, position, saut)."""
    n = len(liste)
    for longueur in longueurs:
        # segment circulaire : on copie les indices concernés
        indices = [(position + k) % n for k in range(longueur)]
        valeurs = [liste[i] for i in indices][::-1]
        for i, v in zip(indices, valeurs):
            liste[i] = v
        position = (position + longueur + saut) % n
        saut += 1
    return liste, position, saut


def hasher(longueurs, taille=TAILLE):
    """Liste après un tour complet."""
    liste = list(range(taille))
    liste, _, _ = un_tour(liste, longueurs)
    return liste


def solve(texte):
    liste = hasher(lire_longueurs(texte))
    return liste[0] * liste[1]


def main():
    print("Produit des deux premiers:", solve(read_texte()))


if __name__ == "__main__":
    main()
