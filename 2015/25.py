def code_at(row, col):
    n = (row + col - 2) * (row + col - 1) // 2 + col
    code = 20151125
    for _ in range(1, n):
        code = (code * 252533) % 33554393
    return code

# Exemple : remplacer row et col par ton input réel
row = 3010   # ex: row dans le puzzle
col = 3019   # ex: column dans le puzzle

print("Code à la position:", code_at(row, col))
