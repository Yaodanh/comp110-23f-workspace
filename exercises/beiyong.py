def all(numbers, target):
    if not numbers:
        return False
    
    for num in numbers:
        if num != target:
            return False
    
    return True

def max(input):
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    max_value = input[0]
    for num in input:
        if num > max_value:
            max_value = num
    
    return max_value

def is_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    
    return True

