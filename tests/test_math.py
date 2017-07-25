"""
Tests for module math.py of fcm
"""

import friendly_computing_machine as fcm
import pytest

def test_mult():
    assert fcm.mult(2, 5) == 10
    assert fcm.mult(5, 2) == 10

    assert fcm.mult(2, 3) == 6
    assert fcm.mult(3, 2) == 6

test_add_data = [
    (2, 5, 7),
    (1, 3, 4),
    (6, 9, 15),
    (0, 1, 1)
]

@pytest.mark.parametrize("a, b, expected", test_add_data)
def test_add(a, b, expected):
    assert fcm.add (a, b) == expected
    assert fcm.add (b, a) == expected
