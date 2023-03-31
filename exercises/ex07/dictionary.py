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
    """Return a new string which is the color that appears most frequently in the old dictionary."""
    new_string: str = ""
    



def count(old_list: list[str]) -> dict[str, int]:
    """Return a new dictionary where each key is a unique value in the old list and each value is the count of that appeared in the old list."""
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

# python -m pytest exercises/ex07