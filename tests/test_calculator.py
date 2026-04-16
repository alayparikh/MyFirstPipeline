import pytest
from src.calculator import add, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        divide(1, 0)