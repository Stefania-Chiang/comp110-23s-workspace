"""EX05 - List Utility Functions."""
__author__ = "730517776"


def only_evens(old_list: list[int]) -> list[int]:
    """Return a new list containing only the even numbers of the old list."""
    new_list: list[int] = []
    for num in old_list:
        if num % 2 == 0:
            new_list.append(num)
    return new_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Return a new list containing all the numbers of the first list and the second list."""
    new_list: list[int] = []
    for num in first_list:
        new_list.append(num)
    for num in second_list:
        new_list.append(num)
    return new_list


def sub(given_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Return a new list which is subset of the given list between start index and end index - 1."""
    new_list: list[int] = [given_list[start_index], given_list[end_index - 1]]
    return new_list