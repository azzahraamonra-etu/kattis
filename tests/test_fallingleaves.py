import pytest
from src.kattis.fallingleaves import fallingleaves

def test_single_block_star():
    # Input with only '*' as end marker
    input_lines = [
        "LLLR",
        "LRLL",
        "*"
    ]
    expected = ["LLLRLRLL"]
    assert fallingleaves(input_lines) == expected

def test_single_block_dollar():
    # Input ending with '$' stops processing
    input_lines = [
        "LRLR",
        "RLLR",
        "$"
    ]
    expected = ["LRLRRLLR"]
    assert fallingleaves(input_lines) == expected

def test_multiple_blocks():
    # Multiple blocks of lines separated by '*'
    input_lines = [
        "LL",
        "RR",
        "*",
        "LR",
        "RL",
        "*",
        "$"
    ]
    expected = ["LLRR", "LRRL"]
    assert fallingleaves(input_lines) == expected

def test_empty_input():
    # Empty input returns empty list
    input_lines = []
    expected = []
    assert fallingleaves(input_lines) == expected

def test_no_commands():
    # No '*' or '$' in input: all lines concatenated
    input_lines = ["A", "B", "C"]
    expected = []
    # Should return empty list because it waits for '*' or '$' to finalize a block
    assert fallingleaves(input_lines) == expected

def test_command_at_start():
    # Command at the start
    input_lines = ["*", "LR"]
    expected = []
    assert fallingleaves(input_lines) == expected

def test_multiple_stars_and_dollar():
    input_lines = [
        "X",
        "*",
        "Y",
        "*",
        "Z",
        "$",
        "W"
    ]
    expected = ["X", "Y", "Z"]
    assert fallingleaves(input_lines) == expected
