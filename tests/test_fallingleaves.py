def fallingleaves(input_lines: list[str]) -> list[str]:
    """
    Solve the Falling Leaves problem.

    Args:
        input_lines (list[str]): Lines of leaf data ending with '*' or '$'.

    Returns:
        list[str]: Each element is a reconstructed string per block.
    """
    results = []
    block = []

    for line in input_lines:
        if line in ("*", "$"):
            if block:
                # Interleave columns of all rows in the block
                transposed = [''.join(col) for col in zip(*block)]
                results.append(''.join(transposed))
                block = []
            if line == "$":
                break
        else:
            block.append(line)

    return results
