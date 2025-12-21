import sys
import re
from itertools import product


def parse_line(line):
    # Extract indicator diagram [...]
    diagram_match = re.search(r'\[([.#]+)\]', line)
    diagram = diagram_match.group(1)
    target = [1 if c == '#' else 0 for c in diagram]
    n_lights = len(target)

    # Extract button schematics (...)
    buttons = []
    for match in re.finditer(r'\(([^)]+)\)', line):
        indices = list(map(int, match.group(1).split(',')))
        buttons.append(indices)

    return n_lights, target, buttons


def solve_machine(n_lights, target, buttons):
    """Find minimum button presses to reach target configuration.

    This is a system of linear equations over GF(2).
    We need to find x_i in {0,1} such that sum(button_i * x_i) = target (mod 2)
    and minimize sum(x_i).

    Since pressing a button twice cancels out, we only need to consider 0 or 1 presses.
    """
    n_buttons = len(buttons)

    if n_buttons <= 20:
        # Brute force for small number of buttons
        min_presses = float('inf')

        for mask in range(1 << n_buttons):
            state = [0] * n_lights
            presses = 0

            for i in range(n_buttons):
                if mask & (1 << i):
                    presses += 1
                    for idx in buttons[i]:
                        state[idx] ^= 1

            if state == target:
                min_presses = min(min_presses, presses)

        return min_presses if min_presses != float('inf') else -1
    else:
        # Gaussian elimination for larger systems
        return solve_gaussian(n_lights, target, buttons)


def solve_gaussian(n_lights, target, buttons):
    """Solve using Gaussian elimination over GF(2) with minimum weight solution."""
    n_buttons = len(buttons)

    # Build augmented matrix [A | b] where A*x = b (mod 2)
    # Rows = lights, Cols = buttons + 1 (for target)
    matrix = []
    for light in range(n_lights):
        row = []
        for btn_idx, btn in enumerate(buttons):
            row.append(1 if light in btn else 0)
        row.append(target[light])
        matrix.append(row)

    # Gaussian elimination
    pivot_col = 0
    pivot_rows = []

    for row in range(n_lights):
        if pivot_col >= n_buttons:
            break

        # Find pivot
        pivot_row = None
        for r in range(row, n_lights):
            if matrix[r][pivot_col] == 1:
                pivot_row = r
                break

        if pivot_row is None:
            pivot_col += 1
            continue

        # Swap rows
        matrix[row], matrix[pivot_row] = matrix[pivot_row], matrix[row]
        pivot_rows.append((row, pivot_col))

        # Eliminate
        for r in range(n_lights):
            if r != row and matrix[r][pivot_col] == 1:
                for c in range(n_buttons + 1):
                    matrix[r][c] ^= matrix[row][c]

        pivot_col += 1

    # Check for inconsistency
    for row in range(n_lights):
        all_zero = all(matrix[row][c] == 0 for c in range(n_buttons))
        if all_zero and matrix[row][n_buttons] == 1:
            return -1  # No solution

    # Find free variables
    pivot_cols = set(pc for _, pc in pivot_rows)
    free_vars = [c for c in range(n_buttons) if c not in pivot_cols]

    # Try all combinations of free variables to find minimum weight solution
    min_presses = float('inf')

    for free_vals in product([0, 1], repeat=len(free_vars)):
        # Set free variables
        solution = [0] * n_buttons
        for i, fv in enumerate(free_vars):
            solution[fv] = free_vals[i]

        # Back-substitute to find pivot variables
        valid = True
        for row_idx, pivot_c in reversed(pivot_rows):
            val = matrix[row_idx][n_buttons]
            for c in range(n_buttons):
                if c != pivot_c:
                    val ^= matrix[row_idx][c] * solution[c]
            solution[pivot_c] = val

        # Verify and count
        state = [0] * n_lights
        for i, s in enumerate(solution):
            if s:
                for idx in buttons[i]:
                    state[idx] ^= 1

        if state == target:
            presses = sum(solution)
            min_presses = min(min_presses, presses)

    return min_presses if min_presses != float('inf') else -1


def solve(lines):
    total_presses = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        n_lights, target, buttons = parse_line(line)
        presses = solve_machine(n_lights, target, buttons)

        if presses == -1:
            return -1  # No solution

        total_presses += presses

    return total_presses


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()

    result = solve(lines)
    print(result)


if __name__ == "__main__":
    main()
