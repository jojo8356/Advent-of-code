"""2017, jour 20 : Particle Swarm — partie 2.

Les particules qui occupent **exactement** la même position au même tick sont
toutes détruites (y compris celles qui viennent d'arriver). Réponse : nombre de
particules restantes.

Horizon borné analytiquement plutôt que deviné : pour chaque paire, une
collision impose, sur chacun des trois axes, une équation du second degré en t
(la loi de position est `p + v t + a t(t+1)/2`). On calcule toutes les racines
entières possibles : au-delà du plus grand de ces instants, plus aucune
rencontre n'est possible, donc simuler jusque-là suffit pour être exact.
"""

from pathlib import Path
import math
import sys

from part1 import read_particules

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day20.txt"


def _racines(A, B, C):
    """Racines entières de A t² + B t + C = 0.

    Renvoie None si l'équation est une identité, sinon la liste triée des
    racines (y compris négatives).
    """
    if A == 0:
        if B == 0:
            return None
        return [(-C) // B] if (-C) % B == 0 else []
    discriminant = B * B - 4 * A * C
    if discriminant < 0:
        return []
    racine = math.isqrt(discriminant)
    if racine * racine != discriminant:
        return []
    solutions = set()
    for signe in (racine, -racine):
        numerateur = -B + signe
        if numerateur % (2 * A) == 0:
            solutions.add(numerateur // (2 * A))
    return sorted(solutions)


def horizon(particules):
    """Plus grand instant où une collision est arithmétiquement possible."""
    limite = 0
    n = len(particules)
    for i in range(n):
        for j in range(i + 1, n):
            xi, xj = particules[i], particules[j]
            instants = None
            possible = True
            for k in range(3):
                dp = xi[0][k] - xj[0][k]
                dv = xi[1][k] - xj[1][k]
                da = xi[2][k] - xj[2][k]
                racines = _racines(da, 2 * dv + da, 2 * dp)
                if racines is None:            # même axe à jamais
                    continue
                if not racines:
                    possible = False
                    break
                positifs = {t for t in racines if t >= 0}
                instants = positifs if instants is None else (instants & positifs)
                if not instants:
                    possible = False
                    break
            if possible and instants:
                limite = max(limite, max(instants))
    return limite


def simuler(particules, ticks):
    """Simule `ticks` pas et détruit les particules qui se rencontrent."""
    vivantes = list(particules)
    for _ in range(ticks + 1):
        # mise à jour de la vitesse puis de la position (semi-implicite)
        nouvelles = []
        for p, v, a in vivantes:
            v = tuple(v[k] + a[k] for k in range(3))
            p = tuple(p[k] + v[k] for k in range(3))
            nouvelles.append((p, v, a))
        vues = {}
        for index, (p, v, a) in enumerate(nouvelles):
            vues.setdefault(p, []).append(index)
        conflits = {index for indices in vues.values() if len(indices) > 1
                    for index in indices}
        vivantes = [particule for index, particule in enumerate(nouvelles)
                    if index not in conflits]
    return vivantes


def solve(particules):
    # état initial : une collision à t = 0 ne concerne que des positions
    # identiques au départ (aucune dans nos entrées), on démarre au tick 1
    limite = horizon(particules)
    return len(simuler(particules, limite))


def main():
    print("Particules restantes:", solve(read_particules()))


if __name__ == "__main__":
    main()
