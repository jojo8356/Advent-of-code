"""Jour 11, partie 1 : prochain mot de passe valide.

Règles :
  - lettres `a` à `z` uniquement, incrément « odomètre » (`xx` -> `xy`, `xz` -> `ya`) ;
  - au moins trois lettres consécutives croissantes (`abc`, `xyz`, ...) ;
  - aucune des lettres `i`, `o`, `l` ;
  - au moins deux paires différentes de lettres identiques (`aa`, `bb`, ...),
    sans se chevaucher (`aaa` ne compte que pour une paire).

On part du mot de passe fourni et on cherche le suivant qui respecte tout ça.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day11.txt"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
INTERDITES = set("iol")


def read_key():
    """Renvoie le mot de passe de départ (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    return sys.stdin.read().strip()


def incrementer(mot_de_passe):
    """Incrémente un mot de passe comme un odomètre (avec retenue)."""
    lettres = list(mot_de_passe)
    i = len(lettres) - 1
    while i >= 0:
        if lettres[i] == "z":
            lettres[i] = "a"
            i -= 1
        else:
            lettres[i] = ALPHABET[ALPHABET.index(lettres[i]) + 1]
            return "".join(lettres)
    return "".join(lettres)  # tout est revenu à 'a'


def a_suite_croissante(mot_de_passe):
    """Vrai s'il existe trois lettres consécutives croissantes."""
    return any(
        ALPHABET.index(mot_de_passe[i + 1]) == ALPHABET.index(mot_de_passe[i]) + 1
        and ALPHABET.index(mot_de_passe[i + 2]) == ALPHABET.index(mot_de_passe[i]) + 2
        for i in range(len(mot_de_passe) - 2)
    )


def nombre_de_paires(mot_de_passe):
    """Compte les paires distinctes de lettres identiques (sans chevauchement)."""
    total = 0
    i = 0
    while i < len(mot_de_passe) - 1:
        if mot_de_passe[i] == mot_de_passe[i + 1]:
            total += 1
            i += 2  # une paire consommée (aaa -> une seule paire)
        else:
            i += 1
    return total


def est_valide(mot_de_passe):
    if INTERDITES & set(mot_de_passe):
        return False
    if not a_suite_croissante(mot_de_passe):
        return False
    return nombre_de_paires(mot_de_passe) >= 2


def suivant(mot_de_passe):
    """Prochain mot de passe valide, en sautant les lettres interdites."""
    candidat = incrementer(mot_de_passe)
    while True:
        # optimisation : on saute directement après une lettre interdite
        for i, lettre in enumerate(candidat):
            if lettre in INTERDITES:
                prefixe = candidat[:i]
                candidat = prefixe + ALPHABET[ALPHABET.index(lettre) + 1] + "a" * (len(candidat) - i - 1)
                break
        if est_valide(candidat):
            return candidat
        candidat = incrementer(candidat)


def solve(mot_de_passe):
    return suivant(mot_de_passe)


def main():
    print(solve(read_key()))


if __name__ == "__main__":
    main()
