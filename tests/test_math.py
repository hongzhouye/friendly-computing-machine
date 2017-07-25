"""
Tests for module math.py of fcm
"""

import friendly_computing_machine as fcm
import pytest

# test mult
test_mult_data = [
    (2, 5, 10),
    (1, 3, 3),
    (6, 9, 54),
    (0, 1, 0)
]

@pytest.mark.parametrize("a, b, expected", test_mult_data)
def test_mult(a, b, expected):
    assert fcm.mult(a, b) == expected
    assert fcm.mult(b, a) == expected

# test add
test_add_data = [
    (2, 5, 7),
    (1, 3, 4),
    (6, 9, 15),
    (0, 1, 1)
]

@pytest.mark.parametrize("a, b, expected", test_add_data)
def test_add(a, b, expected):
    assert fcm.add(a, b) == expected
    assert fcm.add(b, a) == expected

# test sub
test_sub_data = [
    (2, 5, -3),
    (1, 3, -2),
    (6, 9, -3),
    (0, 1, -1)
]

@pytest.mark.parametrize("a, b, expected", test_sub_data)
def test_add(a, b, expected):
    assert fcm.sub(a, b) == expected
