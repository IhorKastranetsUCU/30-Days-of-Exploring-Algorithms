# Day 16

This was the sixteens day of the challenge.
Monday.

---

## Tarjan algorithm
This is algorithm to find SCC (Strongly connected components)

## LeetCode

I've completed daily task **1458. Max Dot Product of Two Subsequences**.

Regarding today's algorythm , I have only solve **1192. Critical Connections in a Network**

That's all for today)

----

## LetCode problems

#### My implementation of Tarjan
```python

class TarjanSCC:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.id = 0
        self.scc_count = 0

        self.ids = [-1] * n
        self.low = [0] * n
        self.on_stack = [False] * n
        self.stack = []

        self.sccs = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def find_sccs(self):
        for i in range(self.n):
            if self.ids[i] == -1:
                self.dfs(i)
        return self.sccs

    def dfs(self, at):
        self.stack.append(at)
        self.on_stack[at] = True
        self.ids[at] = self.low[at] = self.id
        self.id += 1

        for to in self.graph[at]:
            if self.ids[to] == -1:
                self.dfs(to)
                self.low[at] = min(self.low[at], self.low[to])

            elif self.on_stack[to]:
                self.low[at] = min(self.low[at], self.ids[to])

        if self.ids[at] == self.low[at]:
            current_scc = []
            while True:
                node = self.stack.pop()
                self.on_stack[node] = False
                current_scc.append(node)
                if node == at:
                    break

            self.sccs.append(current_scc)
            self.scc_count += 1

    def find_bridges(self):
        if self.ids[0] == -1:
            self.dfs(0, -1)
        return self.bridges

```

#### 1192. Critical Connections in a Network
```python

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        tarjan = TarjanSCC(n)

        for u, v in connections:
            tarjan.add_edge(u, v)

        return tarjan.find_bridges()
```
____

#### 1458. Max Dot Product of Two Subsequences
```python

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)

        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                product = nums1[i-1] * nums2[j-1]

                dp[i][j] = max(product,dp[i-1][j-1] + product,dp[i-1][j],dp[i][j-1])

        return dp[n][m]

```
____
