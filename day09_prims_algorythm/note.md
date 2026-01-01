# Day 9

This was the nienth day of the challenge.
First day of the year

---

## Prim's Algorithm

Today's topic was **Prim's Algorithm**.

### My Thoughts
This algorithm was new to me, however i saw it yesterday as analogy for kruskal

### Algorithm
Core idea: Gready Dijkstra which build way to every vertice.
We start from specific node. Then we put all adjentic vertices in heap (i used min heap).
Then we get min from a heap , check do not vertices of this edge is already connected.
If they have not been connected prevoiusly we add our edge in MST , and using DSU connect this two vertices.
We repeat until there are **N-1** edges in MST.

**Efficency**
1. Time Complexity : **O(VlogV)** , due to going through all vertices and for each apply heap.Dsu time is negligible.
2. Space Complexity : **O(V+E)** , **O(V)** size array for vertices for DSU and **O(E)** space for min heap


That's all! ))

## LeetCode



I've completed daily task **66. Plus One** , it was genuenly easy.
Relative to Prims Algorythm I resubmitted **1584. Min cost to connect all points** using prims algorythm.
P.S During solution I realised that using DSU is not needed here , cause greedy approach ensuars we would go into already visited vertices. It's simplier and more efficeint to use just set of visited vertices,which i did in leetcode solution.


That's all for today)

----

## LetCode problems

#### My implementation of Prim's
```
class DisjointSet:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            if self.rank[root_a] < self.rank[root_b]:
                self.parents[root_a] = root_b
                self.size[root_b] += self.size[root_a]
            elif self.rank[root_a] > self.rank[root_b]:
                self.parents[root_b] = root_a
                self.size[root_a] += self.size[root_b]
            else:
                self.parents[root_b] = root_a
                self.rank[root_a] += 1
                self.size[root_a] += self.size[root_b]
            return True
        return False

def heapify(arr : list , v : int , n : int) -> list:
    left_child = 2*v+1
    right_child = 2*v+2
    largest = v

    if left_child < n and arr[left_child] < arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] < arr[largest]:
        largest = right_child

    if largest!=v:
        arr[v] , arr[largest] = arr[largest] , arr[v]

        heapify(arr , largest , n)

def heap(arr : list) -> list :
    n = len(arr)
    for i in range( n//2 -1 , -1 , -1):
        heapify(arr, i , n)
    return arr

def insert_in_heap(arr: list, v: int):
    arr.append(v)
    current = len(arr) - 1

    while current > 0:
        parent = (current - 1) // 2
        if arr[current] < arr[parent]:
            arr[current], arr[parent] = arr[parent], arr[current]
            current = parent
        else:
            break

def heap_pop(arr : list):
    arr[-1], arr[0] = arr[0], arr[-1]
    res = arr.pop()
    heapify(arr, 0, len(arr))
    return res


def prims_adjencylist(graph : dict, v):
    res_arr = []
    dsu = DisjointSet(len(graph))
    min_heap = heap([])
    while len(res_arr) < len(graph)-1:
        for neighbor , value in graph[v]:
            insert_in_heap(min_heap , (value , v , neighbor) )

        while len(min_heap) > 0:
            to_edge  = heap_pop(min_heap)

            if dsu.find(to_edge[1]) != dsu.find(to_edge[2]):
                dsu.union(to_edge[1] , to_edge[2])
                res_arr.append( ( to_edge[1] ,to_edge[2] ,to_edge[0] ) )
                v = to_edge[2]
                break

    mst_val = sum([el[2] for el in res_arr ])

    return res_arr , mst_val

```
#### 1584. Min cost to connect all points
```
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        min_heap = []

        insert_in_heap(min_heap, (0, 0))

        visited = [False] * n
        mst_cost = 0
        edges_count = 0

        while min_heap:
            cost, u = heap_pop(min_heap)

            if visited[u]:
                continue

            visited[u] = True
            mst_cost += cost
            edges_count += 1

            if edges_count == n:
                break

            for v in range(n):
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + \
                           abs(points[u][1] - points[v][1])
                    insert_in_heap(min_heap, (dist, v))

        return mst_cost
```
___
