# Day 1

This is the first day of the challenge. After a short discussion with Maksym,
we decided to start with simpler algorithms and implement them using LeetCode tasks.

---

## Prefix Sum

Today’s topic was a very basic but interesting algorithm — **prefix sum**.
The idea of this algorithm is to create a list of cumulative sums from the start
up to each element.\
Once you build this list, it takes **O(1)** time to compute the sum of any subarray
by subtracting the prefix sum at the left index from the prefix sum at the right index.

---

## LeetCode

I completed **7 problems**, **6 of them were prefix sum problems**
(5 Fundamental and 1 Intermediate).\
I am getting used to this platform because I had never used it before.
To be honest, I got stuck on some problems and used ChatGPT to fix my solutions.
However, this time I first tried to find the mistake myself, and only when I failed
did I use AI for help.\
In three solutions written by other people, I noticed a pattern where a temporary
value is compared with a local maximum. I used this idea in one of my solutions myself:

```python
max_sum = max(max_sum, zeros_left + ones_right)
```
I had never used anything like this before.\
Additionally, I had to use class initialization in one problem, but I still don’t fully
understand how it works internally. However, it was necessary to solve the task.
___
## FreeCodeCamp
LeetCode uses classes, which I am not very familiar with.
That is why I decided to start a Python course on FreeCodeCamp.\
I have already completed the first two topics and plan to finish the section on classes
by the end of this week. The problems so far are very simple, and I don’t think it was
strictly necessary to complete the first two topics, but I did it anyway.\
The next topics are supposed to be more complex and contain more useful information.
![img.png](img.png)
___
## Grokking Algorythms
I started reading this book three days ago while traveling home by train.\
The first three chapters were basic for me and mainly refreshed what I studied at university.
However, starting from chapter four, I realized that I was not fully confident about some topics.\
For example, I wondered why Quick Sort is often considered better than Merge Sort,
even though Merge Sort is always O(n log n), while Quick Sort has a worst-case complexity
of O(n²).\
I also learned what a hash function is and how to determine whether it is good or bad.
The next topic introduces graphs, which is especially interesting because I have never
used this data structure before.\
I am currently on page 93.

___
## LetCode problems

#### 209 Minimum Size Subarray Sum
```
def minSubArrayLen(target: int, nums: list[int]) -> int:
    n = len(nums)
    prefix_sum = [nums[0]]
    lenght = n + 1

    for i in range(1, len(nums)):
        prefix_sum.append(prefix_sum[-1] + nums[i])

    for i in range(n):
        end = n - 1
        start = i
        while start <= end:
            mid = (end + start) // 2
            subsum = prefix_sum[mid] - prefix_sum[i] + nums[i]
            if subsum >= target:
                lenght = min(mid - i + 1, lenght)
                end = mid - 1
            else:
                start = mid + 1
    return 0 if lenght > n else lenght
```
___
#### 724 Find Pivot Index
```
def pivotIndex(nums: list[int]) -> int:
    prefix_sum = []
    temp = 0
    for i in nums:
        temp += i
        prefix_sum.append(temp)
    print(prefix_sum)
    if prefix_sum[-1] - prefix_sum[0] == 0:
        return 0
    for i in range(1, len(nums)):
        right_sum = prefix_sum[-1] - prefix_sum[i]
        left_sum = prefix_sum[i-1]
        print(left_sum, right_sum)
        if right_sum == left_sum:
            return i
    return -1
```
___
#### 1422 Maximum Score After Splitting a Stringe
```
def maxScore(s: str) -> int:
    ones_right = s.count("1")
    zeros_left = 0
    max_sum = 0
    for i in range(len(s) - 1):
        if s[i] == "0":
            zeros_left += 1
        else:
            ones_right -= 1
        max_sum = max(max_sum, zeros_left + ones_right)
    return max_sum 
```