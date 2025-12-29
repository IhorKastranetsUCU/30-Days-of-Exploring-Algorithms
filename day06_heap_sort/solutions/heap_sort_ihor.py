def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def build_max_heap(array):
    for i in range((len(array) - 1) // 2, -1, -1):
        heapify(array, len(array), i)

def heapify(array, n, i):
    l = 2 * i + 1
    r = 2 * i + 2

    max = l if l < n and array[l] > array[i] else i
    if r < n and array[r] > array[max]:
        max = r
    if max != i:
        swap(array, max, i)
        heapify(array, n, max)

def heapsort(array):
    build_max_heap(array)
    for i in range(len(array) - 1, 0, -1):
        swap(array, 0, i)
        heapify(array, i,0)
