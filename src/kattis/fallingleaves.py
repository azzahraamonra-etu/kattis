"""Module for solving the fallingleaves problem from Kattis."""

def fallingleaves(input_lines: list[str]) -> list[str]:
    """
    Interleaves leaves column-wise across multiple rows. Each block is separated by '*' 
    and processing stops at '$'.
    """
    results = []
    block = []

    def process_block(b):
        """Interleave a block of rows column-wise (each row reversed first)."""
        if not b:
            return ""
        # Reverse each line horizontally
        b = [line[::-1] for line in b]
        interleaved = ""
        n_cols = len(b[0])
        n_rows = len(b)
        for col in range(n_cols):         # left → right
            for row in range(n_rows):     # top → bottom
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
