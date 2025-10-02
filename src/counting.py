def counting(k: int) -> list[int]:
    """
    Solves the counting problem from Kattis.
    URL: https://open.kattis.com/problems/counting

    Args:
    k (int): The multiplier.

    Returns:
    list[int]: List of the first 12 multiples of k.
    """
    return [i * k for i in range(1, 13)]
