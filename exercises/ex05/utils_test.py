"""Unit tests for list utility functions."""
__author__ = "730517776"


from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat
from exercises.ex05.utils import sub


def test_only_evens_with_even_num() -> None:
    """Test only evens with even numbers."""
    test_old_list: list[int] = [2, 4, 6, 8]
    assert only_evens(test_old_list) == [2, 4, 6, 8]


def test_only_evens_with_odd_num() -> None:
    """Test only evens with odd numbers."""
    test_old_list: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(test_old_list) == []


def test_only_evens_with_no_num() -> None:
    """Test only evens with no number."""
    test_old_list: list[int] = []
    assert only_evens(test_old_list) == []


def test_concat_with_positive_num() -> None:
    """Test concat with positive numbers."""
    test_first_list: list[int] = [9, 8 ,7]
    test_second_list: list[int] = [100, 200, 300]
    assert concat(test_first_list,  test_second_list) == [9, 8, 7, 100, 200, 300]


def test_concat_with_negative_num() -> None:
    """Test concat with negative numbers."""
    test_first_list: list[int] = [-7, -8, -9]
    test_second_list: list[int] = [-30, -20, -10]
    assert concat(test_first_list,  test_second_list) == [-7, -8, -9, -30, -20, -10]


def test_concat_with_no_num() -> None:
    """Test concat with no number."""
    test_first_list: list[int] = []
    test_second_list: list[int] = []
    assert concat(test_first_list,  test_second_list) == []


def test_sub_with_one_num() -> None:
    """Test sub with one number."""
    test_given_list: list[int] = [50]
    test_start_index: int = 0
    test_end_index: int = 1
    assert sub(test_given_list, test_start_index, test_end_index) == [50]


def test_sub_with_many_num() -> None:
    """Test sub with many numbers."""
    test_given_list: list[int]= [19, 17, 15, 13, 11]
    test_start_index: int = 2
    test_end_index: int = 4
    assert sub(test_given_list, test_start_index, test_end_index) == [15, 13]


def test_sub_with_no_num() -> None:
    """Test sub with no number."""
    test_given_list: list[int]= []
    test_start_index: int = 3
    test_end_index: int = 5
    assert sub(test_given_list, test_start_index, test_end_index) == []