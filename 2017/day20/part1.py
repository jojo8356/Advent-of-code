"""2017, jour 20 : Particle Swarm — partie 1.

Chaque particule a une position `p`, une vitesse `v` et une accélération `a`.
À chaque tick : `v += a` puis `p += v` (mise à jour semi-implicite).

Réponse : indice (0-based) de la particule **la plus proche de l'origine à long
terme**.

Le piège est de chercher le minimum de distance au cours du temps : ce n'est pas
la question. À long terme, c'est l'accélération qui décide — la distance croît
en `|a| t²/2`. On classe donc par :
  1. norme de l'accélération,
  2. puis `a·v` (une vitesse qui s'oppose à l'accélération retarde l'éloignement),
  3. puis norme de la vitesse,
  4. puis distance initiale.
La particule de norme d'accélération strictement minimale gagne toujours.
"""

from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day20.txt"
MOTIF = re.compile(r"p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, "
                   r"a=<(-?\d+),(-?\d+),(-?\d+)>")


def read_particules():
    """Renvoie une liste de (p, v, a), chaque terme étant un triplet."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    texte = path.read_text() if path.exists() else sys.stdin.read()
    particules = []
    for ligne in texte.splitlines():
        m = MOTIF.search(ligne)
        if not m:
            continue
        nombres = [int(x) for x in m.groups()]
        particules.append((tuple(nombres[0:3]), tuple(nombres[3:6]), tuple(nombres[6:9])))
    return particules


def position(particule, t):
    """Position de la particule au temps t (mise à jour semi-implicite)."""
    p, v, a = particule
    return tuple(p[i] + v[i] * t + a[i] * t * (t + 1) // 2 for i in range(3))


def distance(particule, t):
    """Distance de Manhattan à l'origine au temps t."""
    return sum(abs(c) for c in position(particule, t))


def cle_eloignement(particule):
    """Ordre de priorité à long terme : petite accélération d'abord."""
    p, v, a = particule
    return (sum(c * c for c in a),                      # 1. norme de a
            sum(a[i] * v[i] for i in range(3)),         # 2. a·v
            sum(c * c for c in v),                      # 3. norme de v
            sum(abs(c) for c in p))                     # 4. distance initiale


def solve(particules):
    """Indice de la particule la plus proche à long terme."""
    return min(range(len(particules)), key=lambda i: cle_eloignement(particules[i]))


def main():
    print("Particule la plus proche:", solve(read_particules()))


if __name__ == "__main__":
    main()
