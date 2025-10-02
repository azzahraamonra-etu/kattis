from kattis.thirteen_floors import thirteen_floors

def test_thirteen_floors():
    # Floor 13 should be skipped
    assert thirteen_floors(13) == 14

    # Floor 14 becomes 15, etc.
    assert thirteen_floors(14) == 15
    assert thirteen_floors(20) == 21

    # Floor 12 and below stay the same
    assert thirteen_floors(12) == 12
    assert thirteen_floors(1) == 1
