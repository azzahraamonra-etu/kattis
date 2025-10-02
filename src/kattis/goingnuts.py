def goingnuts(n: int) -> int:
    """
    Solves the goingnuts problem from Kattis.
    URL: https://open.kattis.com/problems/goingnuts

    Args:
    n (int): The integer input.

    Returns:
    int: The count of set bits (1s) in the binary representation of n.
    """
    return bin(n).count('1')
