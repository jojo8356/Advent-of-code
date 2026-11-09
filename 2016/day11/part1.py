"""2016, jour 11 : Radioisotope Thermoelectric Generators — partie 1.

Un état = (étage de l'ascenseur, positions des générateurs et des puces). On
représente chaque type (isotope) par une paire (étage du générateur, étage de
la puce) et on **canonise** l'état en triant ces paires : deux isotopes sont
interchangeables, ce qui réduit fortement l'espace de recherche.

Contraintes : un étage est sûr si, pour chaque puce non accompagnée de son
générateur, aucun autre générateur n'est présent. L'ascenseur transporte 1 ou
2 objets et ne visite que des étages existants.

Réponse : nombre minimal de trajets pour tout amener au 4ᵉ étage.
"""

from collections import deque
from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day11.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def parse_etages(lines):
    """Étages 1-indexés : {isotope: (etage_generateur, etage_puce)}."""
    generateurs, puces = {}, {}
    for numero, ligne in enumerate(lines, start=1):
        if not ligne.strip():
            continue
        for isotope, _compatible, sorte in re.findall(
            r"(\w+)(-compatible)? (generator|microchip)", ligne
        ):
            if sorte == "generator":
                generateurs[isotope] = numero
            else:
                puces[isotope] = numero
    return {isotope: (generateurs[isotope], puces[isotope]) for isotope in generateurs}


def etage_sur(objets, etage):
    """Vrai si l'étage est sûr : aucune puce « grillée » par un générateur étranger."""
    puces = [iso for iso, (g, m) in objets.items() if m == etage]
    generateurs = {iso for iso, (g, m) in objets.items() if g == etage}
    if not generateurs:
        return True  # pas de rayonnement du tout
    # une puce est protégée si son propre générateur est sur l'étage
    return all(iso in generateurs for iso in puces)


def canoniser(ascenseur, objets):
    """État canonique : paires triées (les isotopes sont interchangeables)."""
    return ascenseur, tuple(sorted(objets.values()))


def est_final(objets, dernier_etage):
    return all(g == dernier_etage and m == dernier_etage for g, m in objets.values())


def distance_minimale(objets, nb_etages=4):
    """Nombre minimal de trajets d'ascenseur pour tout monter au dernier étage."""
    ascenseur = 1
    depart = canoniser(ascenseur, objets)
    if est_final(objets, nb_etages):
        return 0

    vus = {depart}
    file = deque([(ascenseur, tuple(sorted(objets.values())), 0)])

    while file:
        etage, paires, trajets = file.popleft()
        etage = int(etage)

        # objets présents sur l'étage courant : (iso, 0 = generateur, 1 = puce)
        presents = []
        for index, (g, m) in enumerate(paires):
            if g == etage:
                presents.append((index, 0))
            if m == etage:
                presents.append((index, 1))

        # 1 ou 2 objets à transporter
        for i in range(len(presents)):
            for j in range(i, len(presents)):
                choisis = [presents[i]] if i == j else [presents[i], presents[j]]

                for direction in (-1, 1):
                    destination = etage + direction
                    if not 1 <= destination <= nb_etages:
                        continue

                    # déplacement des objets choisis
                    nouvelles = [list(paire) for paire in paires]
                    for index, type_objet in choisis:
                        nouvelles[index][type_objet] = destination
                    nouvelles = tuple(tuple(paire) for paire in nouvelles)

                    # sûreté de l'étage de départ et d'arrivée
                    objets_etat = {
                        index: (nouvelles[index][0], nouvelles[index][1])
                        for index in range(len(nouvelles))
                    }
                    if not etage_sur(objets_etat, etage):
                        continue
                    if not etage_sur(objets_etat, destination):
                        continue

                    etat = canoniser(destination, objets_etat)
                    if etat in vus:
                        continue
                    if all(g == nb_etages and m == nb_etages for g, m in etat[1]):
                        return trajets + 1
                    vus.add(etat)
                    file.append((destination, etat[1], trajets + 1))

    return None


def solve(lines, nb_etages=4):
    objets = parse_etages(lines)
    return distance_minimale(objets, nb_etages)


def main():
    print("Trajets minimaux:", solve(read_lines()))


if __name__ == "__main__":
    main()
