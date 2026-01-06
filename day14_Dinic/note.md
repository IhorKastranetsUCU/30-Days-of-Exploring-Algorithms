# Day 14

This was the thirteen day of the challenge.
Monday.

---

## Dinic's Algorithm

Today's topic was Dinic's Algorithm.

### My Thoughts
We continue exploring Flow Network Theory. Dinic's algorithm is a significant improvement over Edmonds-Karp for computing maximum flow.

# The Dinic's Algorithm

### **Algorithm Overview**
**Dinic's Algorithm** computes the **Maximum Flow** in a flow network more efficiently than Ford-Fulkerson or Edmonds-Karp. It uses the concept of a **Level Graph** and **Blocking Flow** to push flow in phases.

### **Key Concepts**
1.  **Level Graph:** A subgraph of the residual graph that includes only edges $(u, v)$ such that $level(v) = level(u) + 1$. Levels are determining by a BFS from the Source.
2.  **Blocking Flow:** A flow in the level graph such that every path from Source to Sink contains at least one saturated edge.

### **The Logic**
Dinic's algorithm runs in phases. In each phase:
1.  Construct the **Level Graph** using **BFS** from the Source ($S$) to determine the level (distance) of each node. If the Sink ($T$) is not reachable, terminate.
2.  Find a **Blocking Flow** in the Level Graph using **DFS**. We push as much flow as possible along paths in the level graph until no more flow can be sent.
3.  Add the flow from this phase to the total max flow.
4.  Repeat until the Sink is no longer reachable in the Level Graph.

### **Complexity**
*   **Time Complexity:** $O(V^2 E)$ generally.
    *   For **Unit Networks** (capacities are 0 or 1), it runs in $O(E\sqrt{V})$.
    *   This is much faster than Edmonds-Karp's $O(V E^2)$ for dense graphs.
*   **Space Complexity:** $O(V + E)$ to store the graph and levels.

That's all! ))

## LeetCode

I've completed daily task **1161. Maximum Level Sum of a Binary Tree**.

Regarding today's algorythm, I implemented Dinic's algorithm.
Also I've managed to tackle **1349. Maximum Students Taking Exam** in both implementation.
Ford - Fulkerson and Dinic's. Below is Dinic's implementation.

----

## LeetCode problems

#### My implementation of Dinic's Algorithm
```python
from typing import List

class Dinic:
    def __init__(self , n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = []

    def add_edge(self, u , v , cap):
        forward  = [ v , cap  , len(self.graph[v]) ]

        backward  = [ u , 0  , len(self.graph[u]) - 1  ]

        self.graph[v].append(backward)
        self.graph[u].append(forward)

    def bfs(self, s , t):
        self.level= [-1] * (self.n)
        self.level[s] = 0

        q = Queue([s])

        while q:
            u = q.pop_front()
            for v, cap , rev in self.graph[u]:
                if cap > 0 and self.level[v] < 0 :
                    self.level[v] = self.level[u] + 1
                    q.append(v)

        return self.level[t] >= 0

    def dfs(self, u, t ,flow , ptr):
        if u == t or flow == 0:
            return flow

        for i in range(ptr[u] , len(self.graph[u]) ):
            ptr[u] = i

            v, cap , rev = self.graph[u][i]

            if self.level[v] == self.level[u] + 1 and cap > 0:
                pushed = self.dfs(v, t , min(flow , cap) ,ptr)

                if pushed > 0:
                    self.graph[u][i][1] -= pushed
                    self.graph[v][rev][1] += pushed
                    return pushed

        return 0

    def max_flow(self, s, t):
        max_f = 0
        while self.bfs(s,t):
            ptr = [0] * self.n
            while True:
                pushed = self.dfs(s,t, float('inf') ,ptr)
                if pushed == 0:
                    break
                max_f +=pushed

        return max_f

class Queue:
    def __init__(self, array=None):
        if array is None:
            self.q = []
        else:
            self.q = list(array)
        self.index = 0

    def append(self, el):
        self.q.append(el)

    def pop_front(self):
        if self.index >= len(self.q):
            return None

        val = self.q[self.index]
        self.index += 1
        return val

    def __len__(self):
        return len(self.q) - self.index

    def __bool__(self):
        return self.index < len(self.q)
```

#### 1349. Maximum Students Taking Exam
```python

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        row = len(seats)
        cols = len(seats[0])

        s = row * cols
        t = row * cols + 1

        mx = Dinic(t+1)


        total = 0

        directions = [
            (0 , -1) , ( 0 , 1),
            (-1, -1) , (-1 , 1),
            (1,-1) , (1 , 1)
        ]

        for r in range(row):
            for c in range(cols):
                if seats[r][c] == "#":
                    continue

                total+=1
                u = r*cols + c

                if c%2 == 0:
                    mx.add_edge(s , u , 1)
                    for dr , dc in directions:
                        nr , nc = r + dr , c+ dc
                        if 0 <= nr < row and 0 <= nc < cols:
                            if seats[nr][nc] == '.':
                                v = nr * cols + nc
                                mx.add_edge(u , v , float('inf') )
                else:
                    mx.add_edge( u , t , 1)

        res = mx.max_flow(s,t)

        return total - res


```
____

#### 1161. Maximum Level Sum of a Binary Tree
```python

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def dfs(v : TreeNode , level , array : list):
            if not v:
                return


            #print(level , v.val)
            if len(array) > level:
                array[level] += v.val

            else:
                #print("--------")
                #print(level , v.val)
                array.append(v.val)

            level += 1
            dfs(v.left ,level , array)
            dfs(v.right , level , array)

            return


        array = [0]
        dfs(root , 0 , array)
        s = -1 * float('inf')
        i_max = 0
        for i, el in enumerate(array):
            if el > s:
                s = el
                i_max = i
            print(s , i_max ,el )

        return i_max+1

```
____
