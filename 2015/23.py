# Exemple d'entrée (remplace avec ton puzzle input)
program = """jio a, +18
inc a
tpl a
inc a
tpl a
tpl a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
tpl a
tpl a
inc a
jmp +22
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7""".split("\n")

# Registres : a commence à 1 pour Part Two
# Part A
registers = {"a": 0, "b": 0}
# Part B
registers = {"a": 1, "b": 0}

pc = 0  # program counter

while 0 <= pc < len(program):
    instr = program[pc].split()
    cmd = instr[0]

    if cmd == "hlf":
        r = instr[1]
        registers[r] //= 2
        pc += 1
    elif cmd == "tpl":
        r = instr[1]
        registers[r] *= 3
        pc += 1
    elif cmd == "inc":
        r = instr[1]
        registers[r] += 1
        pc += 1
    elif cmd == "jmp":
        offset = int(instr[1])
        pc += offset
    elif cmd == "jie":
        r = instr[1].rstrip(",")
        offset = int(instr[2])
        pc += offset if registers[r] % 2 == 0 else 1
    elif cmd == "jio":
        r = instr[1].rstrip(",")
        offset = int(instr[2])
        pc += offset if registers[r] == 1 else 1

print("Valeur du registre b:", registers["b"])
