from kattis.lvable import lvable

def test_lvable():
    # Already contains "lv" → 0 ops
    assert lvable(4, "love") == 1

    # Replace one character to get "lv"
    assert lvable(4, "lave") == 1

    # Reverse "vl" to "lv"
    assert lvable(4, "vlad") == 1

    # Insert "lv" (2 ops)
    assert lvable(1, "a") == 2
