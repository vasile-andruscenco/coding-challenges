import numbers


def first_appearance(numbers, target):
    """Find the index of the first occurrence of target in a sorted list.

    Uses binary search, continuing left after each match to find the earliest
    occurrence. Returns -1 if target is not present.

    Args:
        numbers (list[int]): A sorted list of integers.
        target (int): The value to search for.

    Returns:
        int: Index of the first occurrence of target, or -1 if not found.

    Examples:
        >>> first_appearance([1, 2, 2, 2, 3], 2)
        1
        >>> first_appearance([1, 3, 5], 4)
        -1
    """
    left = 0
    right = len(numbers) - 1
    result = -1

    while left <= right:
        middle = left + (right -left) // 2
        if numbers[middle] == target:
            result = middle
            right = middle - 1
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return result

def exists(numbers, target):
    """Check whether target exists in a sorted list using binary search.

    Args:
        numbers (list[int]): A sorted list of integers.
        target (int): The value to search for.

    Returns:
        bool: True if target is present, False otherwise.

    Examples:
        >>> exists([1, 3, 5, 7], 5)
        True
        >>> exists([1, 3, 5, 7], 4)
        False
    """

    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = left + (right - left) // 2
        if numbers[middle] == target:
            return True
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return False

def last_appearance(numbers, target):
    """Find the index of the last occurrence of target in a sorted list.

    Uses binary search, continuing right after each match to find the latest
    occurrence. Returns -1 if target is not present.

    Args:
        numbers (list[int]): A sorted list of integers.
        target (int): The value to search for.

    Returns:
        int: Index of the last occurrence of target, or -1 if not found.

    Examples:
        >>> last_appearance([1, 2, 2, 2, 3], 2)
        3
        >>> last_appearance([1, 3, 5], 4)
        -1
    """
    left = 0
    right = len(numbers) - 1
    result = -1

    while left <= right:
        middle = left + (right - left) // 2
        if numbers[middle] == target:
            result = middle
            left = middle + 1
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return result


def first_greater_or_equal(numbers, target):
    """Find the index of the first element >= target in a sorted list.

    Equivalent to a lower-bound search. Returns -1 if all elements are
    strictly less than target.

    Args:
        numbers (list[int]): A sorted list of integers.
        target (int): The lower bound value to search for.

    Returns:
        int: Index of the first element >= target, or -1 if none exists.

    Examples:
        >>> first_greater_or_equal([1, 3, 5, 7], 4)
        2
        >>> first_greater_or_equal([1, 3, 5, 7], 8)
        -1
    """

    left = 0
    right = len(numbers) - 1
    result = -1

    while left <= right:
        middle = left + (right - left) // 2
        if numbers[middle] >= target:
            result = middle
            right = middle - 1
        else:
            left = middle + 1
    return result


def last_less_or_equal(numbers, target):
    """Find the index of the last element <= target in a sorted list.

    Equivalent to an upper-bound search. Returns -1 if all elements are
    strictly greater than target.

    Args:
        numbers (list[int]): A sorted list of integers.
        target (int): The upper bound value to search for.

    Returns:
        int: Index of the last element <= target, or -1 if none exists.

    Examples:
        >>> last_less_or_equal([1, 3, 5, 7], 4)
        1
        >>> last_less_or_equal([1, 3, 5, 7], 0)
        -1
    """

    left = 0
    right = len(numbers) - 1
    result = -1
    while left <= right:
        middle = left + (right - left) // 2
        if numbers[middle] <= target:
            result = middle
            left = middle + 1
        else:
            right = middle - 1
    return result

def integer_square_root(number):
    """Compute the integer (floor) square root of a non-negative integer.

    Returns the largest integer k such that k * k <= number, using binary
    search over the range [0, number].

    Args:
        number (int): A non-negative integer.

    Returns:
        int: The floor of the square root of number.

    Examples:
        >>> integer_square_root(81)
        9
        >>> integer_square_root(50)
        7
        >>> integer_square_root(15)
        3
    """
    left = 0
    right = number
    result = 0

    while left <= right:
        middle = left + (right - left) // 2
        square = middle * middle
        if square == number:
            return middle
        elif square < number:
            result = middle
            left = middle + 1
        else:
            right = middle - 1

    return result
