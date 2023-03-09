"""EX05 - List Utility Functions."""
__author__ = "730517776"

evens_list: list[int]
sub_list: list[int]


def only_evens(int_list: list[int]) -> list[int]:
    """Return a new list containing only the elements of the input list that were even."""
    idx: int = 0
    evens_list: list[int] = []
    stop: int = len(int_list)
    for idx in range(0, stop):
        if int_list[idx] % 2 == 0:
            evens_list.append(int_list[idx])
        else:
            idx += 1
    return evens_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Generate a new List which contains all of the elements of the first list followed by all of the elements of the second list."""
    return first_list + second_list


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Generate a list which is a subset of the given list, between the specified start index and the end index - 1."""
    s: int = 0
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    if start >= len(a_list) or end <= 0 or len(a_list) == 0:
        return []
    sub_list: list[int] = []
    for s in range(start, end):
        sub_list.append(a_list[s])
    return sub_list