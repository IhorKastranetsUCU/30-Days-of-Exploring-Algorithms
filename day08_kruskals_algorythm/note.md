# Day 8

This was the eighth day of the challenge.
Last day of the year ^_^ , nothing to add.

---

## Kruskal's Algorithm

Today's topic was **Kruskal's Algorithm**.

### My Thoughts
This algorithm was completely new to me.

### Algorithm
The core idea lies in the greedy connection of vertices.
First, we sort the array of edges to ensure that the greedy approach works.
Then, we simply iterate through every connection and check if two vertices are already in the same group.
This is handled by the DSU (Disjoint Set Union).
If they are, we move on; otherwise, we connect them and unite them in the DSU.
We continue this process until we have used **V-1** edges (because that is the minimum needed to connect all **V** vertices).
That's all! ))

**Efficiency:**
* Sorting the array takes **$O(E \log E)$** (where $E$ is the number of edges), using whatever sorting algorithm we like.
* Finding if two vertices are connected or uniting them takes only **$O(\alpha(V))$** time, thanks to the DSU.
---

## LeetCode

I've completed only one Kruskal task and it is **1584. Min cost to connect all points**

----

## LetCode problems

#### My implementation of Kruskal
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

def kruskal(num_vertices, edges):
    edges.sort(key=lambda x: x[2])

    dsu = DisjointSet(num_vertices)
    mst_edges = []
    total_cost = 0

    edges_count = 0

    for u, v, weight in edges:
        if dsu.union(u, v):
            mst_edges.append((u, v, weight))
            total_cost += weight
            edges_count += 1

            if edges_count == num_vertices - 1:
                break

    return total_cost

```
#### 1584. Min cost to connect all points

```
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        all_edges = []

        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                all_edges.append([i, j, dist])

        return kruskal(n, all_edges)

```
___
