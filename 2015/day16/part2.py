from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day16.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


# Propriétés connues détectées par MFCSAM
mfcsam = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def parse_input(lines):
    sues = {}
    pattern = re.compile(r"Sue (\d+): (.+)")
    for line in lines:
        m = pattern.match(line.strip())
        if m:
            sue_number = int(m.group(1))
            props_str = m.group(2)
            props = {}
            for item in props_str.split(", "):
                key, value = item.split(": ")
                props[key] = int(value)
            sues[sue_number] = props
    return sues


def find_matching_sue(sues):
    for number, props in sues.items():
        match = True
        for key, value in props.items():
            if key in ["cats", "trees"]:
                if value <= mfcsam[key]:
                    match = False
                    break
            elif key in ["pomeranians", "goldfish"]:
                if value >= mfcsam[key]:
                    match = False
                    break
            else:
                if mfcsam[key] != value:
                    match = False
                    break
        if match:
            return number
    return None


def solve(lines):
    """Numéro de la tante Sue qui correspond au relevé."""
    sues = parse_input(lines)
    winner = find_matching_sue(sues)
    return f"The real Aunt Sue is number {winner}"


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()
