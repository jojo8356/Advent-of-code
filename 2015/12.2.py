import sys
import json
from typing import Any

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

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)
    print(sum_json_no_red(data))

if __name__ == '__main__':
    main()
