"""Jour 23, partie 1 : exécuter le programme assembleur avec a = 0, b = 0.

Jeu d'instructions :
  - `hlf r`      -> r = r / 2
  - `tpl r`      -> r = r * 3
  - `inc r`      -> r = r + 1
  - `jmp offset` -> saut relatif
  - `jie r, o`   -> saut si r est pair
  - `jio r, o`   -> saut si r vaut exactement 1
On renvoie la valeur du registre `b` à la fin du programme.
"""

from pathlib import Path
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day23.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def run(program, registers=None):
    """Exécute le programme et renvoie les registres finaux."""
    registers = dict(registers or {"a": 0, "b": 0})
    pc = 0  # program counter

    while 0 <= pc < len(program):
        instr = program[pc].split()
        cmd = instr[0]

        if cmd == "hlf":
            registers[instr[1]] //= 2
            pc += 1
        elif cmd == "tpl":
            registers[instr[1]] *= 3
            pc += 1
        elif cmd == "inc":
            registers[instr[1]] += 1
            pc += 1
        elif cmd == "jmp":
            pc += int(instr[1])
        elif cmd == "jie":
            registre = instr[1].rstrip(",")
            pc += int(instr[2]) if registers[registre] % 2 == 0 else 1
        elif cmd == "jio":
            registre = instr[1].rstrip(",")
            pc += int(instr[2]) if registers[registre] == 1 else 1

    return registers


def solve(lines, a=0, b=0):
    """Valeur du registre b après exécution, en partant de a et b donnés."""
    programme = [l.strip() for l in lines if l.strip()]
    return run(programme, {"a": a, "b": b})["b"]


def main():
    print("Valeur du registre b:", solve(read_lines()))


if __name__ == "__main__":
    main()
