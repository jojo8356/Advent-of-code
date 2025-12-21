import sys


def solve(lines):
    # Remove trailing newlines but preserve spaces
    grid = [line.rstrip('\n') for line in lines]

    if not grid:
        return 0

    # Pad all lines to the same length
    max_len = max(len(line) for line in grid)
    grid = [line.ljust(max_len) for line in grid]

    rows = len(grid)
    cols = max_len

    # The last row contains the operators
    operator_row = grid[-1]

    # Find problems by looking at columns
    # Problems are separated by columns of only spaces
    problems = []
    current_problem_cols = []

    for c in range(cols):
        # Check if this column is all spaces (separator)
        is_separator = all(grid[r][c] == ' ' for r in range(rows))

        if is_separator:
            if current_problem_cols:
                problems.append(current_problem_cols)
                current_problem_cols = []
        else:
            current_problem_cols.append(c)

    if current_problem_cols:
        problems.append(current_problem_cols)

    grand_total = 0

    for prob_cols in problems:
        # Extract the operator from the last row
        operator = None
        for c in prob_cols:
            ch = operator_row[c]
            if ch in '+*':
                operator = ch
                break

        # Extract numbers from rows above the operator row
        numbers = []
        for r in range(rows - 1):
            num_str = ''.join(grid[r][c] for c in prob_cols).strip()
            if num_str:
                numbers.append(int(num_str))

        # Compute result
        if operator == '+':
            result = sum(numbers)
        elif operator == '*':
            result = 1
            for n in numbers:
                result *= n
        else:
            result = 0

        grand_total += result

    return grand_total


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
