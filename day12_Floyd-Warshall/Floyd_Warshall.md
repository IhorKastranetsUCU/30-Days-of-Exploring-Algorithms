# Floyd-Warshall


### Description

Floyd–Warshall is an algorithm to find the shortest paths between all pairs of vertices in a graph.
It works with graphs that have negative edge weights as well as regular ones.
If a negative number appears on the diagonal of the distance matrix after running the algorithm, 
it means the graph has a negative cycle.

The algorithm doesn’t require any complex data structures — it can be implemented using just 
a distance matrix and three nested loops.

### Approaches

1. **Copy the matrix:**  
Make a copy of the input distance matrix to avoid modifying the original.  
Let `n` be the number of vertices.
```python
from copy import deepcopy

def floyd_warshall(edges: list[list]):
    edges_copy = deepcopy(edges)
    n = len(edges_copy)
```

2. **Initialize the predecessor matrix:**  
Set `predecessor[i][j] = i` if there is a direct edge from `i` to `j`.  
Otherwise, set it to `None`.  
This will help reconstruct the shortest paths later.
```Py
 predecessor = [
     [None if edges_copy[u][v] == float("inf") else u for u in range(n)]
     for v in range(n)
    ]
```

3. **Three nested loops:**  
For each intermediate vertex `k`, update distances between all pairs `(i, j)`:  
     ```python
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if edges_copy[i][k] != float("inf") and edges_copy[k][j] != float("inf"):
                    if edges_copy[i][k] + edges_copy[k][j] < edges_copy[i][j]:
                        edges_copy[i][j] = edges_copy[i][k] + edges_copy[k][j]
                        predecessor[i][j] = predecessor[i][k]
     ```

4. **Check for negative cycles:**  
If any `edges_copy[i][i]` becomes negative, it indicates a negative cycle.  
You can return `-1` or handle it as needed.
```Py
 for i in range(n):
     if edges_copy[i][i] < 0:
         return -1 
```

5. **Return results:**  
Return the final distance matrix and the predecessor matrix for path reconstruction.
```Py
return edges_copy, predecessor
```

### Complexity
* **Time Complexity:** $O(V^3)$ — This is the result of three nested loops.
* **Space Complexity:** $O(V^2)$ — Required to store the $N \times N$ distance matrix.

### Pros and Cons
**Pros:**
1) **All-Pairs Solution:** Computes the shortest path between all pairs of nodes simultaneously, not just from a single source.
2) **Negative Weights:** Handles edges with negative weights correctly (unlike Dijkstra).
3) **Implementation:** Extremely simple to code (compact logic).

**Cons:**
1) **Slow:** Inefficient for large graphs. Typically unusable if $V > 500$.
2) **Negative Cycles:** Cannot find shortest paths in the presence of negative cycles (though it can detect them if a diagonal distance becomes negative).
___
### Alternatives
1) **Repeated Dijkstra:** Run Dijkstra's algorithm $V$ times (once for each node). Better for sparse graphs with non-negative weights.
2) **Johnson's Algorithm:** Uses Bellman-Ford once to handle negative weights, then runs Dijkstra for all nodes. Faster than Floyd-Warshall for sparse graphs.
___
### When to Use
1) **Small Constraints:** The number of vertices is small (typically $V \le 400$).
2) **Dense Graphs:** The graph has many edges ($E \approx V^2$), making the overhead of other algorithms less worthwhile.
3) **Adjacency Matrix:** The input is already provided as an Adjacency Matrix.
4) **Multiple Queries:** You need to answer many distance queries in $O(1)$ time after a one-time calculation.
___
### LeetCode problems

787. Cheapest Flights Within K Stops
743. Network Delay Time
1976. Number of Ways to Arrive at Destination
399. Evaluate Division
1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
1462. Course Schedule IV
