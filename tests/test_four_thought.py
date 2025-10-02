from kattis.four_thought import four_thought

def test_four_thought():
    results = four_thought([16])
    assert any(expr == "4 + 4 + 4 + 4 = 16" for expr in results) or \
           any(expr == "4 / 4 * 4 * 4 = 16" for expr in results)

    assert "no solution" in four_thought([12])

    # Test with multiple numbers, some solvable, some not
    results = four_thought([9, 7, 0])
    assert any("= 9" in res for res in results)
    assert any("= 7" in res or res == "no solution" for res in results)
    assert any("= 0" in res or res == "no solution" for res in results)

    # Test no solution
    assert four_thought([1000]) == ["no solution"]
