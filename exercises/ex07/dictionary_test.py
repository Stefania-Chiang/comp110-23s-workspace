"""Unit Tests for Dictionary Functions."""
__author__ = "730517776"

from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count


def test_invert_with_positive_numbers() -> None:
    """Test invert with positive numbers."""
    test_old_dict: dict[str, str] = {"chocolate": "12", "vanilla": "8", "strawberry": "5"}
    assert invert(test_old_dict) == {"12": "chocolate", "8": "vanilla", "5": "strawberry"}


def test_count_with_positive_numbers() -> None:
    """Test count with positive numbers."""
    test_old_list: list[str] = {"chocolate", "vanilla", "strawberry", "vanilla", "chocolate"}
    assert count(test_old_list) == {"chocolate": 2, "vanilla": 2, "strawberry": 1}
    
