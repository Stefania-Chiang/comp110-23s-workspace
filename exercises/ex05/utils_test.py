"""Unit tests for list utility functions."""
__author__ = "730517776"


from exercises.ex05.utils import only_evens


"""Test a list with one number."""
def test_one_num() -> None:
    test_list: list[int] = [2]
    assert only_evens(test_list) == [2]


"""Test a list with many numbers."""
def test_many_num() -> None:
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(test_list) == [2, 4, 6]


"""Test a list with negative numbers."""
def test_negative_num() -> None:
    test_list: list[int] = [-7, -8, -9, -10]
    assert only_evens(test_list) == [-8, -10]

from exercises.ex05.utils import concat
