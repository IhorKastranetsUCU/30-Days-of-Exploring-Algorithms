def two_pointers(string):
    """
    The function is an example of two pinters algoithm. It checks is the string palindrom.
    :param string: str, the given string
    :return: True if the string is palindrom, False otherwise
    >>> two_pointers("1234")
    False
    >>> two_pointers("HeleH")
    True
    >>> two_pointers("lalalal")
    True
    """
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True