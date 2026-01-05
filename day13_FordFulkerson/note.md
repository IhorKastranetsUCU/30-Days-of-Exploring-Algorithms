# Day 13

This was the thirteen day of the challenge.
Monday.

---

## Fold-Fulkerson

Today's topic was Fold-Fulkerson.
### My Thoughts
We have entered Flow Network Theor


# The Ford-Fulkerson Algorithm

### **Algorithm Overview**
**Ford-Fulkerson** is a greedy algorithm used to compute the **Maximum Flow** in a flow network. It iteratively pushes flow from a Source ($S$) to a Sink ($T$) until no more flow can be added.

### **Key Concepts**
1.  **Flow Network:** A directed graph where each edge has a capacity.
2.  **Augmenting Path:** A path from Source to Sink in the **residual graph** where every edge has remaining capacity greater than zero.
3.  **Residual Graph:** A representation of the network that shows two things:
    * **Forward Capacity:** How much *more* flow can be pushed through an edge ($Capacity - CurrentFlow$).
    * **Backward Capacity:** How much flow can be **undone** or pushed back ($CurrentFlow$). This allows the algorithm to correct earlier "greedy" mistakes.

### **The Logic**
The fundamental idea is to keep searching for an augmenting path. If a path exists, we can improve our total flow. If no path exists, we have reached the maximum flow.

**Steps:**
1.  Initialize total flow to 0.
2.  **Search** for an augmenting path from Source to Sink in the residual graph.
3.  **Bottleneck:** Find the minimum residual capacity along that path (the "bottleneck").
4.  **Augment:**
    * Increase flow on forward edges by the bottleneck amount.
    * Decrease flow (or increase residual capacity) on backward edges.
5.  **Repeat** steps 2-4 until no augmenting path can be found.

### **Implementation Variations**
The original Ford-Fulkerson method does not specify *how* to find the augmenting path.

* **DFS (Depth-First Search):** The standard "naive" implementation. It is easy to code but can be inefficient if it picks long, winding paths.
* **BFS (Breadth-First Search):** This specific implementation is called the **Edmonds-Karp Algorithm**. It always finds the *shortest* augmenting path (in terms of number of edges), making it more stable and guaranteeing polynomial time complexity.


#### **Time Complexity**
The complexity depends heavily on the search strategy used:

* **Standard (DFS):** $O(E \cdot f^*)$
    * $E$: Number of edges.
    * $f^*$: The maximum flow value in the network.
    * *Risk:* If capacities are large integers, the algorithm might increment flow by 1 at a time, leading to extremely slow performance.

#### **Space Complexity**
* **$O(V + E)$**
    * Required to store the graph (Adjacency List) and the `visited` array during traversal.

That's all! ))

## LeetCode

I've completed daily task **1975. Maximum Matrix Sum**.

Regarding today's algorythm , I haven't solved anything.
Just tested my alogrithm on `Gemini` generated test for it.

That's all for today)

----

## LetCode problems

#### My implementation of Ford-Fulkerson
```python

class FordFulkerson:
    def __init__(self , n):
        self.size = n
        self.graph = [[] for _ in range(n)]
        self.visited = [0] * n

    def add_edge(self, u , v ,cap):
        forward = [ v , cap , 0 , len(self.graph[v]) ] # v, cap, current_flow, rev_idx
        backward = [ u , 0 , 0 , len(self.graph[u]) ]

        self.graph[u].append(forward)
        self.graph[v].append(backward)

    def dfs(self , u  , t , flow ):
        if u == t:
            return flow

        self.visited[u] = 1
        for i in range(len(self.graph[u])):
            v , cap , cur_flow , idx = self.graph[u][i]

            if not self.visited[v] and cap - cur_flow > 0:
                neck = self.dfs( v, t , min(flow ,  cap - cur_flow ))

                if neck > 0:
                    self.graph[u][i][2] += neck
                    self.graph[v][idx][2] -= neck
                    return neck

        return 0

    def max_flow(self, s, t):
        max_flow = 0

        while True:

            self.visited = [0] * self.size
            path = self.dfs(s, t, float('inf'))

            if path == 0:
                break

            max_flow +=path

        return max_flow

```

#### 1975. Maximum Matrix Sum
```python

from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        min_abs = float('inf')
        neg_count = 0

        for row in matrix:
            for val in row:
                abs_val = abs(val)
                total_sum += abs_val

                if abs_val < min_abs:
                    min_abs = abs_val

                if val < 0:
                    neg_count += 1

        if neg_count % 2 != 0:
            return total_sum - (2 * min_abs)

        return total_sum

```
____
