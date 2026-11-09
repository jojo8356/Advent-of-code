"""2016, jour 5 : How About a Nice Game of Chess? — partie 1.

Le mot de passe se fabrique en hachant `sel + 0`, `sel + 1`, `sel + 2`, …
Les hachages MD5 commençant par **cinq zéros** fournissent un caractère : le
6ᵉ caractère hexadécimal du hachage. On s'arrête au 8ᵉ caractère trouvé.
"""

from hashlib import md5
from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day05.txt"
PREFIXE = "00000"


def read_key():
    """Renvoie le sel du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    return sys.stdin.read().strip()


def mot_de_passe(sel, longueur=8):
    """Mot de passe : 6ᵉ caractère des hachages qui commencent par cinq zéros."""
    resultat = []
    indice = 0

    while len(resultat) < longueur:
        empreinte = md5(f"{sel}{indice}".encode()).hexdigest()
        if empreinte.startswith(PREFIXE):
            resultat.append(empreinte[5])
        indice += 1

    return "".join(resultat)


def solve(sel):
    return mot_de_passe(sel)


def main():
    print("Password:", solve(read_key()))


if __name__ == "__main__":
    main()
