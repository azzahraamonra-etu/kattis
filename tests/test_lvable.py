from kattis.lvable import lvable

def test_lvable():
    # Case 1: Already contains "lv" → 0 ops
    # "love" does NOT contain substring "lv", but can be fixed with 1 replacement
    assert lvable(4, "love") == 1

    assert lvable(2, "lv") == 0

    # Case 2: Replace one character to get "lv"
    assert lvable(4, "lave") == 1  # Replace 'a' with 'v'
    assert lvable(4, "llve") == 0  # Replace 2nd 'l' with 'v'

    # Case 3: Reverse "vl" to "lv" (1 operation)
    assert lvable(4, "vlad") == 1
    assert lvable(3, "vla") == 1
    assert lvable(2, "vl") == 1

    # Case 4: Insert "lv" (2 ops)
    assert lvable(1, "a") == 2
    assert lvable(0, "") == 2

    # Edge cases
    assert lvable(1, "l") == 2
    assert lvable(1, "v") == 2
