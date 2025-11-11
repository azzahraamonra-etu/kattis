import pytest
from fallingleaves import fallingleaves

def test_single_block():
    input_lines = [
        "ABC",
        "DEF",
        "*",
        "$"
    ]
    # Columns: (C,F), (B,E), (A,D) => interleaved bottom→top per column
    expected = ["DBEAFC"]
    assert fallingleaves(input_lines) == expected

def test_multiple_blocks():
    input_lines = [
        "ABC",
        "DEF",
        "*",
        "GHI",
        "JKL",
        "$"
    ]
    expected = ["DBEAFC", "JGLKHI"]
    assert fallingleaves(input_lines) == expected

def test_no_blocks():
    input_lines = ["$"]
    assert fallingleaves(input_lines) == []

def test_empty_block_before_dollar():
    input_lines = ["*", "$"]
    assert fallingleaves(input_lines) == []

def test_last_block_without_star():
    input_lines = [
        "AB",
        "CD",
        "$"
    ]
    expected = ["CADA"]
    # Columns: col0: D, C => bottom→top = CD; col1: B, A => bottom→top = BA => "CDBA"
    # Wait, let’s verify properly:
    # Rows: ["AB", "CD"]
    # col0: bottom→top: "C", "A"
    # col1: bottom→top: "D", "B"
    # result: "CADB"
    expected = ["CADB"]
    assert fallingleaves(input_lines) == expected
