def interpolation_search(arr : list[int] , x : int) -> int:
    low , high = 0 , len(arr) - 1

    #iteration
    i = 0

    while low <= high and x >= arr[low] and x <= arr[high]:

        if low == high:
            if arr[low] == x:
                return (low, i)
            return -1

        i+=1
        pos = low + ( (x - arr[low]) * (high - low) // (arr[high] - arr[low]) )

        if arr[pos] == x:
            return ( pos , i)

        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(arr)
    print(interpolation_search(arr , 30))
    print(interpolation_search(arr , 80))
    #--------
    arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 1024, 2048]
    print(arr)
    print(interpolation_search(arr , 2048))
    print(interpolation_search(arr , 512))
    arr = [1]
    print(arr)
    print(interpolation_search(arr , 2048))
    print(interpolation_search(arr , 512))