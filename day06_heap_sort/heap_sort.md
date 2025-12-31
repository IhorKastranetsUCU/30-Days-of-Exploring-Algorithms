# Heap Sort

## Description

Heap Sort is a comparison-based sorting algorithm that uses a **Binary Heap** data structure.  
It divides the input into a **sorted** and an **unsorted** region, and iteratively shrinks the unsorted region by extracting the largest element and moving it to the sorted region.

Heap Sort uses a "virtual" tree through mapping:  
- **Parent**: `i`  
- **Left child**: `2*i + 1`  
- **Right child**: `2*i + 2`

---

## Approaches

- **Standard two-phase approach**:
  1. Build Max Heap  
  2. Extract max and sort

- **Two implementation ways**:
  - Recursion  
  - Iteration

---
### Complexity
#### Time complexity
- **Worst case**: $O(n\log n)$
- **Average case**: $O(n\log n)$
- **Best case**: $O(n\log n)$

#### Space complexity : $O(1)$

### Pros 

- Time complexity is always $O(n \log n)$
- Space complexity is $O(1)$; it does not require extra memory
- In-place algorithm
- Can be implemented both recursively and iteratively
- Can sort any comparable data, such as integers, floats, and strings

### Cons

- Difficult and tricky to implement correctly
- Sometimes slower than alternatives because of a large constant factor
- Unstable when it comes to the order of same values

## Alternatives

- **Default**: Quick Sort or Merge Sort  
- **Exotic**: Intro Sort (used in `std::sort`) — combines Heap Sort and Quick Sort.  

---
## When to use

- When there is **no additional space** (Heap Sort uses O(1) extra space)  
- When you **cannot afford to be slower than O(n log n)**  
- When you **don’t need a fully sorted array**, only part of it
___

## Related LeetCode Problems

- **912. Sort an Array** — just to test Heap Sort  
- **215. Kth Largest Element in an Array** — use Heap Sort until the k-th largest is found  
- **347. Top K Frequent Elements** — make Heap Sort compatible with non-integer entries