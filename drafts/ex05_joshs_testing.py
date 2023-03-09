"""Unit tests for list utility functions."""
__author__ = "730517776"


from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_all_odds() -> None:
    """Test with all odd ints."""
    test_list: list[int] = [-3, -5, -7, -9]
    assert only_evens(test_list) == []


def test_all_evens() -> None:
    """Test with all even ints."""
    test_list: list[int] = [-2, -4, -6, -8]
    assert only_evens(test_list) == [-2, -4, -6, -8]


def test_empty_list() -> None:
    """Test with an empty list."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_positive_ints() -> None:
    """Test with positive ints."""
    test_list1: list[int] = [1, 1, 1]
    test_list2: list[int] = [2, 2, 2]
    assert concat(test_list1, test_list2) == [1, 1, 1, 2, 2, 2]


def test_negative_ints() -> None:
    """Test with negative ints."""
    test_list1: list[int] = [-5, -7, -2, -8]
    test_list2: list[int] = [-4, -2, -6, -10]
    assert concat(test_list1, test_list2) == [-5, -7, -2, -8, -4, -2, -6, -10]


def test_both_empty() -> None:
    """Test with two empty lists."""
    test_list1: list[int] = []
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == []


def test_subset_use1() -> None:
    """Test to return a subset of the list."""
    test_list: list[int] = [100, 80, -50, -35]
    start_at_idx: int = 0
    end_at_idx: int = len(test_list)
    assert sub(test_list, start_at_idx, end_at_idx)


def test_subset_use2() -> None:
    """Test to return a subset of the list."""
    test_list: list[int] = [0, 1, 2, 3, 4, 5]
    start_at_idx: int = 1
    end_at_idx: int = 3
    assert sub(test_list, start_at_idx, end_at_idx) == [1, 2]


def test_edge_idx() -> None:
    """Test edge case."""
    test_list: list[int] = [-5, -4, -3, -2, -1]
    start_at_idx: int = -5
    end_at_idx: int = 10
    assert sub(test_list, start_at_idx, end_at_idx) == [-5, -4, -3, -2, -1]