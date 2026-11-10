"""2017, jour 18 : Duet — partie 1.

Un seul programme. `snd X` joue la valeur de X ; `rcv X` la récupère **si** X
est non nul (sinon l'instruction est ignorée).

Réponse : fréquence récupérée par le premier `rcv` qui déclenche.

Attention au parsing : `i` est ici un **registre** (ce sont les noms de registres
qui sont des lettres), tandis que `jgz 1 3` porte un littéral.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day18.txt"


def read_lignes():
    """Renvoie les lignes brutes (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        return path.read_text().splitlines()
    return sys.stdin.read().splitlines()


def parse(lignes):
    """Renvoie une liste de tuples (instruction, x, y|None)."""
    programme = []
    for ligne in lignes:
        if not ligne.strip():
            continue
        mots = ligne.split()
        programme.append((mots[0], mots[1], mots[2] if len(mots) > 2 else None))
    return programme


def valeur(registres, jeton):
    """Valeur d'un opérande : un registre s'il est alphabétique, sinon un entier."""
    if jeton is None:
        return 0
    if jeton.lstrip("-").isdigit():
        return int(jeton)
    return registres.get(jeton, 0)


def executer(programme):
    """Joue le programme jusqu'au premier `rcv` déclenché ; renvoie la fréquence."""
    registres = {}
    position = 0
    son = 0
    while 0 <= position < len(programme):
        instruction, x, y = programme[position]
        if instruction == "snd":
            son = valeur(registres, x)
        elif instruction == "set":
            registres[x] = valeur(registres, y)
        elif instruction == "add":
            registres[x] = valeur(registres, x) + valeur(registres, y)
        elif instruction == "mul":
            registres[x] = valeur(registres, x) * valeur(registres, y)
        elif instruction == "mod":
            diviseur = valeur(registres, y)
            registres[x] = valeur(registres, x) % diviseur
        elif instruction == "jgz":
            if valeur(registres, x) > 0:
                position += valeur(registres, y)
                continue
        elif instruction == "rcv":
            if valeur(registres, x) != 0:
                return son
        else:
            raise ValueError(f"instruction inconnue : {instruction!r}")
        position += 1
    raise ValueError("le programme s'est terminé sans récupération")


def solve(lignes):
    return executer(parse(lignes))


def main():
    print("Fréquence récupérée:", solve(read_lignes()))


if __name__ == "__main__":
    main()
