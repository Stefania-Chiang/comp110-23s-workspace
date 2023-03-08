"""EX05 - List Utility Functions."""
__author__ = "730517776"


def only_evens(input_list: list[int]) -> list[int]:
    """Return a new list containing only the elements of the input list that were even"""
    new_list: list[int]
    idx: int = 0
    while idx < len(input_list):
        for num in input_list:
            if num % 2 == 0:
                return num
            new_list.append(num)
            idx += 1
    return new_list
