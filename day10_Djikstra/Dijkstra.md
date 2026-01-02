### Description

Dijkstra's algorithm is a greedy algorithm used to find the shortest path from a single source node to all other nodes in a weighted graph.

It maintains smallest distance to every node (initialized to infinity) and iteratively improve these aproximation. At every step, the algorithm selects the unvisited node with the smallest distance, visits its neighbors, and updates their distances if a shorter path is found.

---

### Approaches

There are several ways to implement this algorithm and each of them has different 
[complexity](#complexity). The choice of data structure directly affects the algorithm’s performance.

#### Priority Queue (Binary Heap)

This is the most common and practical implementation.
Distances are stored in a MinHeap, allowing efficient extraction of the closest unvisited node.
Each edge relaxation may insert a new entry into the heap.
This approach offers good performance and is widely used in practice. 

```python
import heapq

def dijkstra(graph: dict, nodes: list, start):
    path_len = {v: float("inf") for v in nodes}
    path_len[start] = 0
    parents = {v: None for v in nodes}
    minHeap = [[0, start]]

    while minHeap:
        w1, v1 = heapq.heappop(minHeap)
        if w1 > path_len[v1]:
            continue

        for v2, w2 in graph[v1]:
            weight = w2 + w1
            if weight < path_len[v2]:
                path_len[v2] = weight
                parents[v2] = v1
                heapq.heappush(minHeap, (weight, v2))
    return  path_len, parents

```

#### Priority Queue (Fibonacci Heap)
A theoretical optimization of Dijkstra’s algorithm.
It improves performance by supporting O(1) amortized decrease-key operations, which reduces the total complexity.
Despite better asymptotic bounds, it is rarely used in practice due to implementation complexity and large constant factors. 

Fibonacci Heap structure
```python
class FibNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class FibonacciHeap:
    def __init__(self):
        self.nodes = []

    def insert(self, node):
        self.nodes.append(node)

    def extract_min(self):
        min_node = min(self.nodes, key=lambda x: x.key)
        self.nodes.remove(min_node)
        return min_node

    def decrease_key(self, node, new_key):
        node.key = new_key

    def is_empty(self):
        return len(self.nodes) == 0
```
Dijkstra Algorithm
```python
def dijkstra_fibonacci_heap(graph: dict, nodes: list, start):
    heap = FibonacciHeap()

    dist = {v: float("inf") for v in nodes}
    parent = {v: None for v in nodes}
    handles = {}

    dist[start] = 0

    for v in nodes:
        node = FibNode(dist[v], v)
        heap.insert(node)
        handles[v] = node

    while not heap.is_empty():
        min_node = heap.extract_min()
        u = min_node.value

        for v, w in graph.get(u, []):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heap.decrease_key(handles[v], dist[v])

    return dist, parent
```

#### Linear Scan (Array)
The simplest approach.
At each step, the algorithm linearly scans all unvisited vertices to find the one with the smallest distance.
This method is easy to implement but inefficient for large graphs.
```py 
def dijkstra_linear(graph: dict, nodes: list, start):
    dist = {v: float("inf") for v in nodes}
    parent = {v: None for v in nodes}
    visited = set()

    dist[start] = 0

    for _ in range(len(nodes)):
        u = None
        min_dist = float("inf")

        for v in nodes:
            if v not in visited and dist[v] < min_dist:
                min_dist = dist[v]
                u = v

        if u is None:
            break

        visited.add(u)

        for neighbor, weight in graph.get(u, []):
            if neighbor not in visited:
                new_dist = dist[u] + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    parent[neighbor] = u

    return dist, parent
```

___

### Complexity

Let  be the number of vertices and  be the number of edges.

| Approach                        | Time Complexity     | Space Complexity |
|---------------------------------|---------------------|------------------|
| Priority Queue (Binary Heap)    | $O((E + V) \log V)$ | $O(V+E)$         |
| Priority Queue (Fibonacci Heap) | $O(V \log V + E) $  | $O(V + E)$       |                  |
| Linear Scan (Array)             | $ O(V^2)   $        | $ O(V) $         |
---

### Pros
- Guarantees the shortest path in graphs with non-negative edge weights.  
- Flexible: works with both Heap and Array data structures.  
- Easy to understand conceptually.  

### Cons
- Doesn't work with negative numbers.
- Linear Scan version is inefficient for large graphs $O(V^2)$.
- Not suitable for all-pairs shortest path problems.
___

### Alternatives

1. A* (A-Star) Search variation's:
* *Use when:* You know the target node and have a heuristic (like Euclidean distance on a map). It directs Dijkstra toward the goal, saving massive amounts of time.

2. Bellman-Ford Algorithm:
* *Use when:* The graph has negative edge weights. It is slower (O(V*E)) but can detect negative cycles.

3. BFS (Breadth-First Search):
* *Use when:* The graph is unweighted. BFS is O(V+E) and simpler.

4. Floyd-Warshall:
* *Use when:* You need shortest paths between all pairs of nodes (O(V^3)).

---

### When to Use
- When you need the shortest path from a single start point to all other nodes in a graph.  
- When all edge weights are non-negative.  
- When the graph is weighted.
___

### Related LeetCode Problems

* 743. Network Delay Time (Medium) - *The classic "hello world" of Dijkstra.*

* 778. Swim in Rising Water (Hard) - *Problem often solved with Modified Dijkstra.*
