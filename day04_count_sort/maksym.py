def count_sort(arr : list) -> list:
    countArr = [0 for i in range(max(arr) + 1) ]
    pref_cnt = [0 for i in range(max(arr) + 1) ]
    for i in arr:
        countArr[i]+=1

    for i in range(1, max(arr) + 1):
        countArr[i] += countArr[i - 1]


    res = [0] * len(arr)
    print(pref_cnt)

    for i in range( len(arr)-1 , -1 , -1):
        res[ countArr[ arr[i] ] - 1] = arr[i]
        countArr[ arr[i] ] = countArr[ arr[i] ] - 1

    return res



if __name__ == "__main__":
    arr = [1, 4, 0, 2, 1, 1]
    arr_new = count_sort(arr)
    print(arr)
    print(arr_new)
