"""Module for solving the fallingleaves problem from Kattis."""

def fallingleaves(input_lines: list[str]) -> list[str]:
    """
    Interleaves leaves column-wise across multiple rows. Each block is separated by '*'
    and processing stops at '$'.  Columns are read alternately top→bottom then
    bottom→top, starting with top→bottom.
    """
    results = []
    block = []

    def process_block(b):
        if not b:
            return ""
        interleaved = ""
        n_cols = len(b[0])
        n_rows = len(b)
        for col in range(n_cols):
            if col % 2 == 0:
                # even column: top → bottom
                for row in range(n_rows):
                    interleaved += b[row][col]
            else:
                # odd column: bottom → top
                for row in range(n_rows - 1, -1, -1):
                    interleaved += b[row][col]
        return interleaved

    for line in input_lines:
        if line == "*":
            if block:
                results.append(process_block(block))
                block = []
        elif line == "$":
            if block:
                results.append(process_block(block))
            break
        else:
            block.append(line)

    return results
