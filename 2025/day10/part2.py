from pathlib import Path
import re
import sys

try:
    import numpy as np
    from scipy.optimize import Bounds, LinearConstraint, milp
except ModuleNotFoundError:  # dépendance optionnelle
    np = milp = None

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day10.txt"


def read_lines():
    """Renvoie les lignes de l'entrée du puzzle (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    return sys.stdin.readlines()


def parse_line(line):
    # Extract button schematics (...)
    buttons = []
    for match in re.finditer(r'\(([^)]+)\)', line):
        indices = list(map(int, match.group(1).split(',')))
        buttons.append(indices)

    # Extract joltage requirements {...}
    joltage_match = re.search(r'\{([^}]+)\}', line)
    joltage = list(map(int, joltage_match.group(1).split(',')))

    return buttons, joltage


def solve_machine(buttons, target):
    """Find minimum button presses to reach target joltage levels.

    This is an Integer Linear Programming problem:
    Minimize: sum(x_i)
    Subject to: A * x = target, x_i >= 0, x_i integer

    Where A[j][i] = 1 if button i affects counter j, else 0
    """
    if milp is None:
        raise SystemExit(
            "2025/day10/part2 nécessite scipy : pip install scipy"
        )

    n_buttons = len(buttons)
    n_counters = len(target)

    # Build constraint matrix A
    # A[counter][button] = 1 if button affects counter
    A = np.zeros((n_counters, n_buttons), dtype=float)
    for btn_idx, btn in enumerate(buttons):
        for counter_idx in btn:
            if counter_idx < n_counters:
                A[counter_idx][btn_idx] = 1

    # Objective: minimize sum of x_i
    c = np.ones(n_buttons)

    # Constraints: A * x = target
    b = np.array(target, dtype=float)

    # Use MILP solver
    constraints = LinearConstraint(A, b, b)
    bounds = Bounds(lb=0, ub=np.inf)
    integrality = np.ones(n_buttons)  # All variables are integers

    result = milp(c, constraints=constraints, bounds=bounds, integrality=integrality)

    if result.success:
        return int(round(result.fun))
    else:
        return -1


def solve(lines):
    total_presses = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        buttons, target = parse_line(line)
        presses = solve_machine(buttons, target)

        if presses == -1:
            return -1

        total_presses += presses

    return total_presses


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    result = solve(lines)
    print(result)

if __name__ == "__main__":
    main()
