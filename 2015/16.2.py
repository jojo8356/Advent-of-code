import sys
import re

# Valeurs détectées par MFCSAM
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
    "perfumes": 1
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

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()

    sues = parse_input(lines)
    winner = find_matching_sue(sues)
    print(f"The real Aunt Sue is number {winner}")

if __name__ == "__main__":
    main()
