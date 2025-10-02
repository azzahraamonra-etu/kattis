"""Module for solving the 13floors problem from Kattis."""

def thirteen_floors(f1: int) -> int:
    """
    Solves the 13floors problem from Kattis.
    URL: https://open.kattis.com/problems/13floors

    Args:
        f1 (int): The floor number before adjustment.

    Returns:
        int: The adjusted floor number considering skipping floor 13.
    """
    if f1 > 12:
        return f1 + 1
    return f1
