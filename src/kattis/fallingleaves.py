"""Module for solving the fallingleaves problem from Kattis."""

def fallingleaves(input_lines: list[str]) -> list[str]:
    results = []
    block = []

    for line in input_lines:
        if line == '*':
            if block:
                n_cols = len(block[0])
                n_rows = len(block)
                interleaved = ""
                for col in range(n_cols):
                    for row in range(n_rows):
                        interleaved += block[row][col]
                results.append(interleaved)
                block = []
        elif line == '$':
            if block:
                n_cols = len(block[0])
                n_rows = len(block)
                interleaved = ""
                for col in range(n_cols):
                    for row in range(n_rows):
                        interleaved += block[row][col]
                results.append(interleaved)
            break
        else:
            block.append(line)

    return results

