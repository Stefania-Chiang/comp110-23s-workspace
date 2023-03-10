"""Unit tests for list utility functions."""
__author__ = "730517776"


from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat
from exercises.ex05.utils import sub


def test_even_num() -> None:
    """Test only evens with even numbers."""
    test_list: list[int] = [2, 4, 6, 8]
    assert only_evens(test_list) == [2, 4, 6, 8]


def test_odd_num() -> None:
    """Test only evens with odd numbers."""
    test_list: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(test_list) == []


def test_mix_num() -> None:
    """Test only evens with mix numbers."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(test_list) == [2, 4, 6]


def test_no_num() -> None:
    """Test concat with no numbers."""
    test_list_one: list[int] = []
    test_list_two: list[int] = []
    assert concat(test_list_one, test_list_two) == []


def test_positive_num() -> None:
    """Test concat with positive numbers."""
    test_list_one: list[int] = [9, 8 ,7]
    test_list_two: list[int] = [100, 200, 300]
    assert concat(test_list_one, test_list_two) == [9, 8, 7, 100, 200, 300]


def test_negative_num() -> None:
    """Test concat with negative numbers."""
    test_list_one: list[int] = [-7, -8, -9]
    test_list_two: list[int] = [-30, -20, -10]
    assert concat(test_list_one, test_list_two) == [-7, -8, -9, -30, -20, -10]






