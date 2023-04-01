"""EX07 - Dictionary Functions."""
__author__ = "730517776"


def invert(old_dict: dict[str, str]) -> dict[str, str]:
    """Return a new dictionary that inverts the keys and the values of the old dictionary."""
    new_dict: dict[str, str] = {}
    for dict_item in old_dict:
        if old_dict[dict_item] in new_dict:
            raise KeyError("Key Error!")
        new_dict[old_dict[dict_item]] = dict_item
    return new_dict
    

def favorite_color(old_dict: dict[str, str]) -> str:
    """Return a new string which is the color that appears most frequently in the old dictionary."""
    new_dict: dict[str, int] = {}
    for dict_item in old_dict:
        if old_dict[dict_item] in new_dict:
            new_dict[dict_item] += 1
        else:
            new_dict[dict_item] = 1 
    max_dict_item: int = new_dict[0]
    max_dict_index: int = 0
    idx: int = 0
    while idx < len(new_dict):
        if max_dict_item < new_dict[idx + 1]:
            max_dict_item = new_dict[idx + 1]
            max_dict_index += 1
        idx += 1
    return new_dict[max_dict_index]
    # return the matching key for the value of max dict item
    # if there's a tie, return the key that appear first
    
    
def count(old_list: list[str]) -> dict[str, int]:
    """Return a new dictionary where each key is a unique value in the old list and each value is the count of that appeared in the old list."""
    new_dict: dict[str, int] = {}
    for list_item in old_list:
        if list_item in new_dict:
            new_dict[list_item] += 1
        else:
            new_dict[list_item] = 1
    return new_dict


# python -m tools.submission exercises/ex07