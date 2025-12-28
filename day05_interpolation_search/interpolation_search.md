# Interpolation Search

## Description
Interpolation search is a **method to find the index of a target** in a sorted array 
based on the concept of binary search. It is similar to binary search, except that 
the position to check is chosen using a formula rather than the middle of the current interval.

In some scenarios that resemble real-world problems, this algorithm can be more efficient 
than binary search. It uses the following formula:

\[
\text{pos} = \left\lfloor 
l + \frac{(\text{target} - \text{array}[l]) \cdot (r - l)}{\text{array}[r] - \text{array}[l]} 
\right\rfloor
\]

Where:  
- \(l\) – left bound  
- \(r\) – right bound  
- \(\text{target}\) – the value we are looking for  
- \(\text{array}\) – the given **sorted** list of values  

It works well with **uniformly distributed integers**. Floating-point numbers
may introduce small calculation errors in Python, which can make the algorithm less reliable.

---

## Approaches
- Interpolation search can be implemented **iteratively** or **recursively**.  
- The **iterative approach** is the most common and recommended method.

---

## Complexity
- **Worst case:** \(O(n)\)  
- **Average case:** \(O(\log \log n)\)  
- **Best case:** \(O(1)\)  

---

## Pros and Cons

**Pros:**  
- Extremely fast for perfectly uniform data, approaching \(O(\log \log n)\).  
- Can find the target in just a few iterations on large datasets.  

**Cons:**  
- Performance can degrade to **linear search** with unevenly distributed data.  
- Division and multiplication operations take longer than addition or bit-shifting, 
so binary search may outperform it in small datasets or edge cases.  

---

## Alternatives
- **Binary Search:** The standard, simple, and reliable option.  
- **Ternary Search:** Used mainly for finding maxima or minima of functions rather than searching in arrays.  

---

## When to Use
- Sorted, numeric, and **uniformly distributed** large datasets.  

---

## Related LeetCode Problems
- Search in Rotated Sorted Array  
- Search Insert Position  
- First Bad Version  