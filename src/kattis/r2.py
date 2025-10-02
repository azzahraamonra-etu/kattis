def r2(n: int, average: int) -> int:
    """
    Solves the r2 problem from Kattis.
    URL: https://open.kattis.com/problems/r2

    Args:
    n (int): The first number.
    average (int): The average of two numbers.

    Returns:
    int: The second number.
    """
    return 2 * average - n
