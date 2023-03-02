"""EX04 - Utility Functions"""
__author__: str = "730517776"

# function 1 of EX04: all
def all(input: list[int], num: int) -> bool:
    """Returns a bool indicating whether or not all the ints in the list are the same as the given int"""
    if len(input) == 0:
        return False
    index: int = 0
    while index < len(input):
        # While looping, look for the same value 
        if num != input[index]:
            # Return True or False
            return False
        index += 1
    return True

# function 2 of EX04: max
def max(input: list[int]) -> int:
    """Returns the largest number in the list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 0 
    max = input[0]
    # Loop through the input list 
    while index < len(input) - 1:
        # While looping, look for the biggest value 
        if max < input[index + 1]:
            max = input[index + 1]
        index += 1
    # Return the biggest value 
    return max

# function 3 of EX04: is_equal
def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Return True if every element at every index is equal in both lists"""
    if len(list_1) != len(list_2):
        return False
    elif list_1 == list_2:
        return True
    else:
        return False
