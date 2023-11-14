"""ex04_utils."""
__author__ = "703707593"


def all(list_of_numbers: list[int], number: int) -> bool:
    """Search the number in the list_of _number list of string."""
    idx = 0
    if len(list_of_numbers) == 0:
        return False
    while idx < len(list_of_numbers):
        if list_of_numbers[idx] == number:
            idx += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Compare each int to get the max_value."""
    max_value: int = input[0]
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx = 1
    while idx < len(input):
        if max_value < input[idx]:
            max_value = input[idx]
        idx += 1
    return max_value
    

def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Determine whether two arguements are equal."""
    if list1 == list2:
        return True
    return False
