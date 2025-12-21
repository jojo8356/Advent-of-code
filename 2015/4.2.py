import sys
import hashlib


def solve(key):
    key = key.strip()
    n = 1
    while True:
        data = f"{key}{n}".encode()
        hash_hex = hashlib.md5(data).hexdigest()
        if hash_hex.startswith("000000"):
            return n
        n += 1


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            key = f.read().strip()
    else:
        key = sys.stdin.read().strip()

    result = solve(key)
    print(result)


if __name__ == "__main__":
    main()
