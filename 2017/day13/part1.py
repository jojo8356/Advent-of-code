"""2017, jour 13 : Packet Scanners — partie 1.

Chaque scanner de profondeur `d` et de fenêtre `n` balaie de haut en bas puis
revient : sa position au temps `t` est `t % (2 * (n - 1))`. Il faut éviter d'être
sur la bonne profondeur au bon moment.

Réponse : somme des `d * n` des scanners qui attrapent le paquet (départ à t=0).
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day13.txt"


def read_lignes():
    """Renvoie les lignes brutes (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        return path.read_text().splitlines()
    return sys.stdin.read().splitlines()


def parse(lignes):
    """Renvoie [(profondeur, fenêtre)] trié par profondeur."""
    scanners = []
    for ligne in lignes:
        if not ligne.strip():
            continue
        gauche, droite = ligne.split(":")
        scanners.append((int(gauche), int(droite)))
    return sorted(scanners)


def periode(fenetre):
    """Période du va-et-vient : 2 * (fenêtre - 1)."""
    return 2 * (fenetre - 1)


def attrape(profondeur, fenetre, depart=0):
    """Vrai si le scanner occupe la position 0 au moment où le paquet y passe."""
    return (depart + profondeur) % periode(fenetre) == 0


def severite(scanners, depart=0):
    """Somme des d * n des collisions."""
    return sum(d * n for d, n in scanners if attrape(d, n, depart))


def solve(lignes):
    return severite(parse(lignes))


def main():
    print("Sévérité:", solve(read_lignes()))


if __name__ == "__main__":
    main()
