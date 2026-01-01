def heapify(arr : list , v : int , n : int) -> list:
    left_child = 2*v+1
    right_child = 2*v+2
    largest = v

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest!=v:
        arr[v] , arr[largest] = arr[largest] , arr[v]

        heapify(arr , largest , n)

def max_heap(arr : list) -> list :
    n = len(arr)
    for i in range( n//2 -1 , -1 , -1):
        heapify(arr, i , n)
    return arr


def insert_in_heap(arr: list, v: int):
    arr.append(v)
    current = len(arr) - 1

    while current > 0:
        parent = (current - 1) // 2
        if arr[current] > arr[parent]:
            arr[current], arr[parent] = arr[parent], arr[current]
            current = parent
        else:
            break



def heap_sort(arr : list):
    n = len(arr)

    #build_max_heap
    for i in range( n//2 -1 , -1 , -1):
        heapify(arr, i , n)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)

    return arr



if __name__ == "__main__":
    arr = [5,12,64,1,37, 90, 91 , 97]
    print(max_heap(arr))
    insert_in_heap(arr, 39)
    print(max_heap(arr))
