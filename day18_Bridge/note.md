# Day 18

This was the eighteens day of the challenge.
Saturday.

---

## Bridge algorithm
This algo is used to find bridges in graph )

## LeetCode

I've completed daily task **712. Minimum ASCII Delete Sum for Two Strings**.

Regarding today's algorythm , I have only resubmitted **1192. Critical Connections in a Network**

That's all for today)

----

## LetCode problems

#### My implementation of Tarjan
```python

class BridgeFind:
    def __init__(self , n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.used = [0] * self.n
        self.tin = [0] * self.n
        self.tmin = [0] * self.n
        self.timer = 0
        self.bridges = []

    def add_edge(self , u , v , idx ):
        self.graph[u].append((v,idx))
        self.graph[v].append((u,idx))

    def dfs(self , v , par , edge ):
        self.used[v] = 1
        self.tin[v] = self.tmin[v] = self.timer
        self.timer += 1

        for to , e in self.graph[v]:
            if e == edge:
                continue

            if self.used[to] == 0:
                self.dfs(to ,v , e)

                self.tmin[v] = min(self.tmin[v], self.tmin[to])

                if self.tmin[to] > self.tin[v]:
                    self.bridges.append(e)
            else:
                self.tmin[v] = min(self.tmin[v], self.tin[to])

    def find_bridges(self):
        for i in range(self.n):
            if self.used[i] == 0:
                self.dfs(i, -1, -1)

        return sorted(self.bridges)

```

#### 1192. Critical Connections in a Network
```python
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        b = BridgeFind(n)

        for i , ( v , to )  in enumerate(connections):
            b.add_edge(v , to , i)

        arr = b.find_bridges()
        f = []
        for i in arr:
            f.append(connections[i])

        return f

```
____

#### 712. Minimum ASCII Delete Sum for Two Strings
```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])

        for j in range(1, m + 1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    delete_s1 = dp[i-1][j] + ord(s1[i-1])
                    delete_s2 = dp[i][j-1] + ord(s2[j-1])
                    dp[i][j] = min(delete_s1, delete_s2)

        return dp[n][m]
```
____
