"""EX05 - List Utility Functions."""
__author__ = "730517776"


def only_evens(input_list: list[int]) -> list[int]:
    """Return a new list containing only the elements of the input list that were even"""
    for num in input_list:
        if num % 2 == 0:
            print(num)