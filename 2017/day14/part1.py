"""2017, jour 14 : Disk Defragmentation — partie 1.

Le disque est une grille 128 × 128. La ligne `i` est le **knot hash** (jour 10)
de la chaîne `<sel>-<i>` : 32 caractères hexadécimaux = 128 bits.

Réponse : nombre total de cases utilisées (`1`).
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day14.txt"
TAILLE_GRILLE = 128
TAILLE_HASH = 256
SUFFIXE = [17, 31, 73, 47, 23]
TOURS = 64


def read_sel():
    """Renvoie le sel (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    texte = path.read_text() if path.exists() else sys.stdin.read()
    return texte.strip()


# --- knot hash (algorithme du jour 10) ------------------------------------- #
def _un_tour(liste, longueurs, position, saut):
    n = len(liste)
    for longueur in longueurs:
        indices = [(position + k) % n for k in range(longueur)]
        valeurs = [liste[i] for i in indices][::-1]
        for i, v in zip(indices, valeurs):
            liste[i] = v
        position = (position + longueur + saut) % n
        saut += 1
    return liste, position, saut


def knot_hash(texte, taille=TAILLE_HASH):
    """Knot hash complet : 64 tours, XOR par blocs de 16, hexadécimal."""
    liste = list(range(taille))
    position = saut = 0
    longueurs = [ord(c) for c in texte] + SUFFIXE
    for _ in range(TOURS):
        liste, position, saut = _un_tour(liste, longueurs, position, saut)
    blocs = []
    for debut in range(0, taille, 16):
        valeur = 0
        for v in liste[debut:debut + 16]:
            valeur ^= v
        blocs.append(valeur)
    return "".join(f"{b:02x}" for b in blocs)


# --- grille ---------------------------------------------------------------- #
def ligne_bits(sel, numero):
    """128 bits (liste de 0/1) de la ligne `numero`."""
    hexa = knot_hash(f"{sel}-{numero}")
    bits = []
    for caractere in hexa:
        valeur = int(caractere, 16)
        bits.extend((valeur >> decalage) & 1 for decalage in (3, 2, 1, 0))
    return bits


def grille(sel, taille=TAILLE_GRILLE):
    """Grille complète : liste de lignes, chaque ligne = liste de 0/1."""
    return [ligne_bits(sel, i) for i in range(taille)]


def solve(sel, taille=TAILLE_GRILLE):
    return sum(sum(ligne) for ligne in grille(sel, taille))


def main():
    print("Cases utilisées:", solve(read_sel()))


if __name__ == "__main__":
    main()
