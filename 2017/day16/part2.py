"""2017, jour 16 : Permutation Promenade — partie 2.

Un milliard de danses. Une danse est une permutation d'un ensemble fini : la
suite des états est donc **périodique**. On enregistre l'état après `k` danses ;
dès qu'un état réapparaît au rang `m`, la période vaut `m - k`. Il ne reste qu'à
effectuer `1e9 mod periode` danses de plus depuis cet état.
"""

from pathlib import Path
import sys

from part1 import read_mouvements, danser, PROGRAMMES

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day16.txt"
DANSES = 1_000_000_000


def ordre_apres(mouvements, danses=DANSES, depart=PROGRAMMES):
    """Ordre après `danses` danses, en exploitant la périodicité."""
    vus = {}                       # état -> rang (nombre de danses effectuées)
    etat = depart
    rang = 0
    while etat not in vus:
        vus[etat] = rang
        etat = danser(etat, mouvements)
        rang += 1
    # l'état s'est répété : rang = première réapparition
    periode = rang - vus[etat]
    debut = vus[etat]
    # danses restantes à faire depuis `etat` (qui est l'état au rang `rang`)
    restantes = (danses - rang) % periode
    for _ in range(restantes):
        etat = danser(etat, mouvements)
    return etat


def solve(mouvements, danses=DANSES):
    return ordre_apres(mouvements, danses)


def main():
    print("Ordre après 1 milliard de danses:", solve(read_mouvements()))


if __name__ == "__main__":
    main()
