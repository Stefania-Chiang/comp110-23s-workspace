"""Unit Tests for Dictionary Functions."""
__author__ = "730517776"


from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count


def test_invert_with_words() -> None:
    """Test invert with all words in the strings."""
    test_old_dict: dict[str, str] = {"chocolate": "blueberry", "vanilla": "oreo", "strawberry": "banana"}
    assert invert(test_old_dict) == {"blueberry": "chocolate", "oreo": "vanilla", "banana": "strawberry"}


def test_invert_with_numbers() -> None:
    """Test invert with all numbers in the strings."""
    test_old_dict: dict[str, str] = {"13": "12", "15": "8", "7": "5"}
    assert invert(test_old_dict) == {"12": "13", "8": "15", "5": "7"}


def test_invert_with_empty() -> None:
    """Test invert with an empty dictionary."""
    test_old_dict: dict[str, str] = {}
    assert invert(test_old_dict) == {}


def test_favorite_color_with_different() -> None:
    """Test favorite color with all different color."""
    test_old_dict: dict[str, str] = {"Josh": "blue", "Martina": "red", "Sophia": "green", "Betty": "yellow"}
    assert favorite_color(test_old_dict) == "blue"


def test_favorite_color_with_same() -> None:
    """Test favorite color with all same color."""
    test_old_dict: dict[str, str] = {"Josh": "red", "Martina": "red", "Sophia": "red", "Betty": "red"}
    assert favorite_color(test_old_dict) == "red"


def test_favorite_color_with_empty() -> None:
    """Test favorite color with an empty dictionary."""
    test_old_dict: dict[str, str] = {}
    assert favorite_color(test_old_dict) == ""


def test_count_with_different() -> None:
    """Test count with all different strings."""
    test_old_list: list[str] = ["chocolate", "vanilla", "strawberry", "blueberry", "oreo", "banana"]
    assert count(test_old_list) == {"chocolate": 1, "vanilla": 1, "strawberry": 1, "blueberry": 1, "oreo": 1, "banana": 1}


def test_count_with_same() -> None:
    """Test count with all same strings."""
    test_old_list: list[str] = ["chocolate", "chocolate", "chocolate", "chocolate", "chocolate", "chocolate"]
    assert count(test_old_list) == {"chocolate": 6}


def test_count_with_empty() -> None:
    """Test count with an empty list."""
    test_old_list: list[str] = []
    assert count(test_old_list) == {}


# python -m pytest exercises/ex07