"""2016, jour 12 : Leonardo's Monorail — partie 1.

Petit assembleur à quatre registres (a, b, c, d) :

  - `cpy x y` : copie la valeur (registre ou entier) x dans le registre y ;
  - `inc x`   : incrémente le registre x ;
  - `dec x`   : décrémente le registre x ;
  - `jnz x y` : saute de y instructions si x (registre ou entier) ≠ 0.

Deux motifs de boucles très fréquents sont exécutés en une seule fois, sans
changer le résultat :

  - `inc x / dec y / jnz y -2`  ->  x += y ; y = 0   (si y > 0)
  - `dec x / jnz x -2`          ->  x = 0            (si x > 0)

Réponse : valeur du registre `a` à la fin du programme (tous registres à 0).
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day12.txt"
REGISTRES = ("a", "b", "c", "d")
LIMITE = 50_000_000  # garde-fou contre une boucle infinie


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


def executer(programme, registres=None, limite=LIMITE):
    """Exécute le programme et renvoie les registres finaux."""
    registres = dict(registres or {r: 0 for r in REGISTRES})
    code = [ligne.split() for ligne in programme if ligne.strip()]
    pointeur = 0
    pas = 0

    while 0 <= pointeur < len(code):
        pas += 1
        if pas > limite:
            raise RuntimeError("boucle infinie ?")

        instruction = code[pointeur]
        nom = instruction[0]

        # --- motif `inc x / dec y / jnz y -2` ---
        if (
            nom == "inc"
            and pointeur + 2 < len(code)
            and code[pointeur + 1][0] == "dec"
            and code[pointeur + 2] == ["jnz", code[pointeur + 1][1], "-2"]
            and registres[code[pointeur + 1][1]] > 0
        ):
            registres[instruction[1]] += registres[code[pointeur + 1][1]]
            registres[code[pointeur + 1][1]] = 0
            pointeur += 3
            continue

        # --- motif `dec x / jnz x -2` ---
        if (
            nom == "dec"
            and pointeur + 1 < len(code)
            and code[pointeur + 1] == ["jnz", instruction[1], "-2"]
            and registres[instruction[1]] > 0
        ):
            registres[instruction[1]] = 0
            pointeur += 2
            continue

        if nom == "cpy":
            cible = instruction[2]
            if cible in registres:  # `cpy x 5` est invalide : on l'ignore
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
        else:
            raise ValueError(f"instruction inconnue : {instruction}")

    return registres


def solve(lines, registres=None):
    """Valeur du registre a après exécution."""
    return executer(lines, registres)["a"]


def main():
    print("Valeur du registre a:", solve(read_lines()))


if __name__ == "__main__":
    main()
