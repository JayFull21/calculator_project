import pytest

from calculator import add, subtract, multiply, divide

def test_add():
    assert add (3 ,4) == 7

def test_subtract():
    assert subtract(10,4) == 6