import sys
from typing import List


def add(values: List[float]) -> float:
    """Return the sum of all negative numbers in the list."""
    return sum(x for x in values if x < 0)


def subtract(values: List[float]) -> float:
    """Return the difference of all positive numbers in the list."""
    positive_numbers = [x for x in values if x > 0]
    if not positive_numbers:
        return 0
    result = positive_numbers[0]
    for num in positive_numbers[1:]:
        result -= num
    return result


def multiply(values: List[float]) -> float:
    """Return the product of all non-zero numbers in the list."""
    non_zero_numbers = [x for x in values if x != 0]
    if not non_zero_numbers:
        return 0
    result = 1
    for num in non_zero_numbers:
        result *= num
    return result


def divide(values: List[float]) -> float:
    """Return the result of dividing all numbers in the list."""
    if not values:
        return 0
    if values[0] == 0:
        if 0 in values[1:]:
            sys.exit("Cannot divide by 0.")
        return 0
    result = values[0]
    for num in values[1:]:
        if num == 0:
            sys.exit("Cannot divide by 0.")
        result /= num
    return result
