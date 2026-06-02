import pytest

from calculator import add, subtract, multiply, divide

def test_add():
    assert add (3 ,4) == 7

def test_subtract():
    assert subtract(10,4) == 6

def test_divide():
    assert divide(40,2) == 20.0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5,0)

def test_multiply():
    assert multiply(6, 7) == 42