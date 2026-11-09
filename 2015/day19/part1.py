from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day19.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def parse_input(lines):
    replacements = []
    molecule = ""
    for line in lines:
        line = line.strip()
        if "=>" in line:
            a, b = line.split(" => ")
            replacements.append((a, b))
        elif line:
            molecule = line
    return replacements, molecule


def generate_molecules(replacements, molecule):
    results = set()
    for src, dst in replacements:
        # trouver toutes les occurrences de src
        for match in re.finditer(f'(?={re.escape(src)})', molecule):
            start = match.start()
            new_molecule = molecule[:start] + dst + molecule[start+len(src):]
            results.add(new_molecule)
    return results


def solve(lines):
    """Nombre de molécules distinctes après un remplacement."""
    replacements, molecule = parse_input(lines)
    return len(generate_molecules(replacements, molecule))


def main():
    print("Distinct molecules after one replacement:", solve(read_lines()))


if __name__ == "__main__":
    main()
