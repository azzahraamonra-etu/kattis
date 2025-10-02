def popcount(n: str) -> int:
    """
    Solves the popcount problem from Kattis.
    URL: https://open.kattis.com/problems/popcount

    Args:
    n (str): Binary string input.

    Returns:
    int: Number of '1's in the string.
    """
    return n.count('1')
