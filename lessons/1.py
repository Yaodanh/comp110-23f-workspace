"""Practice with dictionaries"""


ice_cream: dict[str,int] = {"chocolate":12, "vanilla":8, "strawberry":5}
#adding
ice_cream["mint"] = 3


temps: dict[str, float] = {"Raleigh":56.5, "Boston":51.0}
#removing
temps.pop("Boston")


#take a value
temps["Raleigh"]
print(f"There are {ice_cream['chocolate']} orders of chocolate.")

#subscription
ice_cream["vanilla"] += 1
ice_cream["vanilla"] = 9

#length of dictionary
print(f"The number of key value pairs:{len(ice_cream)}")

#check if key in dictionary
print("Is mint in ice_cream")
print("mint" in ice_cream)
#use condition
if "mint" in ice_cream:
    print(f"There are {ice_cream['mint']} orders of mint.")
else:
    print("no orders of mint.")

#loop through ang print out every flavor and its number of orders
for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders.")

    

"""Practicing summing over lists."""

def sum_evens_in_list(input_list: list[int]) -> int:
    list_sum: int = 0
    for elem in input_list:
        if elem % 2 == 0:
            list_sum = list_sum + elem
    return list_sum

from lessons.sum_evens import sum_evens_in_list

def test_empty_sum():
    assert sum_evens_in_list([]) == 0

def test_list_length_1():
    test_list: list[int] = [2]
    assert sum_evens_in_list(test_list) == 2

def test_list_positives():
    test_list: list[int] = [1,2,3,4]
    assert sum_evens_in_list(test_list) == 6

def test_list_negs_and_pos():
    test_list: list[int] = [1,-2,3,4]
    assert sum_evens_in_list(test_list)