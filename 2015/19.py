import sys
import re

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

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()

    replacements, molecule = parse_input(lines)
    molecules = generate_molecules(replacements, molecule)
    print(f"Distinct molecules after one replacement: {len(molecules)}")

if __name__ == "__main__":
    main()
