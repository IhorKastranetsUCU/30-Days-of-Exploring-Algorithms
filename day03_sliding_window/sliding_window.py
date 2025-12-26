def countGoodSubstrings(s: str) -> int:
    """
    The idea of static sliding window is simple. We take few items in the row
    and move the whole block at the time by subtracting the first value and adding the newest one.

    This function solves the problem where tou need to find the count of sequences
    with the total length of 3 and unique characters only

    >>> countGoodSubstrings("abscdsd")
    4
    >>> countGoodSubstrings("Abracadabra")
    7
    >>> countGoodSubstrings("Ihor")
    2
    """

    l, r, res = 0, 3, 0
    while r <= len(s):
        if len(set(s[l:r])) == 3:
            res += 1
        l += 1
        r += 1
    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod()