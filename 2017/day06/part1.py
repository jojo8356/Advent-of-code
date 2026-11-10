"""2017, jour 6 : Memory Reallocation — partie 1.

À chaque cycle : on choisit le banc le plus chargé (le plus petit indice en cas
d'égalité), on vide ses blocs et on les redistribue un par un aux bancs
suivants, en bouclant. On s'arrête dès qu'une configuration déjà vue réapparaît.

Réponse : nombre de redistributions effectuées avant la répétition.
"""

from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day06.txt"


def read_bancs():
    """Renvoie la liste des blocs (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    texte = path.read_text() if path.exists() else sys.stdin.read()
    return [int(x) for x in re.findall(r"\d+", texte)]


def redistribuer(bancs):
    """Effectue un cycle sur une copie de la liste et renvoie la nouvelle liste."""
    bancs = list(bancs)
    # max() renvoie le premier indice atteignant le maximum → plus petit indice
    i = bancs.index(max(bancs))
    blocs = bancs[i]
    bancs[i] = 0
    for k in range(blocs):
        bancs[(i + 1 + k) % len(bancs)] += 1
    return bancs


def cycles(bancs):
    """Renvoie (nombre de cycles avant répétition, configuration répétée)."""
    vus = set()
    courant = tuple(bancs)
    n = 0
    while courant not in vus:
        vus.add(courant)
        courant = tuple(redistribuer(courant))
        n += 1
    return n, courant


def solve(bancs):
    return cycles(bancs)[0]


def main():
    print("Cycles avant répétition:", solve(read_bancs()))


if __name__ == "__main__":
    main()
