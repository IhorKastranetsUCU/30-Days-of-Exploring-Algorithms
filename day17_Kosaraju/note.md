# Day 17

This was the seventeen day of the challenge.
Friday.

---

## Kosaraju algorithm
This is algorithm to find SCC (Strongly connected components)

## LeetCode

I've completed daily task **865. Smallest Subtree with all the Deepest Nodes**.

Regarding today's algorythm , I have only solve **2360. Longest Cycle in a Graph**

That's all for today)

----

## LetCode problems

#### My implementation of Kosaraju
```python

class Kosaraju:
    def __init__(self , n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.traversal = [[] for _ in range(n)]
        self.used = [0]*self.n
        self.topsort = []

    def add_edge(self, u , v):
        self.graph[u].append(v)
        self.traversal[v].append(u)

    def topsort_dfs(self, v ):
        if self.used[v] == 1:
            return

        self.used[v] = 1

        for to in self.graph[v]:
            self.topsort_dfs(to)

        self.topsort.append(v)


    def scc_dfs(self, v , comp):
        if self.used[v] != 0:
            return

        self.used[v] = comp

        for to in self.traversal[v]:
            self.scc_dfs(to , comp)

    def scc(self):
        for i in range(self.n):
            self.topsort_dfs(i)

        self.used = [0]*self.n

        self.topsort.reverse()

        comp = 1
        for v in self.topsort:
            if self.used[v] == 0:
                self.scc_dfs(v, comp)
                comp+=1


    def bridges(self):
        bridges = []
        for v in range(self.n):
            for to in self.graph[v]:
                if self.used[v]!=self.used[to]:
                    bridges.append((v,to))
        return bridges

```

#### 2360. Longest Cycle in a Graph
```python
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)

        k = Kosaraju(n)
        for u, v in enumerate(edges):
            if v != -1:
                k.add_edge(u, v)

        k.scc()
        components = {}
        for node, comp_id in enumerate(k.used):
            if comp_id not in components:
                components[comp_id] = []
            components[comp_id].append(node)

        max_cycle = -1

        for comp_nodes in components.values():
            size = len(comp_nodes)

            if size > 1:
                max_cycle = max(max_cycle, size)
            elif size == 1:
                node = comp_nodes[0]
                if edges[node] == node:
                    max_cycle = max(max_cycle, 1)

        return max_cycle
```
____

#### 865. Smallest Subtree with all the Deepest Nodes
```python

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        def dfs(node):
            if not node:
                return (None, 0)

            left_lca, left_depth = dfs(node.left)
            right_lca, right_depth = dfs(node.right)

            if left_depth == right_depth:
                return (node, left_depth + 1)

            elif left_depth > right_depth:
                return (left_lca, left_depth + 1)

            else:
                return (right_lca, right_depth + 1)

        result_node, _ = dfs(root)
        return result_node

```
____
