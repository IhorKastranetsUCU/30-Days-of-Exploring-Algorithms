# Day 11

This was the eleventh day of the challenge.
Saturday.

---

## Bellman-Ford

Today's topic was widely knew **Belman-Ford**.

### My Thoughts
Empty



### Algorithm
**Bellman-Ford** algorithm allows us to find min distance from single node to every other.
Special about this algorythm is that it can work with graphs ,  which contain negative-weight edges.
*NOTE* There must not be cycles of negative weight.
Idea is simple , we brute force throught list of edges at most *V-1* times.
On every step we check all edges, updating minimal possible distance to vertices which are connected by this edge.
Relevant question is why at most *V-1* ?
Reason is simple , it is gratest possible length of minimal path.
If path is longer => there exist cycle => length is not minimal.Therefore , we can optimize it.

**Efficency**
1. Time Complexity : **O(V*E)** , due to going through vertices.
2. Space Complexity : **O(V)** , **O(V)** size array for vertices


That's all! ))

## LeetCode



I've completed daily task **1411. Number of Ways to Paint N × 3 Grid**

Regarding today's algorythm , I resubmitted **743. Network Delay Time** and completed
**1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance**


That's all for today)

----

## LetCode problems

#### My implementation of Bellman-Ford
```python
def bellman_ford(graph : list , n : int , v ):
    dist = [float("inf")]*n
    prev = [-1] * n

    def update(dist : list ,prev : list , el):
        par , to , w = el[0] , el[1] ,el[2]
        tmp = dist[to]

        if dist[par] == float("inf"):
            return

        dist[to] = min(dist[to] , dist[par] + w )

        if tmp != dist[to]:
            prev[to] = par


    dist[v] = 0
    for i in range(n-1):
        for el in graph:
            update(dist , prev , el)

    return dist , prev

```

#### 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
```python

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        directed_edges = []
        for u, v, w in edges:
            directed_edges.append([u, v, w])
            directed_edges.append([v, u, w])

        def bellman_ford(graph: list, n: int, v: int):
            dist = [float("inf")] * n
            prev = [-1] * n

            def update(dist: list, prev: list, el: list):
                par, to, w = el[0], el[1], el[2]

                if dist[par] == float("inf"):
                    return

                tmp = dist[to]
                dist[to] = min(dist[to], dist[par] + w)

                if tmp != dist[to]:
                    prev[to] = par

            dist[v] = 0

            for i in range(n - 1):
                changed = False
                for el in graph:

                    before = dist[el[1]]

                    update(dist, prev, el)

                    if dist[el[1]] != before:
                        changed = True
                if not changed:
                    break

            return dist, prev

        min_reachable = float('inf')
        best_city = -1

        for i in range(n):
            dists, _ = bellman_ford(directed_edges, n, i)

            count = 0
            for node_idx, d in enumerate(dists):
                if node_idx != i and d <= distanceThreshold:
                    count += 1

            if count <= min_reachable:
                min_reachable = count
                best_city = i

        return best_city

```
____
