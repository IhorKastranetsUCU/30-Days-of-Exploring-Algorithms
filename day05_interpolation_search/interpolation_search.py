def interpolation_search(array: list, key):
    pos = 0
    l, r = 0, len(array) - 1
    while l <= r and key >= array[l] and key <= array[r]:
        pos = int(l + ((key - array[l]) * (r - l)) / (array[r] - array[l]))
        if array[pos] < key:
            l = pos + 1
        elif array[pos] > key:
            r = pos - 1
        else:
            return pos
    return -1
