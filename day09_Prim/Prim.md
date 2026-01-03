Prim's Algorithm
___

### Description

Prim’s algorithm builds a **Minimum Spanning Tree (MST)** by starting from a vertex and 
growing the tree one vertex at a time.

This tree should follow next rules:
- Has the same vertices to the graph
- Doesn't have loops
- Connected – exists path between any two vertices
- Tree should have the minimum sum of weights

### Approaches

There are two main approaches: **Lazy** and **Eager**.

**1. Lazy**

1. Add all edges connected to the vertex we just processed into the Min-Heap.

2. Pop the smallest edge; if the destination node has already been visited, skip it and pop the next smallest.

* **Pros:** Easy to implement.

* **Cons:** Consumes a lot of memory (the heap grows large).

**2. Eager**

The difference is that we add only **ONE** edge per unvisited node. The idea is that if we find a shorter path to an unvisited node, we don't spam the heap with unnecessary edges we will never use; instead, we simply update the existing record (decrease-key).


* **Pros:** Keeps the heap small (O(V)).

* **Cons:** Complex to implement (requires an Indexed Priority Queue).
___
### Complexity

**Time Complexity:**

* **Lazy Binary Heap:** O(E log E)

* **Eager Binary Heap:** O(E log V) *(Note: Eager is slightly faster because V < E)*

* **Linear Search:** O(V^2)



**Space Complexity:**

* **Lazy:** O(V + E)

* **Eager:** O(V)

* **Linear:** O(V^2)

**Note:** If we know that the graph is very dense, the linear search approach is often faster.
___

### Alternatives

1. **Kruskal’s algorithm**  
   - Sorts all edges and adds them to the MST if they don’t form a cycle.  
   - Better for **sparse graphs** or when you need to check connectivity across verices.  

2. **Linear search Prim**  
   - Instead of a heap, scan all vertices to find the minimum edge.  
   - Simple but slower (O(V²)); can be faster for **very dense graphs**.  
___
### Pros and Cons
**Pros:**
1. **Better for dense graphs:** Sorting edges (as required in Kruskal's) is expensive. Prim's can efficiently scan distances without this preprocessing step.

2. **Connectivity:** It always maintains a single connected component throughout the process.

**Cons:**

1. **Sparse Graphs:** The Lazy implementation is often slower than Kruskal's on sparse graphs.

2. **Disconnected Graphs:** It does not work directly if "islands" (disconnected components) exist. Kruskal's handles this naturally.

3. **Complexity:** The optimized (Eager) version is harder to implement than the DSU used in Kruskal's.
___
### When to Use

We always aim to leverage the pros and avoid the cons; therefore:

* **Use Prim's** when the graph is dense, when you want to start from a specific node, or when you need to minimize memory usage (Eager approach).

* **Use Kruskal's** when the graph is sparse, or when you need its side effect of determining if the graph is connected.

___
### LeetCode problemd
1584. Min Cost to Connect All Points
