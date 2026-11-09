from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day15.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def parse_input(lines):
    ingredients = {}
    pattern = re.compile(
        r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"
    )
    for line in lines:
        m = pattern.match(line.strip())
        if m:
            name = m.group(1)
            props = {
                "capacity": int(m.group(2)),
                "durability": int(m.group(3)),
                "flavor": int(m.group(4)),
                "texture": int(m.group(5)),
                "calories": int(m.group(6)),
            }
            ingredients[name] = props
    return ingredients


def all_combinations(total, n):
    """Génère toutes les combinaisons de n entiers >=0 qui font total"""
    if n == 1:
        yield (total,)
        return
    for i in range(total + 1):
        for tail in all_combinations(total - i, n - 1):
            yield (i,) + tail


def score_cookie(ingredients, amounts):
    totals = {"capacity": 0, "durability": 0, "flavor": 0, "texture": 0}
    for amount, (name, props) in zip(amounts, ingredients.items()):
        for key in totals:
            totals[key] += props[key] * amount
    # remplace les négatifs par 0
    for key in totals:
        totals[key] = max(0, totals[key])
    product_score = 1
    for key in totals:
        product_score *= totals[key]
    return product_score


def solve(lines):
    """Meilleur score de biscuit pour 100 cuillères d'ingrédients."""
    ingredients = parse_input(lines)
    n = len(ingredients)
    best_score = 0

    for amounts in all_combinations(100, n):
        score = score_cookie(ingredients, amounts)
        if score > best_score:
            best_score = score

    return best_score


def main():
    print(solve(read_lines()))


if __name__ == "__main__":
    main()
