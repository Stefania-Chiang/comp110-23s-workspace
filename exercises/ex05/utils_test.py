"""Unit tests for list utility functions."""
__author__ = "730517776"


from exercises.ex05.utils import only_evens

def test_one_num() -> None:
    """Test a list with one number."""
    test_list: list[int] = [2]
    assert only_evens(test_list) == [2]

def test_many_num() -> None:
    """Test a list with many numbers."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(test_list) == [2, 4, 6]

def test_negative_num() -> None:
    """Test a list with negative numbers."""
    test_list: list[int] = [-7, -8, -9, -10]
    assert only_evens(test_list) == [-8, -10]

from exercises.ex05.utils import concat
