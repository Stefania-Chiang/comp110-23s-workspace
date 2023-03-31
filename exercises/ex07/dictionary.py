"""EX07 - Dictionary Functions."""
__author__ = "730517776"


def invert(old_dict: dict[str, str]) -> dict[str, str]:
    """Return a new dictionary that inverts the keys and the values of the old dictionary."""
    new_dict: dict[str, str] = {}
    for key in old_dict:
        if old_dict[key] in new_dict:
            raise KeyError("Key Error!")
        new_dict[old_dict[key]] = key
    return new_dict
    

def favorite_color(old_dict: dict[str, str]) -> str:
    """Return a str which is the color that appears most frequently in the given dictionary."""
    new_str: str = ""



def count(old_list: list[str]) -> dict[str, int]:
    """Return a dictionary where each key is a unique value in the given list and each value is the count of that appeared in the given list."""
    new_dict: dict[str, int] = {}
    idx: int = 0
    list_item: str = old_list[idx]
    while idx < len(old_list):
        if list_item in new_dict:
            new_dict[list_item] += 1
        else:
            new_dict[list_item] = 1
        idx += 1
    return new_dict



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


# python -m pytest exercises/ex07