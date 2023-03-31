"""EX07 - Dictionary Functions."""
__author__ = "730517776"


def invert(old_dict: dict[str, str]) -> dict[str, str]:
    """Return a new dictionary that inverts the keys and the values of the old dictionary."""
    new_dict: dict[str, str] = {}
    idx: int = 0
    while idx < len(old_dict):
        new_dict[]


def zip(first_list: list[str], second_list: list[int]) -> dict[str, int]:
    input_list: dict[str, int] = {}
    idx: int = 0
    if len(first_list) == len(second_list) and len(first_list) != 0:
        while idx < len(first_list):
            input_list[first_list[idx]] = second_list[idx]
            idx += 1
        return input_list 
    else:
        return input_list