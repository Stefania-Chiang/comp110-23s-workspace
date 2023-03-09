"""EX05 - List Utility Functions."""
__author__ = "730517776"


def only_evens(input_list: list[int]) -> list[int]:
    """Return a new list containing only the elements of the input list that were even."""
    for num in input_list:
        if num % 2 == 0:
            input_list.append(num)
    return input_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Generate a new List which contains all of the elements of the first list followed by all of the elements of the second list."""
    for num in second_list:
        first_list.append(num)
    return first_list


def sub(a_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Generate a list which is a subset of the given list, between the specified start index and the end index - 1."""
    a_list: list[int] = [a_list[start_index], a_list[end_index - 1]]
    return a_list