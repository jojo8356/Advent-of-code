"""2016, jour 25 : Clock Signal — partie 1.

Programme assembleur (`cpy`, `inc`, `dec`, `jnz`) auquel s'ajoute `out x` :
chaque `out` émet la valeur de `x`. On cherche le **plus petit `a` positif**
tel que la sortie commence par `0, 1, 0, 1, 0, 1, …` indéfiniment.

On exécute chaque candidat et l'on s'arrête dès qu'un `out` ne respecte pas
l'alternance attendue. Un candidat valide sur un grand nombre de sorties
(ici 100) est accepté : le programme est un compteur en base 2 modifié, sa
période est très courte, donc 100 sorties correctes excluent une erreur.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day25.txt"
REGISTRES = ("a", "b", "c", "d")
SORTIES_TESTEES = 100
LIMITE_PAS = 2_000_000


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def valeur(argument, registres):
    """Valeur d'un opérande : entier littéral ou contenu d'un registre."""
    if argument in registres:
        return registres[argument]
    return int(argument)


def signal_valide(programme, a, sorties=SORTIES_TESTEES, limite=LIMITE_PAS):
    """Exécute le programme et vérifie l'alternance 0, 1, 0, 1, …"""
    registres = {r: 0 for r in REGISTRES}
    registres["a"] = a
    code = [list(instruction) for instruction in programme]
    pointeur = 0
    pas = 0
    attendu = 0
    emises = 0

    while 0 <= pointeur < len(code):
        pas += 1
        if pas > limite:
            return False
        instruction = code[pointeur]
        nom = instruction[0]

        if nom == "cpy":
            cible = instruction[2]
            if cible in registres:
                registres[cible] = valeur(instruction[1], registres)
            pointeur += 1
        elif nom == "inc":
            registres[instruction[1]] += 1
            pointeur += 1
        elif nom == "dec":
            registres[instruction[1]] -= 1
            pointeur += 1
        elif nom == "jnz":
            if valeur(instruction[1], registres) != 0:
                pointeur += valeur(instruction[2], registres)
            else:
                pointeur += 1
        elif nom == "out":
            if valeur(instruction[1], registres) != attendu:
                return False
            emises += 1
            if emises >= sorties:
                return True
            attendu ^= 1
            pointeur += 1
        else:
            raise ValueError(f"instruction inconnue : {instruction}")

    return False  # programme terminé sans avoir émis assez de sorties


def solve(lines, maximum=100_000):
    """Plus petit a > 0 dont la sortie alterne 0, 1, 0, 1, …"""
    programme = [ligne.split() for ligne in lines if ligne.strip()]
    for a in range(1, maximum + 1):
        if signal_valide(programme, a):
            return a
    return None


def main():
    print("Plus petit a produisant 0,1,0,1,… :", solve(read_lines()))


if __name__ == "__main__":
    main()
