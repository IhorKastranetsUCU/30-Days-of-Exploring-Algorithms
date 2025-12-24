def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (high + low)//2
        print(mid)
        if item > list[mid]:
            low = mid + 1
        elif item < list[mid]:
            high = mid - 1
        else:
            return mid
print(binary_search([1, 2, 3, 4, 5, 10, 11], 3))


