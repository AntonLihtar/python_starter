import pytest
from tasks1.task1 import is_odd

def test_task1():
    assert is_odd(1) ==False
    assert is_odd(4) == True
    assert is_odd(7) == False
    assert is_odd(0) == True
    assert is_odd(-11) == False
    assert is_odd(-2) == True
