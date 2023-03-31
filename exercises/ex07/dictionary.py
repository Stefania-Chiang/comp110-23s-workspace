"""EX07 - Dictionary Functions."""
__author__ = "730517776"


def invert(old_dict: dict[str, str]) -> dict[str, str]:
    """Return a new dictionary that inverts the keys and the values of the old dictionary."""
    new_dict: dict[str, str] = {}
    for key in old_dict:
        new_dict[value] = old_dict[key]
    for value in old_dict:
        new_dict[key] = old_dict[value]
    return new_dict
