Day 10
___
- [Maksym’s Notes](#Maksym)
- [Ihor’s Notes](#Ihor)
___

# Maksym 

This was the tenth day of the challenge.
Feel slightly tired because of my Homework.

---

## Dijkstra algorithm


Today's topic was widely knew **Dijkstra algorithm**.

### My Thoughts
This algorithm is great and almost optimal , however during our DM project one of suggested was new algorithm , which in certain condition can outperform Dijkstra in sparse graph.



### Algorithm
We start from certain node ,then we look for smallest distance to enter new node and we enter it.
We do so until we come in last unvisited lost. In result we get list of mininal distance we have to travle to get to each vertice



**Efficency**
1. Time Complexity : **O(ElogV)** , due to going through vertices and find min using min-heap.
2. Space Complexity : **O(V+E)** , **O(V)** size array for vertices and **O(E)** space for min heap


That's all! ))

## LeetCode



I've completed daily task **961. N-Repeated Element in Size 2N Array** , it was genuenly easy.

To try ot my implementation of Dijkstra i solved **743. Network Delay Time**.
Also had a look on more complex problems as **778. Swim in Rising Water** , i created idea ,but haven't  implimented it yet.

Also , i have practised my OOP skills and implemented my own Heap class with castomizable heap criteria.

That's all for today)

----

## LetCode problems

#### My implementation of Dijkstra
```python
from typing import Callable

class Heap:

    def __init__(self , comparator : Callable = (lambda x,y : x < y) ):
        self.heap = []
        self.comp = comparator

    def __str__(self):
        return str(self.heap)

    def push_down(self , v):
        n = len(self.heap)
        while True:
            left = 2*v+1
            right = 2*v+2
            most = v

            if left < n and self.comp( self.heap[left], self.heap[most] ):
                most = left
            if right < n and self.comp( self.heap[right], self.heap[most] ):
                most = right

            if most != v:
                self.heap[v] , self.heap[most] = self.heap[most] , self.heap[v]
                v = most
            else:
                break

    def push_up(self , v):
        while v > 0:
            parents = (v-1) //2
            if self.comp(self.heap[v] , self.heap[parents]):
                self.heap[v] , self.heap[parents] = self.heap[parents] , self.heap[v]
                v = parents
            else:
                break

    def insert(self , el ):
        self.heap.append(el)
        self.push_up(len(self.heap)-1)

    def pop(self):
        if not self.heap:
            return None

        self.heap[0] , self.heap[-1] = self.heap[-1] , self.heap[0]
        pop_element = self.heap.pop()

        if self.heap:
            self.push_down(0)

        return pop_element

    def build_heap_from_array(self, array : list):
        self.heap = array
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.push_down(i)

    def size(self):
        return len(self.heap)



def Dijkstra(graph : dict , v):

    dheap = Heap(lambda x,y : x < y)
    dheap.insert( ( 0, v , 0) )

    visited = {}
    closest = {}

    while dheap.size() > 0:
        weight, to , parent = dheap.pop()

        if to in visited:
            continue

        visited[to] = weight
        closest[to] = parent

        if to in graph:
            for sus , sus_w in graph[to]:
                if sus not in visited:
                    new_distance = weight + sus_w
                    dheap.insert((new_distance, sus , to))

    return visited , closest


```


#### 743. Network Delay Time

```python
def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    from collections import defaultdict
    graph = defaultdict(list)

    for edge in times:
        u = edge[0]
        v = edge[1]

        weight = edge[2]
        val_forward = (v, weight)
        graph[u].append(val_forward)

        if v not in graph:
            graph[v] = []

    result = Dijkstra(graph, k)
    ans = max(result.values())
    if len(result)!=n:
        return -1

    return ans

```
___

#### 961. N-Repeated Element in Size 2N Array
```python
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hash_map = {}
        for el in nums:
            hash_map.setdefault(el , 0)
            hash_map[el]+=1

        for i in hash_map:
            if hash_map[i] == len(nums)//2:
                return i
```
___
# Ihor
## Dijkstra's Algorithm
Dijkstra's is well known for me from Discrete math course from university. 

In implementation, I used heapq package to use Heap data structure which is
uses in algorithm to guarantee time complexity $O((E+V)\log V)$

```python 
import heapq

def dijkstra(graph: dict, nodes: list, start):
    path_len = {v: float("inf") for v in nodes}
    path_len[start] = 0
    parents = {v: None for v in nodes}
    minHeap = [[0, start]]

    while minHeap:
        w1, v1 = heapq.heappop(minHeap)
        if w1 > path_len[v1]:
            continue

        for v2, w2 in graph[v1]:
            weight = w2 + w1
            if weight < path_len[v2]:
                path_len[v2] = weight
                parents[v2] = v1
                heapq.heappush(minHeap, (weight, v2))
    return  path_len, parents
```

To learn this algorithm I watched several videos with its implementation but only one 
of them has correct code.

### Good sources
- [Dijkstra's Shortest Path Algorithm Visually Explained](https://www.youtube.com/watch?v=0W8WoRaw5Es) 
– uses Heap data structure and compares the new cost to an assigned.
- [How Dijkstra's Algorithm Works](https://www.youtube.com/watch?v=EFg3u_E6eHU) – great visualisation of an algorithm
### Weak sources
- [Implement Dijkstra's Algorithm](https://www.youtube.com/watch?v=XEb7_z5dG3c)
– its implementation doesn't compare new weights to already exited
- [Dijkstra's Algorithm - Dynamic Programming Algorithms in Python (Part 2)](https://www.youtube.com/watch?v=VnTlW572Sc4)
– its implementation doesn't use Heap data structure, so the time complexity increases to $O(E + V^2)$



___

## Pandas
Today I opened to category on LeetCode for me calls `pandas`. It has problems on datasets
which you can solve with `pandas`, `MySQL`, `Oracle`, `PostgreeSQL` or `MySQL server`. I 
decided to solve several problems and I learned how to rename columns, drop and merge. Also
I practiced basic operations as creating DataFrame, reading from csv, finding shape, rewrite 
on place and saving needed data.

For learning I used these videos:
- [Merging DataFrames in Pandas | Python Pandas Tutorials](https://www.youtube.com/watch?v=TPivN7tpdwc&t=1019s)
- [Pandas Drop Duplicates // Drop duplicate rows in Python pandas with examples for subset and keep](https://www.youtube.com/watch?v=LuB1zEDwteE)
___
## LeetCode
I got 50 solved problems on LeetCode. I think it is more then possible to get 100 until the
end of the challenge. 

I started with daily problem which was quite simple, using hash-tables. Then I solved 4 pandas
problems.
![img.png](img.png)
