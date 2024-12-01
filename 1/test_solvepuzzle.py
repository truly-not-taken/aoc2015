import pytest
from solvepuzzle import part1
from solvepuzzle import part2

def test_part1_1():
    assert 0 == part1('(())')

def test_part1_2():
    assert 0 == part1('()()')

def test_part1_3():
    assert 3 == part1('(((')

def test_part1_4():
    assert 3 == part1('(()(()(')

def test_part1_5():
    assert 3 == part1('))(((((')

def test_part1_6():
    assert -1 == part1('())')

def test_part1_7():
    assert -1 == part1('))(')

def test_part1_8():
    assert -3 == part1(')))')

def test_part1_9():
    assert -3 == part1(')())())')

def test_part1_1000():
    assert 1000 == part1('('*1000)

def test_part2_1():
    assert 1 == part2(')')

def test_part2_2():
    assert 5 == part2('()())')
