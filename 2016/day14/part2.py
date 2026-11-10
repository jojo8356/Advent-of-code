"""2016, jour 14 : One-Time Pad — partie 2.

Même recherche, mais chaque hachage est étiré : après le MD5 initial de
`sel + indice`, on re-hache **l'empreinte seule** (sans le sel) 2 016 fois,
soit 2 017 hachages au total.
"""

from pathlib import Path
import sys

from part1 import read_key, trouver_cles

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day14.txt"
ETIREMENT = 2016  # 1 hachage initial + 2016 ré-hachages = 2017 au total


def solve(sel, nombre=64):
    return trouver_cles(sel, nombre, etirement=ETIREMENT)[-1]


def main():
    print("Indice de la 64e clé (étirement 2016):", solve(read_key()))


if __name__ == "__main__":
    main()
