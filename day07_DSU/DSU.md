# Disjoint Set Union

## Description
Disjoint Set Union is a data structure which creates connections between nodes.

First, you initialize a number of separated elements. Then, you can connect them using
the `union` function. It creates a tree where one element is a parent and another is a
child.

You can add as many nodes as you want from those you have, but all of them will have the
same parent. You can also combine two graphs by making a `union` between their parents.
Then, one of the nodes becomes a child together with all related children.

Therefore, if you try to union a node that already has children, it will still become a
child of the main parent.
___
## Approaches
There are three implementation versions with different ways of representing connections, 
but all of them follow the same principle: keeping all nodes in the graph connected to their parent.
### Version 1
Saves deep, and makes a left node a parent and second node a child in `union` function.
```python
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.parent[y] = x
```


### Version 2:

Saves deep, and makes `union` by checking which tree has more nodes. 
Each node keeps information about its set representative.
```python 
class UnionFind2:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x > y:
            self.parent[y] = x
            self.size[x] += self.size[y]
        else:
            self.parent[x] = y
            self.size[y] += self.size[x]
```

### Version 3: 
Breaks deap by connection all the relative nodes directly to the its representative.
```python 
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
```
___
## Complexity

#### Time complexity
- **Version 1** –$O(n)$
- **Version 2**– $O(\log n)$
- **Version 3** – $O(\alpha(n))$, where $\alpha$ is the inverse Ackermann function
(effectively constant for all practical input sizes)
#### Space complexity : $O(n)$
___

## Pros:

- **Speed:** It is blazingly fast. The structure ensures $O(\alpha(N))$ time complexity, where $\alpha(N)$ is so small (less than 5) that you can count it on one hand for any practical input size.
- **Simplicity:** Minimal code, few operations, and very easy to implement.
- **Online / Dynamic:** Works online, meaning you don't need to rebuild the full graph to check connectivity when new edges are added.
___
## Cons:

- **Merge-Only (Hard to Split):** You can merge sets, but you cannot split them. (It is possible with "Rollback DSU," but that is too complicated for now.)
- **Undirected Only:** Works only with equivalence relations (undirected graphs), not directed ones.
- **Limited Info:** Only tells us if objects are in the same group. We don't know the path or the distance between them.
___
## Alternatives

- **BFS / DFS (Graph Traversal):**  
  Used to check if a connection exists between two objects on a static graph.  
  **Comparison:** Slightly faster if the graph doesn't change, but significantly slower when the graph changes dynamically.

- **Floyd-Warshall:**  
  Tells if one node can reach another and gives full connectivity data for every pair.  
  **Comparison:** Much slower $O(N^3)$, but provides more detailed information.
___
## When to Use

- When you need to work with connectivity in real-time (Dynamic Connectivity).  
- Checking if adding an edge creates a cycle in an undirected graph.  
- Grouping or clustering elements.  
- Finding the Minimum Spanning Tree (Kruskal's Algorithm).
___
## Related LeetCode Problems

- **Satisfiability of Equality Equations** – a great example of basic DSU usage.  
- Link to a useful set of DSU problems on LeetCode: [https://leetcode.com/problem-list/5lhmb4mj/](https://leetcode.com/problem-list/5lhmb4mj/)
