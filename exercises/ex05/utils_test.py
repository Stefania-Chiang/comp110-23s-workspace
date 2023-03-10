"""Unit tests for list utility functions."""
__author__ = "730517776"


from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat
from exercises.ex05.utils import sub


def test_even_num() -> None:
    """Test only evens with even numbers."""
    test_old_list: list[int] = [2, 4, 6, 8]
    assert only_evens(test_old_list) == [2, 4, 6, 8]


def test_odd_num() -> None:
    """Test only evens with odd numbers."""
    test_old_list: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(test_old_list) == []


def test_mix_num() -> None:
    """Test only evens with mix numbers."""
    test_old_list: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(test_old_list) == [2, 4, 6]


def test_no_num() -> None:
    """Test concat with no numbers."""
    test_first_list: list[int] = []
    test_second_list: list[int] = []
    assert concat(test_first_list,  test_second_list) == []


def test_positive_num() -> None:
    """Test concat with positive numbers."""
    test_first_list: list[int] = [9, 8 ,7]
    test_second_list: list[int] = [100, 200, 300]
    assert concat(test_first_list,  test_second_list) == [9, 8, 7, 100, 200, 300]


def test_negative_num() -> None:
    """Test concat with negative numbers."""
    test_first_list: list[int] = [-7, -8, -9]
    test_second_list: list[int] = [-30, -20, -10]
    assert concat(test_first_list,  test_second_list) == [-7, -8, -9, -30, -20, -10]

