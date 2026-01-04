### Description
The Bellman-Ford algorithm is used to find the shortest paths from one source to all other vertices in a weighted graph.
Unlike Dijkstra, it supports negative edge weights, which makes it useful in scenarios with discounts, bonuses, or penalties.

The algorithm works by relaxing all edges multiple times. During each relaxation, we try to improve the current known cost to reach a vertex using another edge. Because some paths may depend on others, a single pass is not enough.

By repeating this process, Bellman-Ford guarantees that all shortest paths are found, as long as there are no negative cycles reachable from the source.
___
### Approaches
1. Initialize the cost to all vertices as infinity, except the source vertex which is set to 0.
```python
predecessor = {v: None for v in nodes}
cost = {v: float("inf") for v in nodes}
cost[start] = 0
```
2. Repeat the relaxation process n − 1 times, where n is the number of vertices.
```python 
for i in range(len(nodes) - 1):
```
3. On each iteration, go through all edges and update the cost if a cheaper path is found.
```py
flag = False
for u, v, weight in edges:
    if cost[u] != float('inf') and cost[u] + weight < cost[v]:
        cost[v] = cost[u] + weight
        predecessor[v] = u
        flag = True
```
4. If during an iteration no values change, the algorithm can stop early.
```py 
if not flag:
    break 
```
5. After the final loop make one aditional check to find the negative cycles and if the are there return message about it
```py 
for u, v, weight in edges:
    if cost[u] != float("inf") and cost[u] + weight < cost[v]:
        return -1
```
6. Return the result
```py
return cost, predecessor
```

___
### Complexity

| Time Complexity   | Space Complexity |
|-------------------|------------------|
| $O(V\cdot E)$     | $O(V+E)$         |


___
### Pros
1) **Handles negative weights:** Unlike other algorithms, it can handle edges with negative weights. It also detects negative weight cycles.
2) **Simple:** The logic is straightforward and easy to implement.
3) **K-Edges Constraint:** Allows finding the shortest distance using at most *K* edges.
___
### Cons:
1) **Slow:** Time complexity is $O(V \cdot E)$, which is much slower than Dijkstra's algorithm.
2) **Redundant Calculations:** Performs many unnecessary relaxation steps if the graph is already optimized early.
___
### Alternatives
1) **Dijkstra:** Great and fast, but cannot handle negative edges.
2) **Floyd-Warshall:** Best for All-Pairs Shortest Path on small graphs.
3) **BFS:** Best for unweighted graphs.
4) **SPFA:** An optimized version of Bellman-Ford that uses a Queue to avoid redundant checks.
___
### When to Use
Logically, you use it when you can utilize its specific pros:
1) When the graph has negative weight edges.
2) To detect negative cycles in the graph.
3) When there is a limit on the number of edges (e.g., "at most K stops").
4) On small graphs where implementation speed matters more than execution speed.
___
### Related Problems
* **787. Cheapest Flights Within K Stops** - Core Use Case (utilizes the K-edges property).
* **743. Network Delay Time** - Good for practice (though Dijkstra is preferred).
* **1334. Find the City With the Smallest Number of Neighbors** - Can be solved using Bellman-Ford (due to small constraints).
* **1514. Path with Maximum Probability** - Requires modifying the relaxation logic, but preserves the core idea.