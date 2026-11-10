"""2016, jour 21 : Scrambled Letters and Hash — partie 1.

Sept types d'instructions :

  - `swap position X with position Y`
  - `swap letter X with letter Y`
  - `rotate left/right N step(s)`
  - `rotate based on position of letter X`  (droite de 1 + index, +1 si index ≥ 4)
  - `reverse positions X through Y`
  - `move position X to position Y`

Réponse : `abcdefgh` brouillé par les 100 instructions.
"""

from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day21.txt"
DEPART = "abcdefgh"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def appliquer(mot, instructions):
    """Applique toutes les instructions dans l'ordre."""
    mot = list(mot)

    for instruction in instructions:
        instruction = instruction.strip()
        if not instruction:
            continue

        if m := re.match(r"swap position (\d+) with position (\d+)", instruction):
            a, b = int(m.group(1)), int(m.group(2))
            mot[a], mot[b] = mot[b], mot[a]

        elif m := re.match(r"swap letter (\w) with letter (\w)", instruction):
            a, b = mot.index(m.group(1)), mot.index(m.group(2))
            mot[a], mot[b] = mot[b], mot[a]

        elif m := re.match(r"rotate (left|right) (\d+) step", instruction):
            n = int(m.group(2)) % len(mot)
            if m.group(1) == "left":
                n = -n
            mot = mot[-n:] + mot[:-n] if n else mot

        elif m := re.match(r"rotate based on position of letter (\w)", instruction):
            index = mot.index(m.group(1))
            n = 1 + index + (1 if index >= 4 else 0)
            n %= len(mot)
            mot = mot[-n:] + mot[:-n] if n else mot

        elif m := re.match(r"reverse positions (\d+) through (\d+)", instruction):
            a, b = int(m.group(1)), int(m.group(2))
            mot[a:b + 1] = reversed(mot[a:b + 1])

        elif m := re.match(r"move position (\d+) to position (\d+)", instruction):
            a, b = int(m.group(1)), int(m.group(2))
            lettre = mot.pop(a)
            mot.insert(b, lettre)

        else:
            raise ValueError(f"instruction inconnue : {instruction}")

    return "".join(mot)


def solve(lines, depart=DEPART):
    return appliquer(depart, lines)


def main():
    print("Mot de passe brouillé:", solve(read_lines()))


if __name__ == "__main__":
    main()
