from kattis.counting import counting

def test_counting():
    # Test with positive multiplier
    assert counting(1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert counting(2) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]

    # Test with zero multiplier
    assert counting(0) == [0] * 12

    # Test with negative multiplier
    assert counting(-1) == [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12]

    # Test with large multiplier
    assert counting(100) == [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]
