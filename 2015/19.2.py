import sys
import re
import random

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

def reverse_steps(replacements, molecule):
    # On inverse les remplacements (dst -> src)
    rev_replacements = [(b, a) for a, b in replacements]
    steps = 0
    current = molecule

    # On shuffle pour éviter les blocages
    while current != 'e':
        old = current
        for b, a in sorted(rev_replacements, key=lambda x: -len(x[0])):
            match = re.search(re.escape(b), current)
            if match:
                start = match.start()
                current = current[:start] + a + current[start+len(b):]
                steps += 1
                break
        if old == current:
            # Échec d’un remplacement -> on réessaie
            random.shuffle(rev_replacements)
            current = molecule
            steps = 0
    return steps

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()

    replacements, molecule = parse_input(lines)
    result = reverse_steps(replacements, molecule)
    print(f"Minimum number of steps to make the medicine: {result}")

if __name__ == "__main__":
    main()
