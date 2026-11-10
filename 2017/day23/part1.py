"""2017, jour 23 : Coprocessor Conflagration — partie 1.

Machine à registres (`a` à `h`, initialisés à 0) avec huit instructions :
`set`, `sub`, `mul`, `jnz` (et les inconnues ignorées).

Réponse : nombre de fois que l'instruction `mul` est exécutée.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day23.txt"


def read_lignes():
    """Renvoie les lignes brutes (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        return path.read_text().splitlines()
    return sys.stdin.read().splitlines()


def parse(lignes):
    """Renvoie [(instruction, x, y)] ; y vaut None quand il est absent."""
    programme = []
    for ligne in lignes:
        ligne = ligne.strip()
        if not ligne:
            continue
        mots = ligne.split()
        programme.append((mots[0], mots[1], mots[2] if len(mots) > 2 else None))
    return programme


def valeur(registres, jeton):
    """Opérande : registre s'il est alphabétique, sinon entier."""
    if jeton is None:
        return 0
    if jeton.lstrip("-").isdigit():
        return int(jeton)
    return registres.get(jeton, 0)


def executer(programme, a=0, limite=10_000_000):
    """Exécute le programme ; renvoie (registres, nombre de `mul` exécutés)."""
    registres = {nom: 0 for nom in "abcdefgh"}
    registres["a"] = a
    position = 0
    multiplications = 0
    pas = 0
    while 0 <= position < len(programme):
        pas += 1
        if pas > limite:
            raise RuntimeError("le programme ne s'arrête pas")
        instruction, x, y = programme[position]
        if instruction == "set":
            registres[x] = valeur(registres, y)
        elif instruction == "sub":
            registres[x] = valeur(registres, x) - valeur(registres, y)
        elif instruction == "mul":
            registres[x] = valeur(registres, x) * valeur(registres, y)
            multiplications += 1
        elif instruction == "jnz":
            if valeur(registres, x) != 0:
                position += valeur(registres, y)
                continue
        else:
            raise ValueError(f"instruction inconnue : {instruction!r}")
        position += 1
    return registres, multiplications


def solve(lignes):
    return executer(parse(lignes))[1]


def main():
    print("Multiplications exécutées:", solve(read_lignes()))


if __name__ == "__main__":
    main()
