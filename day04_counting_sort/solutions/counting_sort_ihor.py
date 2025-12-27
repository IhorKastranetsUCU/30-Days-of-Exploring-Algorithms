def counting_sort(array: list[int]) -> None:
    """
    This algorithm creates a hash table (or list) for every integer between the
    smallest and largest element in the given array, initializing each count to 0.
    Then it counts how many times each element appears in the array by incrementing
    the corresponding count.

    Next, it computes a prefix sum (cumulative sum) over the counts to determine
    the final positions of elements in the sorted array.

    Finally, it iterates through the array in reverse, placing each element at its
    correct position according to the prefix sum, and updates the counts accordingly.

    The algorithm modifies the given array in-place and does not return any value.

    :param array: list[int] – array that will be sorted. Should contain only integers.
    :return: None

    >>> array = [1, 4, -2, 10, -5]
    >>> counting_sort(array)
    >>> print(array)
    [-5, -2, 1, 4, 10]
    >>> array = [0, 1, 1, 1, 1, 0, 0, 0, 1]
    >>> counting_sort(array)
    >>> print(array)
    [0, 0, 0, 0, 1, 1, 1, 1, 1]
    """
    min_el = min(array)
    max_el = max(array)
    counts = {i: 0 for i in range(min_el, max_el + 1)}

    for i in array:
        counts[i] += 1

    for i in counts.keys():
        if i < max_el:
            counts[i + 1] += counts[i]

    for i in array[::-1]:
        array[counts[i] - 1] = i
        counts[i] -= 1

    return