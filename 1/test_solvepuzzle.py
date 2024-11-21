import pytest
from solvepuzzle import solve

def test_solve1():
    assert 0 == solve("(())")

def test_solve2():
    assert 0 == solve("()()")

def test_solve3():
    assert 3 == solve("(((")

def test_solve4():
    assert 3 == solve("(()(()(")

def test_solve5():
    assert 3 == solve("))(((((")

def test_solve6():
    assert -1 == solve("())")

def test_solve7():
    assert -1 == solve("))(")

def test_solve8():
    assert -3 == solve(")))")

def test_solve9():
    assert -3 == solve(")())())")
