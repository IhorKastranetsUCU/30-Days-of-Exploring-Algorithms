import doctest

def prefix_sum (nums: list[float]) -> list[float]:
    """
    Returns a list where each element contains the sum from the start up to that element
    :param nums: the input list of integer numbers
    :return: list of sums
    >>> prefix_sum([1, 2, 3, 4, 5])
    [1, 3, 6, 10, 15]
    >>> prefix_sum([-3, 2, -10, 11, 3, 0])
    [-3, -1, -11, 0, 3, 3]
    >>> prefix_sum([])
    []
    >>> prefix_sum([0.5, 3, -3, -0.5, 0])
    [0.5, 3.5, 0.5, 0.0, 0.0]
    """
    if not len(nums):
        return []

    list_of_sum = [nums[0]] * len(nums)

    for i, el in enumerate(nums[1:], 1):
        list_of_sum[i] = list_of_sum[i-1] + el
    return list_of_sum



if __name__ == "__main__":
    doctest.testmod()
