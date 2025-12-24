def generate_prefix_sum(array: list):
    """
    Creates a list of prefix sums for the array.

    Args:
        array (list): A list of integers or floats.

    Returns:
        list: A new list where the element at index i is the sum of array[0]...array[i].

    >>> generate_prefix_sum([1, 2, 3, 4])
    [1, 3, 6, 10]
    >>> generate_prefix_sum([10, -2, 5])
    [10, 8, 13]
    >>> generate_prefix_sum([5])
    [5]
    """
    if not array:
        return []

    prefix_sum_list = [0] * len(array)

    prefix_sum_list[0] = array[0]

    for i in range(1, len(array)):
        prefix_sum_list[i] = prefix_sum_list[i-1] + array[i]

    return prefix_sum_list

def sum_on_line(prefix_array: list, a: int, b: int):
    """
    Calculates the sum on the interval [a, b] (inclusive) using a prefix sum list.

    Args:
        prefix_array (list): The pre-calculated prefix sum list (from generate_prefix_sum).
        a (int): The starting index (0-based).
        b (int): The ending index (0-based).

    Returns:
        int: The sum of elements in the original array between index a and b.

    >>> p_list = [1, 3, 6, 10]
    >>> sum_on_line(p_list, 0, 2)
    6
    >>> sum_on_line(p_list, 1, 3)
    9
    >>> sum_on_line(p_list, 2, 2)
    3
    """
    if a == 0:
        return prefix_array[b]

    return prefix_array[b] - prefix_array[a-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
