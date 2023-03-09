"""Unit tests for list utility functions."""
__author__ = "730517776"

from exercises.ex05.utils import only_evens

def test_one_num() -> None:
    test_list: list[int] = [2]
    assert only_evens(test_list) == [2]

def test_many_num() -> None:
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(test_list) == [2, 4, 6]
