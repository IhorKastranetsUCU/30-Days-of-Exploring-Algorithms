# Day 4

This was the fourth day of the challenge. The mood was great after visiting grandma and grandpa. This day was not very productive, but the replenishment and ultimate surge from the family reunion gave me motivation and energy to continue moving forward.

---

## Counting Sort

Today's topic was - **Counting Sort**.
I've heard about non-comparison-based sorting, but imagined it slightly differently :)
Today I learned what Counting Sort, Bucket Sort, and Radix Sort are. However, I implemented only Counting Sort today.
The idea is great: what if we don't need to compare objects? This is the aspect where non-comparison sorting excels.
We create an additional structure (usually an array) to create a relative measure system, in our case an axis of natural numbers, to arrange numbers in sorted order.
Then we calculate the prefix sum of that structure to pinpoint where this number should start in the array.
As a result, knowing where the needed numbers should be placed, we place them there.

In summary, we get a couple of **O(N)** and **O(K)** loops, where K is the length of the needed structure.
It looks great, linear. However, it has its own limitations, like working with numbers, especially positive ones (this can be fixed by reassigning, but let's not focus on it).
The length of the additional structure can be enormously big, and the Time Complexity could outperform **O(N²)**.

---

## LeetCode

----

I have completed only one task : **75. Sort Colors** for implmenting inplace Counting sort.

----

## LetCode problems

#### 75. Sort Colors
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

#### Own counting sort implementation
```
def count_sort(arr : list) -> list:
    countArr = [0 for i in range(max(arr) + 1) ]
    pref_cnt = [0 for i in range(max(arr) + 1) ]
    for i in arr:
        countArr[i]+=1

    for i in range(1, max(arr) + 1):
        countArr[i] += countArr[i - 1]


    res = [0] * len(arr)
    #print(pref_cnt)

    for i in range( len(arr)-1 , -1 , -1):
        res[ countArr[ arr[i] ] - 1] = arr[i]
        countArr[ arr[i] ] = countArr[ arr[i] ] - 1

    return res
```

