"""Module for solving the Frog 1D Easy problem from Kattis."""

def frog_1d_easy(n: int, s: int, m: int, board: list[int]) -> tuple[str, int]:
    """
    Solves the 1D Frog Easy problem from Kattis.
    URL: https://open.kattis.com/problems/1dfroggereasy

    Args:
    n (int): Length of the board.
    s (int): Starting position (1-based index).
    m (int): Magic number to reach.
    board (list[int]): List representing the board.

    Returns:
    tuple[str, int]: A tuple with the outcome ("magic", "cycle", "left", or "right")
                     and the number of hops taken.
    """
    pos = s - 1  # convert to 0-based index
    hops = 0
    visited = set()

    while True:
        if board[pos] == m:
            return ("magic", hops)
        if pos in visited:
            return ("cycle", hops)
        visited.add(pos)
        move = board[pos]
        next_pos = pos + move
        hops += 1
        if next_pos < 0:
            return ("left", hops)
        if next_pos >= n:
            return ("right", hops)
        pos = next_pos
