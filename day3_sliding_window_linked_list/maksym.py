def totalFruit(fruits: list[int]) -> int:
    """
    >>> totalFruit([1,2,1])
    3
    >>> totalFruit([0,1,2,2])
    3
    >>> totalFruit([1,2,3,2,2])
    4
    >>> totalFruit([3,3,3,1,2,1,1,2,3,3,4])
    5
    """
    pleft = 0
    pright = 0
    dict_fruit = {}
    max_outcome = -1
    while pright < len(fruits):

        if fruits[pright] not in dict_fruit:
            dict_fruit.setdefault(fruits[pright],0)
        dict_fruit[fruits[pright]] += 1


        while len(dict_fruit)>2:
            dict_fruit[ fruits[ pleft] ]  -= 1
            if dict_fruit[ fruits[ pleft] ]  == 0:
                dict_fruit.pop( fruits[ pleft] )
            pleft += 1

        max_outcome = max(max_outcome ,  pright - pleft + 1 )

        pright+=1



    return max_outcome

def countGoodSubstrings(s: str) -> int:
    """
    Returns the number of good substrings of length three in s.
    A substring is good if there are no repeated characters.

    >>> countGoodSubstrings("xyzzaz")
    1
    >>> countGoodSubstrings("aababcabc")
    4
    >>> countGoodSubstrings("abc")
    1
    >>> countGoodSubstrings("aba")
    0
    >>> countGoodSubstrings("aa")
    0
    """
    count = 0
    for i in range(len(s) - 2):
        if len(set(s[i:i+3])) == 3:
            count += 1
    return count


if __name__ == "__main__" :
    import doctest
    doctest.testmod()
