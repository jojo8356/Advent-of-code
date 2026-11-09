"""2016, jour 7 : Internet Protocol Version 7 — partie 1.

Une adresse a la forme `abcd[efgh]ijkl` : les segments entre crochets sont
« internes » (hypernet), les autres « externes ». Une séquence ABBA est un
palindrome de 4 caractères dont les deux du milieu sont différents
(`abba`, mais pas `aaaa`).

Une IP supporte TLS si elle contient un ABBA dans un segment **externe** et
**aucun** ABBA dans un segment interne.
"""

from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day07.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def decouper(adresse):
    """Sépare les segments externes et internes (entre crochets)."""
    adresse = adresse.strip()
    internes = re.findall(r"\[([a-z]+)\]", adresse)
    externes = re.sub(r"\[[a-z]+\]", "|", adresse).split("|")
    return externes, internes


def a_un_abba(segment):
    """Vrai si le segment contient un palindrome de 4 lettres à milieu différent."""
    for i in range(len(segment) - 3):
        a, b, c, d = segment[i:i + 4]
        if a == d and b == c and a != b:
            return True
    return False


def supporte_tls(adresse):
    externes, internes = decouper(adresse)
    if any(a_un_abba(segment) for segment in internes):
        return False
    return any(a_un_abba(segment) for segment in externes)


def solve(lines):
    """Nombre d'adresses qui supportent TLS."""
    return sum(1 for ligne in lines if ligne.strip() and supporte_tls(ligne))


def main():
    print("Adresses supportant TLS:", solve(read_lines()))


if __name__ == "__main__":
    main()
