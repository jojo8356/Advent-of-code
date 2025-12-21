# sum_numbers_regex.py
import sys
import re

def sum_numbers_text(text: str) -> int:
    return sum(int(n) for n in re.findall(r'-?\d+', text))

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            data = f.read()
    else:
        data = sys.stdin.read()
    print(sum_numbers_text(data))

if __name__ == '__main__':
    main()
