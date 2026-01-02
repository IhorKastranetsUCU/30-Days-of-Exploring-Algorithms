# Day 10

This was the tenth day of the challenge.
Feel slightly tired because of my Homework.

---

## Dijkstra algorithm


Today's topic was widely knew **Dijkstra algorithm**.

### My Thoughts
This algorithm is great and almost optimal , however during our DM project one of suggested new algorithm , which in certain condition can outperform Dijkstra in sparse graph.
[This algorithm Duan-Mao-Mao-Shu-Yiun ](https://arxiv.org/pdf/2504.17033)


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
