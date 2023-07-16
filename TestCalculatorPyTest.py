import pytest

from Calculator import Calculator


def test_add():
    c = Calculator()
    assert c.add(1, 2) == 3


def test_subtract():
    c = Calculator()
    assert c.subtract(1, 2) == -1


def test_multiply():
    c = Calculator()
    assert c.multiply(1, 2) == 2


def test_divide():
    c = Calculator()
    assert c.divide(1, 2) == 0.5


def test_type_error():
    c = Calculator()
    with pytest.raises(TypeError):
        c.add(1, "2")
