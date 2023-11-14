def get_a(list1: list[str]) -> dict[int, str]:
    """This function gets all words starting with "a"."""
    return_dict: dict[int, str] = {}
    n: int = 1
    for i in list1:
        if i[0] == "a":
            return_dict[n] = i
            n += 1
    return return_dict
            

def remove_even(list1: list[int]) -> list[int]:
    odd_list: list[int] = []#create a new list to avoid influencing list1
    for i in list1:
        if i % 2 != 0:
            odd_list.append (i)#use append instead of pop
    return odd_list

def no_letter_word(list_str: list[str]) -> list[str]:
    returned_list: list[str] = []
    for i in list_str:
        returned_list. append(i)
    for i in returned_list:
        if len(i) == 4:
            returned_list.pop(i)
    return returned_list