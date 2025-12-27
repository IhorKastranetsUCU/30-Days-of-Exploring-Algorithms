def bestClosingTime(customers: str) -> int:
    """
    >>> bestClosingTime("YYNY")
    2
    >>> bestClosingTime("NNNNN")
    0
    >>> bestClosingTime("YYYY")
    4
    """
    customers = "N"+customers
    y_arr = []
    counter = 0
    for i in customers:
        if i == "Y":
            counter+=1
        y_arr.append(counter)

    min_pen = 1e8
    min_ind = 0
    for i , num in enumerate(y_arr):
        pen = (i - y_arr[i]) + (y_arr[-1] - y_arr[i])
        if pen < min_pen:
            min_pen = pen
            min_ind = i

    return min_ind


if __name__ == "__main__":
    import doctest
    doctest.testmod()
