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


if __name__ == "__main__" :
    import doctestф
    doctest.testmod()
