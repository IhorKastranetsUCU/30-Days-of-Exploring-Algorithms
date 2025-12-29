# Day 6

This was the sixth day of the challenge.
Things are going good. I am currently preparing for my next exam period ).
Productivity is not as bad as i thought i coulde , therefore everythins is great.

---

## Heap Sort

Today's topic was **Heap sort**.

#### My thoughts
Concept of heap is widely used in programing , so I heard about it in past.
However , I haven't deeply dive into it. This topic reqired some knoweledge from
Discrete Math course from past term in uni. Even before uni , I was familiar with trees
due to intresting circumstances, thats why heap was not completly new for me.

#### Algorythm
Concept of heap is to create "Heap" - commonly represented as binary tree with unique property.
This property can differ , common heaps are max/min Heap.
Where elements are positioned from top down in descending or ascending order.
If we are talking about sort , idea is that on top of MaxHeap is always greatest element ,
by knowing it we can build heap , take gratest element  , swap with the element in end and then move (kinda delete ) it  from heap.
And by going through all heap we can make array sorted.
One more question to raise is how to keep it max heap.
We would do process called heapify. Idea , we go through changed part of tree and restore order by checking is structure is correct and if not we swap incorrect nodes.
Recursion ensuars that we would not come across bugs )


---

## LeetCode

I've completed **912. Sort an Array** just to test my implementation of heap sort.
Also by idea of heap , i sorted array till certain point
I've solved **215. Kth Largest Element in an Array**


----

## LetCode problems

#### 912. Sort an Array
```
def sortArray(self, nums: List[int]) -> List[int]:
    arr = nums
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

    n = len(arr)

    #build_max_heap
    for i in range( n//2 -1 , -1 , -1):
        heapify(arr, i , n)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)

    return arr



```
___

#### 215. Kth Largest Element in an Array
```
def findKthLargest(self, nums: List[int], k: int) -> int:
    arr = nums
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


    n = len(arr)

    #build_max_heap
    for i in range( n//2 -1 , -1 , -1):
        heapify(arr, i , n)

    for i in range(n - 1, n-k, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)

    return arr[0]
```
___
#### My implementation of Heap Sort
```
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

def heap_sort(arr : list):
    n = len(arr)

    #build_max_heap
    for i in range( n//2 -1 , -1 , -1):
        heapify(arr, i , n)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)

    return arr
```
