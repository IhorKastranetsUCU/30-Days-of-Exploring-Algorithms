### Description

Counting Sort is a cool non-comparison algorithm that works like putting numbers
in buckets instead of comparing them against each other. It simply counts how many
times each number appears in the list using a helper "count array." When counted, 
it rebuilds the sorted list by essentially pushing out the buckets in order.
___
### Approaches

There are two main ways to code this: the "lazy" way just overwrites the 
original array with the counts, which is fast but loses the original order
of duplicates (unstable). The "think" way uses prefix sums to calculate 
exact positions in a new array, which keeps the original order intact (stable) 
but uses a bit more memory.
___
### Complexity

This algorithm is very very fast with a time complexity of **O(N+K)** , where N is 
the number of items and K is the range of values. However, it demands  space 
for the count array, so it is a bad choice if your range of numbers K is essentially 
huge in comparison to the number of items you are sorting.
___
### Pros

- **Speed** This is one of the fastest algorithms that exist. With time complexity of **O(N+K)**
where K is difference between largest and smallest values. 
- **Easy** The algorithm has only 4 steps and python implementation can take around 10 lines
- **Stability** The given array doesn't affect to the time performance

---

### Cons

- **Only integer values** Algorithm can sort only integers, both positive and negative.
If you need to apply algorythm to another data, you need to think about translating the 
data to numbers
- **Space** It takes O(K) additional space which makes it bad on the arrays with large range
___
### Alternatives

- **Bucket Sort**
- **Radix sort**
- **Hash-based counting**
___
### When to Use

**Key Indicators**:
- The input consists of integers (or values that can be mapped to integers). 
- range between the smallest and largest values is relatively small.
___
### LeetCode problems


### 75. Sort Colors
```
def sortColors(self, nums: List[int]) -> None:
      """
      Do not return anything, modify nums in-place instead.
      """
      _max = max(nums)
      countArr = [0 for _ in range(_max + 1)]

      for i in nums:
          countArr[i] += 1

      current_index = 0
      for val in range(_max + 1):
          while countArr[val] > 0:
              nums[current_index] = val
              current_index += 1
              countArr[val] -= 1
```
___
### 1365. How Many Numbers Are Smaller Than the Current Number
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
```
def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    if not nums:
        return []

    min_el = min(nums)
    max_el = max(nums)

    counts = [0] * (max_el - min_el + 1)
    for num in nums:
        counts[num - min_el] += 1
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    return [0 if num == min_el else counts[num - min_el - 1] for num in nums]
```
___
### 2037. Minimum Number of Moves to Seat Everyone
There are n availabe seats and n students standing in a room. You are given an array seats of length n,
where seats[i] is the position of the ith seat. You are also given the array students of length n,
where students[j] is the position of the jth student.
You may perform the following move any number of times:
Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position
x to x + 1 or x - 1)
Return the minimum number of moves required to move each student to a seat such that no two students
are in the same seat.

```
def minMovesToSeat(seats: List[int], students: List[int]) -> int:
    diff = [0] * max(max(seats), max(students))
    for i in students:
        diff[i - 1] += 1
    for j in seats:
        diff[j - 1] -= 1
    counter = 0
    unmached = 0
    for change in diff:
        counter += abs(unmached)
        unmached += change
    return counter
```
___
# 561. Array Partition
Given an integer array nums of 2n integers, group these integers into n pairs
(a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized.
Return the maximized sum.

```
def arrayPairSum(nums: List[int]) -> int:
    min_el = min(nums)
    max_el = max(nums)

    count = [0] * (max_el - min_el + 1)

    for num in nums:
        count[num - min_el] += 1

    min_val = 0
    l = r = 0

    while r < len(count):
        if count[r] == 0:
            r += 1
            continue
        if count[l] == 0:
            l += 1
            continue
        if l == r and count[r] < 2:
            r += 1
            continue

        min_val += l + min_el
        count[l] -= 1
        count[r] -= 1

    return min_val
```
___

### 1122. Relative Sort Array
Given two arrays arr1 and arr2, the elements of arr2 are distinct,
and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

```
def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    values = {key: 0 for key in arr2}
    rest = []
    for i in arr1:
        if i in values:
            values[i] += 1
        else:
            rest.append(i)
    list_to = []
    for i in arr2:
        list_to.extend([i] * values[i])
    return list_to + sorted(rest)
```
