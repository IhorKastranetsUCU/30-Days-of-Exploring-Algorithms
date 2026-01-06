# The Ford-Fulkerson Algorithm

### Description
Ford–Fulkerson is an algorithm used to find the **maximum flow** in a flow network.
The idea is simple:  
as long as there exists an **augmenting path** from the source to the sink with positive residual capacity,
we push flow through this path and update the residual graph.

The algorithm does not specify how to find the path — most often **BFS (Edmonds–Karp)** or **DFS** is used.

---

### **Approaches**

The "Ford-Fulkerson" method is actually a general framework. The specific implementation depends on *how* you search for the augmenting path:



1.  **DFS (Depth-First Search):** The naive implementation. It searches for *any* path. 



2.  **BFS (Breadth-First Search) - Edmonds-Karp:** This is the most common implementation. It uses BFS to always find the **shortest** augmenting path (in terms of number of edges). This guarantees the algorithm will prevent worst-case scenarios.



### **Complexity**

The complexity depends on the search strategy used:



* **Time Complexity:**

    * **DFS Variant:** $O(E \cdot f^*)$, where $f^*$ is the maximum flow value.

    * **Edmonds-Karp (BFS Variant):** $O(V \cdot E^2)$.  More stable for large capacities.

* **Space Complexity:** $O(V + E)$ to store the graph and visited arrays.

---
### Pros
- Simple and intuitive idea
- Easy to implement for small graphs
- Works well for educational purposes
- Can be adapted with different path-search strategies (BFS / DFS)

---

### Cons
- Can fall into **infinite loop** if capacities are irrational
- Time complexity is not strictly bounded in the basic version
- Performance highly depends on how augmenting paths are chosen
- Not suitable for large or dense graphs

---

### Alternatives
- **Edmonds–Karp**  
  Ford–Fulkerson + BFS  
  Guarantees polynomial time complexity: `O(V * E²)`

- **Dinic’s Algorithm**  
  Uses level graph + blocking flow  
  Much faster in practice: `O(E * sqrt(V))` or better

- **Push–Relabel (Goldberg–Tarjan)**  
  Very efficient for large networks  
  Often used in competitive programming and real systems

---

### **When to Use**

* **Network Flow Problems:** Calculating data throughput, pipeline capacity, or traffic flow.

* **Bipartite Matching:** Assigning tasks to people, matching students to seats or dating apps.

* **Constraint Satisfaction:** Problems where you need to make optimal choices under capacity limits (e.g., scheduling).

___

### **Related LeetCode Problems**

| Problem | Difficulty | Application |

| :--- | :--- | :--- |

| **[2123. Minimum Operations to Remove Adjacent Ones...](https://leetcode.com/problems/minimum-operations-to-remove-adjacent-ones-in-matrix/)** | Hard | **Min Vertex Cover.** Convert grid to Bipartite Graph $\to$ Max Flow. |

| **[1349. Maximum Students Taking Exam](https://leetcode.com/problems/maximum-students-taking-exam/)** | Hard | **Max Independent Set.** `Total Nodes - Max Flow`. |

| **[1947. Maximum Compatibility Score Sum](https://leetcode.com/problems/maximum-compatibility-score-sum/)** | Medium | **Variation.** Max Weight Matching |