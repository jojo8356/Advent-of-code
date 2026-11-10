"""2016, jour 23 : Safe Cracking — partie 1.

Assembleur à quatre registres avec l'instruction `tgl x` : elle modifie
l'instruction située `x` lignes plus loin (x peut être un registre) :

  - `inc` devient `dec`, et inversement ;
  - `jnz` devient `cpy`, et inversement ;
  - toute autre instruction (`cpy`, `tgl`, …) devient `inc`.

`tgl` peut donc modifier le programme lui-même, y compris des `tgl` à venir.

Trois motifs de boucles sont exécutés d'un coup (même résultat, coût constant) :

  - `cpy X c / inc a / dec c / jnz c -2 / dec d / jnz d -5`
      -> `a += X × d` (multiplication)
  - `inc x / dec y / jnz y -2`  ->  `x += y ; y = 0`
  - `dec x / jnz x -2`          ->  `x = 0`

Sans eux, la partie 2 (`a = 12`) demanderait de dérouler `12!` ≈ 4,8 × 10^8
itérations et ne terminerait pas.

Réponse : valeur du registre `a` (départ `a = 7` pour la partie 1).
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day23.txt"
REGISTRES = ("a", "b", "c", "d")
LIMITE = 50_000_000


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def parse_programme(lines):
    """Découpe chaque instruction en liste de jetons."""
    return [ligne.split() for ligne in lines if ligne.strip()]


def valeur(argument, registres):
    """Valeur d'un opérande : entier littéral ou contenu d'un registre."""
    if argument in registres:
        return registres[argument]
    return int(argument)


def est_multiplication(code, pc, registres):
    """Motif `cpy X c / inc a / dec c / jnz c -2 / dec d / jnz d -5` ?"""
    if pc + 5 >= len(code) or code[pc][0] != "cpy":
        return False
    compte = code[pc][2]
    if code[pc + 1] != ["inc", "a"]:
        return False
    if code[pc + 2][0] != "dec" or code[pc + 2][1] != compte:
        return False
    if code[pc + 3] != ["jnz", compte, "-2"]:
        return False
    if code[pc + 4][0] != "dec":
        return False
    if code[pc + 5] != ["jnz", code[pc + 4][1], "-5"]:
        return False
    return registres[code[pc + 4][1]] > 0


def executer(programme, registres=None, limite=LIMITE):
    """Exécute le programme (avec `tgl`) et renvoie les registres finaux."""
    registres = dict(registres or {r: 0 for r in REGISTRES})
    code = [list(instruction) for instruction in programme]
    pointeur = 0
    pas = 0

    while 0 <= pointeur < len(code):
        pas += 1
        if pas > limite:
            raise RuntimeError("boucle infinie ?")

        instruction = code[pointeur]
        nom = instruction[0]

        # --- motif multiplication : la boucle devient a += X × d ---
        if est_multiplication(code, pointeur, registres):
            compteur = code[pointeur + 4][1]
            registres["a"] += valeur(instruction[1], registres) * registres[compteur]
            registres[instruction[2]] = 0
            registres[compteur] = 0
            pointeur += 6
            continue

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

        elif nom == "tgl":
            cible = pointeur + valeur(instruction[1], registres)
            if 0 <= cible < len(code):
                modifiee = code[cible]
                if len(modifiee) == 2:   # inc <-> dec
                    modifiee[0] = {"inc": "dec", "dec": "inc"}.get(modifiee[0], "inc")
                else:                    # jnz <-> cpy
                    modifiee[0] = {"jnz": "cpy", "cpy": "jnz"}.get(modifiee[0], "inc")
            pointeur += 1

        else:
            raise ValueError(f"instruction inconnue : {instruction}")

    return registres


def solve(lines, a=7):
    """Valeur du registre a après exécution."""
    registres = {r: 0 for r in REGISTRES}
    registres["a"] = a
    return executer(parse_programme(lines), registres)["a"]


def main():
    print("Valeur du registre a (a=7):", solve(read_lines()))


if __name__ == "__main__":
    main()
