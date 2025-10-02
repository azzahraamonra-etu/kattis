def lvable(n: int, s: str) -> int:
    """
    Solves the Lvable problem from Kattis.
    URL: https://open.kattis.com/problems/lvable

    Args:
    n (int): Length of the string s.
    s (str): The input string.

    Returns:
    int: The minimum number of operations to make the string contain "lv".
    """
    # Case 1: Already contains "lv"
    if "lv" in s:
        return 0

    min_ops = float('inf')

    # Case 2: Can we replace one character to make "lv"?
    for i in range(n - 1):
        a, b = s[i], s[i+1]
        cost = 0
        if a != 'l':
            cost += 1
        if b != 'v':
            cost += 1
        min_ops = min(min_ops, cost)

    # Case 3: Can we reverse "vl" to make "lv"?
    if "vl" in s:
        min_ops = min(min_ops, 1)

    # Case 4: Insert "lv" (always takes 2 operations)
    min_ops = min(min_ops, 2)

    return min_ops
