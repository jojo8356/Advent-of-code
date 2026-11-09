from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day12.txt"


def sum_numbers_text(text: str) -> int:
    return sum(int(n) for n in re.findall(r'-?\d+', text))


def solve(text):
    """Somme de tous les nombres présents dans le texte."""
    return sum_numbers_text(text)


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
    else:
        data = sys.stdin.read()
    print(solve(data))


if __name__ == "__main__":
    main()
