def count_sort(arr : list) -> list:
    """
    Sorts a list of non negative integers using the Counting Sort algorithm.

    Args:
        arr (list): A list of non-negative integers.

    Returns:
        list: A new list containing the sorted elements.

    Examples:
        >>> count_sort([4, 2, 2, 8, 3, 3, 1])
        [1, 2, 2, 3, 3, 4, 8]

        >>> count_sort([100, 5, 20, 5])
        [5, 5, 20, 100]

        >>> count_sort([0, 0, 0])
        [0, 0, 0]

        >>> count_sort([])
        []

        >>> count_sort([1])
        [1]

        >>> # Check stability (though not visible with integers, the logic ensures it)
        >>> count_sort([3, 1, 2])
        [1, 2, 3]
    """

    countArr = [0 for i in range(max(arr) + 1) ]
    pref_cnt = [0 for i in range(max(arr) + 1) ]
    for i in arr:
        countArr[i]+=1

    for i in range(1, max(arr) + 1):
        countArr[i] += countArr[i - 1]


    res = [0] * len(arr)
    #print(pref_cnt)

    for i in range( len(arr)-1 , -1 , -1):
        res[ countArr[ arr[i] ] - 1] = arr[i]
        countArr[ arr[i] ] = countArr[ arr[i] ] - 1

    return res



if __name__ == "__main__":
    arr = [1, 4, 0, 2, 1, 1 , 1]
    arr_new = count_sort(arr)
    print(arr)
    print(arr_new)
