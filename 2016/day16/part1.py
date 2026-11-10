"""2016, jour 16 : Dragon Checksum — partie 1.

Remplissage par la courbe du dragon sur la graine : tant que la longueur est
inférieure à la taille du disque, on ajoute `a = a + "0" + inverse_complément(a)`.

Puis on calcule la somme de contrôle : tant que sa longueur est **paire**, on
la remplace par la comparaison deux à deux (`11` et `00` donnent `1`,
`10` et `01` donnent `0`).

Réponse : somme de contrôle pour un disque de **272** cases.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day16.txt"
TAILLE_DISQUE = 272


def read_graine():
    """Renvoie la graine du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    return sys.stdin.read().strip()


def remplir(graine, taille):
    """Étend la graine par la courbe du dragon jusqu'à couvrir `taille` cases."""
    donnees = graine
    while len(donnees) < taille:
        complement_inverse = "".join(
            "1" if bit == "0" else "0" for bit in reversed(donnees)
        )
        donnees = donnees + "0" + complement_inverse
    return donnees[:taille]


def somme_de_controle(donnees):
    """Réduit par paires jusqu'à obtenir une longueur impaire."""
    while len(donnees) % 2 == 0:
        donnees = "".join(
            "1" if donnees[i] == donnees[i + 1] else "0"
            for i in range(0, len(donnees), 2)
        )
    return donnees


def solve(graine, taille=TAILLE_DISQUE):
    return somme_de_controle(remplir(graine, taille))


def main():
    print(f"Somme de contrôle (disque de {TAILLE_DISQUE}) :", solve(read_graine()))


if __name__ == "__main__":
    main()
