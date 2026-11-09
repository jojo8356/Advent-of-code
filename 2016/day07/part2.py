"""2016, jour 7 : Internet Protocol Version 7 — partie 2.

Une adresse supporte SSL si un segment **externe** contient une séquence ABA
(`xyx`, x ≠ y) et qu'un segment **interne** contient la séquence BAB
correspondante (`yxy`). Exemple : `aba[bab]xyz` supporte SSL.
"""

from pathlib import Path
import sys

from part1 import decouper, read_lines

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day07.txt"


def sequences(segment, externe=True):
    """Séquences ABA (externes) ou BAB (internes) du segment."""
    trouvees = set()
    for i in range(len(segment) - 2):
        a, b, c = segment[i:i + 3]
        if a == c and a != b:
            # ABA externe -> on cherche BAB interne, et réciproquement
            trouvees.add((a, b) if externe else (b, a))
    return trouvees


def supporte_ssl(adresse):
    externes, internes = decouper(adresse)
    aba = set()
    for segment in externes:
        aba |= sequences(segment, externe=True)
    if not aba:
        return False
    bab = set()
    for segment in internes:
        bab |= sequences(segment, externe=False)
    return bool(aba & bab)


def solve(lines):
    """Nombre d'adresses qui supportent SSL."""
    return sum(1 for ligne in lines if ligne.strip() and supporte_ssl(ligne))


def main():
    print("Adresses supportant SSL:", solve(read_lines()))


if __name__ == "__main__":
    main()
