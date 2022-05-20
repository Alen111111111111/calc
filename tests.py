import pytest
from calc import Сalc

cal = Сalc()

def test_addition():
    assert cal.add(6, 6) == 12

def test_subtraction():
    assert cal.subtract(6, 6) == 0

def test_multiplication():
    assert cal.multiply(6, 6) == 36

def test_division():
    assert cal.divide(6, 6) == 1

def test_raising_to_power():
    assert cal.raise_to_power(6, 6) == 46656




