"""Module for solving the four_thought problem from Kattis."""

from itertools import product

def four_thought(test_cases: list[int]) -> list[str]:
    """
    Solves the 4thought problem from Kattis.
    URL: https://open.kattis.com/problems/4thought

    Args:
    test_cases (list[int]): List of integers to solve for.

    Returns:
    list[str]: List of strings with either the expression that equals
               the number or "no solution" if none exists.
    """
    ops = ["+", "-", "*", "/"]
    expr_map = {}

    # Precompute all possible expressions using 4 fours and the four ops
    for o1, o2, o3 in product(ops, repeat=3):
        expr = f"4 {o1} 4 {o2} 4 {o3} 4"
        try:
            # Evaluate with integer division for '/'
            result = eval(expr.replace("/", "//"))
            expr_map[result] = expr
        except ZeroDivisionError:
            continue

    results = []
    for n in test_cases:
        if n in expr_map:
            results.append(f"{expr_map[n]} = {n}")
        else:
            results.append("no solution")
    return results
