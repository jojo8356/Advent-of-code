from pathlib import Path
import hashlib
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day04.txt"


def solve(key):
    key = key.strip()
    n = 1
    while True:
        data = f"{key}{n}".encode()
        hash_hex = hashlib.md5(data).hexdigest()
        if hash_hex.startswith("00000"):
            return n
        n += 1


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT
    with open(path, "r", encoding="utf-8") as f:
        key = f.read().strip()

    result = solve(key)
    print(result)

if __name__ == "__main__":
    main()
