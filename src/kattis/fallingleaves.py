"""Module for solving the fallingleaves problem from Kattis."""
def fallingleaves(input_lines: list[str]) -> list[str]:
    """
    Processes input lines representing falling leaves and returns the combined 
    strings for each tree block. Blocks are separated by '*' and processing stops at '$'.

    Args:
        input_lines (list[str]): Input lines ending with '*' (block separator) or '$' (end marker).

    Returns:
        list[str]: Each string corresponds to a concatenated tree block.
    """
    results = []
    tree_data = []

    for line in input_lines:
        if line == '*':
            if tree_data:
                results.append(''.join(tree_data))
                tree_data = []
        elif line == '$':
            if tree_data:
                results.append(''.join(tree_data))
            break
        else:
            tree_data.append(line)

    return results
