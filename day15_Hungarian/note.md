# Day 15

This was the fifteenss day of the challenge.
Monday.

---

## Hungarian algorithm


### My Thoughts
Hungarian algorithm was not new for me cause my team for DM project and I have implemented it
as our Final project for this subject. But I wasn't main coder there , so it was great to try out it myself.


## Hungarian algorithm
It have the next steps:
1 ) Reduce Rows & Colums
2 ) Look for optimal assignment
2_1 ) IF no found , shift zeros
Repeat until optimal assignment is found

1. Reduce Rows and Colums means no find minim there and substract from every element in it
2. Look for optimal assigment means to find such assignmetn of zeros to works
3. Shift zeros, find min in uncovered elements by zeros lines ,
substract from other uncovered and add to the place where lines crosses.


#### **Time Complexity**

* **Optimized:** $O(N^3)$
* **Regular:** $O(N^4)$


#### **Space Complexity**
* **$O(V^2)$**
    * Required to store the matrix

That's all! ))

## LeetCode

I've completed daily task **1339. Maximum Product of Splitted Binary Tree**.

Regarding today's algorythm , I have solve **1947. Maximum Compatibility Score Sum**

That's all for today)

----

## LetCode problems

#### My implementation of Hungarian
```python

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = []

    def add_edge(self, u, v, cap):
        forward = [v, cap, 0, len(self.graph[v])]
        backward = [u, 0, 0, len(self.graph[u])]
        self.graph[u].append(forward)
        self.graph[v].append(backward)

    def bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        queue = [s]
        while queue:
            u = queue.pop(0)
            for v, cap, flow, rev in self.graph[u]:
                if cap - flow > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        return self.level[t] >= 0

    def dfs(self, u, t, pushed, ptr):
        if pushed == 0 or u == t:
            return pushed

        for i in range(ptr[u], len(self.graph[u])):
            ptr[u] = i
            v, cap, flow, rev = self.graph[u][i]

            if self.level[v] != self.level[u] + 1 or cap - flow == 0:
                continue

            tr = self.dfs(v, t, min(pushed, cap - flow), ptr)
            if tr == 0:
                continue


            self.graph[u][i][2] += tr
            self.graph[v][rev][2] -= tr
            return tr

        return 0

    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            ptr = [0] * self.n
            while True:
                pushed = self.dfs(s, t, float('inf'), ptr)
                if pushed == 0:
                    break
                flow += pushed
        return flow

class OptimalAssignmentHungarian:
    def __init__(self, matrix):
        self.n = len(matrix)
        self.matrix = [row[:] for row in matrix]
        self.added_edges = [[False] * self.n for _ in range(self.n)]
        self.dinic = None

    def reduction(self):
        for i in range(self.n):
            r_min = min(self.matrix[i])
            for j in range(self.n):
                self.matrix[i][j] -= r_min

        for j in range(self.n):
            c_min = min(self.matrix[i][j] for i in range(self.n))
            for i in range(self.n):
                self.matrix[i][j] -= c_min

    def get_vertex_cover(self):
        row_covered = [False] * self.n
        col_covered = [False] * self.n


        for i in range(self.n):
            if self.dinic.level[i + 1] == -1:
                row_covered[i] = True

        for j in range(self.n):
            if self.dinic.level[self.n + 1 + j] != -1:
                col_covered[j] = True

        return row_covered, col_covered

    def shift_zeros(self, row_covered, col_covered):
        k = float('inf')
        for i in range(self.n):
            if not row_covered[i]:
                for j in range(self.n):
                    if not col_covered[j]:
                        if self.matrix[i][j] < k:
                            k = self.matrix[i][j]

        if k == float('inf') or k == 0: return

        for i in range(self.n):
            for j in range(self.n):
                if row_covered[i]:
                    self.matrix[i][j] += k
                if not col_covered[j]:
                    self.matrix[i][j] -= k

    def solve(self):
        self.reduction()

        s, t = 0, 2 * self.n + 1
        self.dinic = Dinic(2 * self.n + 2)

        for i in range(self.n):
            self.dinic.add_edge(s, i + 1, 1)
        for j in range(self.n):
            self.dinic.add_edge(self.n + 1 + j, t, 1)

        total_matching = 0

        while True:
            for i in range(self.n):
                for j in range(self.n):
                    if self.matrix[i][j] == 0 and not self.added_edges[i][j]:
                        self.dinic.add_edge(i + 1, self.n + 1 + j, 1)
                        self.added_edges[i][j] = True

            delta = self.dinic.max_flow(s, t)
            total_matching += delta

            if total_matching == self.n:
                break

            row_cov, col_cov = self.get_vertex_cover()
            self.shift_zeros(row_cov, col_cov)


        result_pairs = []
        for u in range(1, self.n + 1):
            for v, cap, flow, rev in self.dinic.graph[u]:
                if flow == 1 and v > self.n and v != t:
                    result_pairs.append((u - 1, v - (self.n + 1)))
        return result_pairs

```

#### 1339. Maximum Product of Splitted Binary Tree
```python

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        A = []

        def dfs(n):
            if not n:
                return 0

            l = dfs(n.left)
            r = dfs(n.right)

            s = l + r + n.val
            A.append(s)

            return s

        t = dfs(root)

        res = 0

        for s in A:
            res = max(res, s * (t - s))

        return res % (10**9 + 7)

```
____
