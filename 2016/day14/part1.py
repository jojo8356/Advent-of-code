"""2016, jour 14 : One-Time Pad — partie 1.

On hache `sel + n` en MD5 (n = 0, 1, 2, …). Un indice est une **clé** si son
hachage contient un **triplet** (`aaa`) et si l'un des **1 000 hachages
suivants** contient le **quintuplet** du même caractère (`aaaaa`).

Réponse : l'indice de la **64ᵉ** clé.
"""

from hashlib import md5
from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day14.txt"
FENETRE = 1000
OBJECTIF = 64


def read_key():
    """Renvoie le sel du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    return sys.stdin.read().strip()


def hacher(sel, indice, etirement=0):
    """MD5 de `sel + indice`, puis `etirement` ré-hachages de l'empreinte seule.

    Le sel n'est utilisé que pour le premier hachage. Avec l'étirement du
    puzzle (2016 ré-hachages), cela fait 2 017 hachages MD5 au total.
    """
    empreinte = md5(f"{sel}{indice}".encode()).hexdigest()
    for _ in range(etirement):
        empreinte = md5(empreinte.encode()).hexdigest()
    return empreinte


def premier_triplet(empreinte):
    """Caractère du premier groupe de trois identiques, ou None."""
    for i in range(len(empreinte) - 2):
        if empreinte[i] == empreinte[i + 1] == empreinte[i + 2]:
            return empreinte[i]
    return None


def contient_quintuplet(empreinte, caractere):
    return caractere * 5 in empreinte


def trouver_cles(sel, nombre=OBJECTIF, etirement=0, fenetre=FENETRE):
    """Indices des `nombre` premières clés, en calculant les hachages paresseusement."""
    cles = []
    hachages = {}      # indice -> empreinte (évite les recalculs)
    indice = 0

    while len(cles) < nombre:
        if indice not in hachages:
            hachages[indice] = hacher(sel, indice, etirement)

        caractere = premier_triplet(hachages[indice])
        if caractere is not None:
            for suivant in range(indice + 1, indice + fenetre + 1):
                if suivant not in hachages:
                    hachages[suivant] = hacher(sel, suivant, etirement)
                if contient_quintuplet(hachages[suivant], caractere):
                    cles.append(indice)
                    break

        # on oublie les hachages devenus inutiles
        hachages.pop(indice - fenetre - 1, None)
        indice += 1

    return cles


def solve(sel, nombre=OBJECTIF):
    """Indice de la 64ᵉ clé."""
    return trouver_cles(sel, nombre)[-1]


def main():
    print("Indice de la 64e clé:", solve(read_key()))


if __name__ == "__main__":
    main()
