from pathlib import Path
from typing import Any
import json
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day12.txt"


def sum_json_no_red(obj: Any) -> int:
    if isinstance(obj, int):
        return obj
    if isinstance(obj, float):
        return int(obj)
    if isinstance(obj, list):
        return sum(sum_json_no_red(item) for item in obj)
    if isinstance(obj, dict):
        if "red" in obj.values():
            return 0
        return sum(sum_json_no_red(v) for v in obj.values())
    return 0


def solve(data):
    """Somme JSON en ignorant tout objet qui contient la valeur "red"."""
    return sum_json_no_red(data)


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)
    print(solve(data))


if __name__ == "__main__":
    main()
