"""EX05 - List Utility Functions."""
__author__ = "730517776"


def only_evens(input_list: list[int]) -> list[int]:
    """Return a new list containing only the elements of the input list that were even"""
    new_list: list[int]
    for num in input_list:
        if num % 2 == 0:
            new_list.append(num)
    return new_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Generate a new List which contains all of the elements of the first list followed by all of the elements of the second list."""
    