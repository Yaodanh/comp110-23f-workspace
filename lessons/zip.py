"""Combining two lists into a dictionary."""
__author__ = "730707593"


def zip(str_list: list[str], int_list: list[int]) -> dict[str, int]:
    """Create a definition of dictionary."""
    if len(str_list) != len(int_list) or len(str_list) == 0 or len(int_list) == 0:
        return {} 
    else:
        dictionary: dict[str, int] = {}
        for i in range(len(str_list)):
            dictionary[str_list[i]] = int_list[i]
        return dictionary
    

print(zip(["Happy", "Tuesday"], [1, 2]))
