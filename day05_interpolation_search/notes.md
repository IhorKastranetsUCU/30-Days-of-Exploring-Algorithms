# Day 5
___
- [Maksym’s Notes](#Maksym)
- [Ihor’s Notes](#Ihor)
___
## Maksym


This was the fifth day of the challenge. Everything is okay. I am working on my mental health to be
productive during the next semester. Today I've completed a couple of tasks and relaxed because today is
Sunday.

---

## Interpolation Search

Today's topic was **Interpolation Search**. "Interpolation" sounds like something related to math, and that
turned out to be true.
The idea is that if the data is close to the interpolated values, the algorithm can effectively find the
needed number. This is great because if the data is good enough, it gives an incredibly fast **$O(\log(\log N))$**.
But the constraints on the data are very strong; when the data is not good, it goes to Linear Time.

---

## LeetCode

I've completed the daily problem **1351. Count Negative Numbers in a Sorted Matrix**.
Also, relevant to today's topic, I've submitted **704. Binary Search** with my interpolation search.
I also solved **164. Maximum Gap**, a task with the idea of Interpolation Search combined with Bucket Sort.
---

## LeetCode

----

I've completed daily problem **1351. Count Negative Numbers in a Sorted Matrix**.
Also relative to todays topic I've submitted **704. Binary Search** with my interpolation search.
Task with idea of Interpolationg search combined with ideas of bucket sort **164. Maximum Gap**


----

## LetCode problems

#### 1351. Count Negative Numbers in a Sorted Matrix
```
def countNegatives(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    count = 0

    row, col = m - 1, 0

    while row >= 0 and col < n:
        if grid[row][col] < 0:
            count += (n - col)
            row -= 1
        else:
            col += 1

    return count
```
___

#### 704. Binary Search
```
def search(self, nums: List[int], target: int) -> int:
    arr = nums
    x = target
    low , high = 0 , len(arr) - 1

    #iteration
    i = 0

    while low <= high and x >= arr[low] and x <= arr[high]:
        i+=1

        if low == high:
            if arr[low] == x:
                return low
            return -1

        pos = low + ( (x - arr[low]) * (high - low) // (arr[high] - arr[low]) )

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1
```
___

#### 164. Maximum Gap
```
def maximumGap(self, nums: List[int]) -> int:
    min_val , max_val = min(nums) , max(nums)

    if min_val == max_val:
        return 0

    bucket_size = max(1, (max_val - min_val) // (len(nums) - 1))

    bucket_num = (max_val - min_val) // bucket_size + 1

    buck_min = [-1] * bucket_num
    buck_max = [-1] * bucket_num

    for num in nums:
        index = (num - min_val) // bucket_size

        if buck_min[index] == -1:
            buck_min[index] = num
            buck_max[index] = num
        else:
            buck_min[index] = min(buck_min[index] , num)
            buck_max[index] = max(buck_max[index] , num)

    max_g = 0
    prev_g = buck_max[0]


    for i in range( 1, bucket_num ):

        if buck_min[i] == -1:
            continue

        curr_gap =  buck_min[i] - prev_g
        max_g = max(max_g , curr_gap)

        prev_g = buck_max[i]

    return max_g
```
___

#### My implementation of Interpolate Search
```
def interpolation_search(arr : list[int] , x : int) -> int:
    low , high = 0 , len(arr) - 1

    #iteration
    i = 0

    while low <= high and x >= arr[low] and x <= arr[high]:

        if low == high:
            if arr[low] == x:
                return (low, i)
            return -1

        i+=1
        pos = low + ( (x - arr[low]) * (high - low) // (arr[high] - arr[low]) )

        if arr[pos] == x:
            return ( pos , i)

        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1
```
___

## Ihor

So… I’m cooked. That was the least productive day of the whole holiday.
However, I managed to learn the logic of the interpolation search algorithm and 
understood its weak sides. Still, the difficulty of LeetCode problems makes me feel discouraged.

On the other hand, I started planning my travels. I decided to try Couchsurfing, 
and I suppose it’s going to give me some motivation for studying. In addition,
I’m really happy that I’m finally leaving home and going back to Lviv.

I want to go to the library and lock myself in there to study. I also clearly 
understand that without variety, I will burn out for sure. Tomorrow I have a train at 7:30 AM, 
so I’m going to read algorithm books on the way.