import pytest
from src.kattis.fallingleaves import fallingleaves

def test_single_block_star():
    input_lines = [
        "LLLR",
        "LRLL",
        "*"
    ]
    # Interleave columns
    # L L L R
    # L R L L
    # Interleaving columns: L L → L, L R → L, L L → L, R L → R
    expected = ["LLLRLRLL"]
    assert fallingleaves(input_lines) == expected

def test_single_block_dollar():
    input_lines = [
        "LRLR",
        "RLLR",
        "$"
    ]
    expected = ["LRLRRLLR"]
    assert fallingleaves(input_lines) == expected

def test_multiple_blocks():
    input_lines = [
        "LL",
        "RR",
        "*",
        "LR",
        "RL",
        "*",
        "$"
    ]
    expected = ["LRLR", "LRRL"]  # Interleaving columns per block
    assert fallingleaves(input_lines) == expected

def test_command_at_start():
    input_lines = ["*", "LR"]
    expected = []  # No data before first command
    assert fallingleaves(input_lines) == expected
