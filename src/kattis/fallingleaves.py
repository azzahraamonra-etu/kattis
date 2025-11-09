"""Module for solving the fallingleaves problem from Kattis."""

def fallingleaves(input_lines: list[str]) -> list[str]:
    """
    Interleaves leaves column-wise across multiple rows. Each block is separated by '*' 
    and processing stops at '$'.
    """
    results = []
    block = []

    def process_block(b):
        """Interleave a block of rows column-wise (left→right, top→bottom)."""
        if not b:
            return ""
        interleaved = ""
        n_cols = len(b[0])
        n_rows = len(b)
        for col in range(n_cols):           # left to right
            for row in range(n_rows):       # top to bottom
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
