
## Prefix Sum

### Description

The prefix sum algorithm is widely used for optimizing array processing when you need to compute sums of subarrays multiple times. It provides information about the sum of all elements from the start up to a given index.

Based on the original list, the algorithm returns a list of the same length, where each element at a given index contains the cumulative sum from the start up to that index.
___
### Approaches

There are a few ways to create the prefix sum list:

1. **Fixed-length list approach**:  
   - Create a list of the same length as the original, filled with zeros.  
   - Iterate through the original list, and for each position, store the sum of the previous element in the prefix sum list plus the current element from the original list.

2. **Dynamic list approach**:  
   - Create an empty list and a temporary variable `temp`.  
   - Iterate through the original list, adding each value to `temp`, and append `temp` to the prefix sum list.

Both approaches use a single loop and handle each element once.
___
### Complexity

- **Time Complexity:** O(n) — only a single loop is used, no recursion.  
- **Space Complexity:** O(n) — a new list of length n is created.
___
### Pros and Cons

**Pros (Advantages):**  
* **Constant Time:** The main advantage is that it can calculate the sum of any subarray in O(1) time, regardless of its size.  
* **Simplicity:** Very easy to implement compared to Segment Trees or Fenwick Trees.  
* **Scalability:** Works not only for addition but also for any reversible operation, such as XOR or multiplication.  

**Cons (Disadvantages):**  
* **Static Data:** Not suitable for dynamic arrays. If a single element in the original array changes, the entire prefix sum array must be rebuilt.  
* **Memory:** Requires O(N) extra space to store the prefix sum array.  
* **Overflow:** The cumulative sums can grow rapidly and may exceed the range of int64.  

---

### Alternatives

* **Simple Iteration (Brute Force):**  
  * **Description:** Loop from L to R for every query.  
  * **Comparison:** Very slow (O(N) per query). Acceptable only for a small number of queries.  

* **Segment Tree / Fenwick Tree (Binary Indexed Tree):**  
  * **Description:** Advanced data structures arranged in a tree-like form.  
  * **Comparison:** Much better if the array is dynamic. Can handle both updates and queries in O(log N). Prefix sums are faster (O(1)) but cannot handle updates.  

* **Sparse Table:**  
  * **Description:** Mainly used for Range Minimum / Maximum Queries.  
  * **Comparison:** Works with static data like prefix sums but can handle min/max queries, whereas prefix sums are limited to addition or XOR.  

---

### When to Use

**Key Indicators:**  
* The input array is static.  
* You need to perform multiple range queries (hundreds of thousands or millions).  
* The problem involves calculating the sum, average, or XOR of a subarray.  
* Useful for 2D matrix problems (can extend to 2D prefix sums).  

---

### Example

**Scenario:** Calculate the sum of elements from index 1 to 3 (inclusive).  

**Input:**  
* Array `nums`: `[10, 20, 30, 40, 50]`  
* Query range: `[1, 3]` (values 20, 30, 40)  

**Process:**  
* **Preprocessing (Build Step):**  
  * Create the prefix sum array `P`: `[10, 30, 60, 100, 150]`  

* **Query Processing:**  
  * Formula: `Sum(L, R) = P[R] - P[L-1]`  
  * For Sum(1, 3) = `P[3] - P[0]`  
  * Calculation: `100 - 10 = 90`  

**Output:**  
* Result: `90`

___

### Related LeetCode Problems

1. **209. Minimum Size Subarray Sum**  
   Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`.


2. **1413. Minimum Value to Get Positive Step by Step Sum**  
   Given an array of integers `nums` and an initial positive value `startValue`, calculate the step-by-step sum of `startValue` plus elements in `nums` from left to right. Return the minimum positive `startValue` such that the cumulative sum never drops below 1.


3. **689. Maximum Sum of 3 Non-Overlapping Subarrays**  
   Given an integer array `nums` and an integer `k`, find three non-overlapping subarrays of length `k` with the maximum sum and return the starting indices of each subarray. Return the lexicographically smallest answer if multiple exist.
