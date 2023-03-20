"""Challenge Question 04 - Dict Function Writing."""
__author__ = "730517776"


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