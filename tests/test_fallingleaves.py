def fallingleaves(input_lines: list[str]) -> list[str]:
    """
    Very basic stub version of fallingleaves to avoid errors.

    Args:
    input_lines (list[str]): Input lines ending with commands '*' or '$'.

    Returns:
    list[str]: Just returns a list containing concatenated lines before the command.
    """
    tree_data = []
    results = []

    for line in input_lines:
        if line in ('*', '$'):
            if tree_data:
                results.append(''.join(tree_data))
                tree_data = []
            if line == '$':
                break
        else:
            tree_data.append(line)

    return results
