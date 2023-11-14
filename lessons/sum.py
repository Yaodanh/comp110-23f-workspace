"""Summing the elements of a list using different loops."""
__author__ = 730707593
num1: float = 1.1
num2: float = 0.9
num3: float = 1.0
vals: list[float] = [num1, num2, num3]


def w_sum(vals: list[float]) -> float:
    """Summing the elements of a list using while loop."""
    idx = 0
    sum = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Summing the elements of a list using for loop."""
    new_sum = 0.0
    for val in vals:
        new_sum += val
    return new_sum


def f_range_sum(vals: list[float]) -> float:
    """Summing the elements of a list using for_range loop."""
    total = 0.0
    for idx in range(0, len(vals)):
        total += vals[idx]
    return total


print(w_sum(vals))
print(f_sum(vals))
print(f_range_sum(vals))
