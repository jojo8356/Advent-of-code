"""2017, jour 9 : Stream Processing — partie 2.

Nombre de caractères à l'intérieur des déchets, **non annulés** (les `!` et le
caractère qu'ils neutralisent ne comptent pas, pas plus que les `<` `>`).
"""

from pathlib import Path
import sys

from part1 import read_stream, analyser

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day09.txt"


def solve(flux):
    return analyser(flux)[1]


def main():
    print("Caractères de déchet:", solve(read_stream()))


if __name__ == "__main__":
    main()
