# Day 19

This was the nineteen day of the challenge.
Sunday , before second exam period.

---

## CutVertices(Articulation Point) algorithm
This algo is used to find Articulation in graph

## LeetCode

I've completed daily task **85. Maximal Rectangle**.

Regarding today's algorythm , I have only tested on Written test.

That's all for today)

----

## LetCode problems

#### My implementation of CutVertices(Articulation Point)
```python
class CutVerticesFind:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.used = [0] * self.n
        self.tin = [0] * self.n
        self.low = [0] * self.n
        self.timer = 0
        self.cut_vertices = set()

    def add_edge(self, u, v, idx):
        self.graph[u].append((v, idx))
        self.graph[v].append((u, idx))

    def dfs(self, v, p=-1, edge_idx=-1):
        self.used[v] = 1
        self.tin[v] = self.low[v] = self.timer
        self.timer += 1
        children = 0  # Лічильник дітей для кореня

        for to, idx in self.graph[v]:
            if idx == edge_idx:
                continue

            if self.used[to]:
                # Зворотне ребро
                self.low[v] = min(self.low[v], self.tin[to])
            else:
                # Пряме ребро дерева
                children += 1
                self.dfs(to, v, idx)
                self.low[v] = min(self.low[v], self.low[to])

                if p != -1 and self.low[to] >= self.tin[v]:
                    self.cut_vertices.add(v)


        if p == -1 and children > 1:
            self.cut_vertices.add(v)

    def find_cut_vertices(self):
        self.timer = 0
        self.cut_vertices = set()
        self.used = [0] * self.n

        for i in range(self.n):
            if not self.used[i]:
                self.dfs(i, -1, -1)

        return sorted(list(self.cut_vertices))
```
____

#### 85. Maximal Rectangle
```python
from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        n = len(matrix[0])
        heights = [0] * (n + 1)
        max_area = 0

        for row in matrix:
            for i in range(n):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0

            stack = [-1]
            for i in range(n + 1):
                while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)

                stack.append(i)

        return max_area
```
____
