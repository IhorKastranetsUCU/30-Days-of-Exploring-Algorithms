## Sliding Window Algorithm

### Description

The Sliding Window algorithm is based on the **Two Pointers** principle.  
There are two types of this algorithm: **static** and **dynamic**.

### 1. Static Sliding Window
You have a **fixed-size window**, and you move it from the start to the end of the array.
**Important note:**  
Instead of recalculating the required value from scratch for each window,  
you can **update the current value** by:
- removing the element that leaves the window
- adding the new element that enters the window
This is what differentiates the sliding window approach from the brute-force method  
and allows the algorithm to run in **O(n)** time.

### 2. Dynamic Sliding Window
You place the window at the beginning of the array and **expand it** until it no longer satisfies the given condition.

Then, you start **moving the left border** of the window until the condition becomes valid again.  
You continue this process until the right pointer reaches the end of the array.
___
### Approaches
1.	**While loop**: create variables left and right, which represent the indexes of the window.
    Then create a while loop where the variable right is supposed to be smaller than the length of the given array.
    After each iteration of the loop, increment both left and right indexes by 1.
2.  **For loop**: It also has two branches:
    1. Create a variable left and use a for loop iterated by a temporary variable r from 0 to the end of the array.
    Inside the loop, update the window using left and r as the window boundaries.
    2. Iterate over the range len(array) - k + 1, where k is the length of the given window, 
    so that each iteration represents one valid window position.

### Complexity

The main strength of the Sliding Window algorithm is reducing inefficient calculations to **O(N)** 
time complexity, which means linear time.  
It also often helps to save space, usually requiring **O(K)** additional space, where **K** represents 
information stored about the current window (sometimes referred to as the *caterpillar*).

---

### Pros

- **Efficiency:** Significantly reduces the number of repeated calculations compared
to brute-force solutions.  
- **Flexibility:** The window size can be **dynamic**, which greatly expands the range 
of problems where this approach can be applied.

---

### Cons

- **Limited Scope:** Can only be applied to **continuous data**, such as arrays or strings.  
- **Tricky Logic:** Requires careful handling of edge cases and a clear understanding of
when to **expand** or **shrink** the window.
___
### Alternatives

- Brute Force  
- Prefix Sum  
- Two Pointers
---

### When to Use

- When working with **arrays or strings**.  
- When the task involves **subarrays or substrings**.  
- When you want to optimize a brute-force solution that checks all possible continuous segments.

---

### Related LeetCode Problems

- **1876. Substrings of Size Three with Distinct Characters**  
  A perfect example of the **static sliding window** approach.

- **904. Fruit Into Baskets**  
  A great example of a **dynamic sliding window**, where you adjust the left boundary to maintain 
  a window containing only two unique elements while maximizing its size.