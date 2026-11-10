"""2017, jour 8 : I Heard You Like Registers — partie 1.

Chaque ligne a la forme `reg op val if reg2 cmp val2`. On exécute l'opération
uniquement si la condition est vraie, puis on renvoie la **plus grande valeur
finale** parmi tous les registres (les registres non cités valent 0 et ne
peuvent donc pas être le maximum d'une entrée entièrement négative... sauf s'ils
sont touchés, on les initialise donc à 0 explicitement).
"""

from pathlib import Path
import operator
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day08.txt"

OPERATIONS = {"inc": operator.add, "dec": operator.sub}
COMPARAISONS = {
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne,
}


def read_lines():
    """Renvoie les lignes brutes (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        return path.read_text().splitlines()
    return sys.stdin.read().splitlines()


def parse(ligne):
    """Renvoie (registre, op, valeur, reg_cond, comparaison, valeur_cond)."""
    mots = ligne.split()
    if len(mots) != 7 or mots[3] != "if":
        raise ValueError(f"ligne illisible : {ligne!r}")
    return mots[0], mots[1], int(mots[2]), mots[4], mots[5], int(mots[6])


def executer(lignes):
    """Applique toutes les instructions ; renvoie (registres, max historique)."""
    registres = {}
    maximum_vu = None
    for ligne in lignes:
        if not ligne.strip():
            continue
        reg, op, valeur, reg_cond, comp, valeur_cond = parse(ligne)
        gauche = registres.get(reg_cond, 0)
        if COMPARAISONS[comp](gauche, valeur_cond):
            registres[reg] = OPERATIONS[op](registres.get(reg, 0), valeur)
            courant = max(registres.values())
            if maximum_vu is None or courant > maximum_vu:
                maximum_vu = courant
    return registres, maximum_vu


def solve(lignes):
    registres, _ = executer(lignes)
    return max(registres.values())


def main():
    print("Plus grande valeur finale:", solve(read_lines()))


if __name__ == "__main__":
    main()
