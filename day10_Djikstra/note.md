# Day 10
___


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
