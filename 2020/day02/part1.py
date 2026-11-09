from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day02.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def get_variables(line):
    mini, maxi = line.split(" ")[0].split("-")
    letter = line.split(" ")[1].replace(":", "")
    text = line.split(" ")[-1]
    return float(mini), float(maxi), letter, text


def solve(lines):
    """Nombre de mots de passe valides (au moins mini et au plus maxi occurrences)."""
    n = 0
    for line in lines:
        if not line.strip():
            continue
        mini, maxi, letter, text = get_variables(line)
        if mini <= text.count(letter) <= maxi:
            n += 1
    return n


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()
