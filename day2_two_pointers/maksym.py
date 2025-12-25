def isPalindrome(x: list) -> bool:
    """
    >>> isPalindrome("aba")
    True
    >>> isPalindrome("racecar")
    True
    >>> isPalindrome("hello")
    False
    >>> isPalindrome("")
    True
    >>> isPalindrome("a")
    True
    >>> isPalindrome("Aba")
    False
    >>> isPalindrome("12321")
    True
    >>> isPalindrome(["a", "b", "1", 42, "1", "b", "a"])
    True
    """
    left = 0
    right = len(x)-1
    while left <= right:
        if x[left] != x[right]:
            return False
        left+=1
        right-=1
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
