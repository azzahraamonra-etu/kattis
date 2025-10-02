from kattis.fallingleaves import fallingleaves

def test_fallingleaves():
    # Example input from the problem description
    input_lines = [
        "abc",
        "def",
        "*",
        "gh",
        "*",
        "$"
    ]
    expected_output = [
        "adbecf",  # Preorder traversal after first '*'
        "gh"       # Preorder traversal after second '*'
    ]
    assert fallingleaves(input_lines) == expected_output

    # Test with no commands
    input_lines = ["abc", "def", "$"]
    expected_output = ["adbecf"]
    assert fallingleaves(input_lines) == expected_output

    # Test with only one tree and immediate $
    input_lines = ["a", "$"]
    expected_output = ["a"]
    assert fallingleaves(input_lines) == expected_output

    # Test with multiple '*' and '$'
    input_lines = [
        "a",
        "*",
        "b",
        "*",
        "$"
    ]
    expected_output = ["a", "b"]
    assert fallingleaves(input_lines) == expected_output
