# Day 4
___
That was very lazy day. I started day with creating [password generator](password_generator.py) 
as a first program with module argparse. I understood a little bit how it works and now
I am able to bilde app the can be launched from terminal with nessecery and optional arguments.
Another good thing about that program is practising with `random` module and learning
basic staff from library string which I used to take all the lower/upper case symbols, digits 
and special characters. From `random` I used methods **choices**, **choice**, **shuffle**.

Then I implamented counting sort by myself and started to solve problems on LeetCode. That 
was very tricky LeetCode chapter because some of the **Fundamental** problems were honestly
more difficult than **Intermediate**. I managed to solve half of the problems by myself and 
this time I finally got my own ideas about solution. 

Currently I have 33/3787 solved problems
![img_3.png](img_3.png)

___
## Password Generator
![img_1.png](img_1.png)
#### Password with length 10, with upper and lower case letters, digits and special characters

```python3 password_generator.py 10 -u -l -d -s```
>Sj<WI`4m8F

#### Password with length 20, with only lower case letters, digits and special characters
```python3 password_generator.py 20 -l -s -d```
>tei7a&xrqsq/&n14f=6{

#### Password with length 15, with digits only
```python3 password_generator.py 15 -d```
> 736964566818813
___

## LeetCode problems

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

### 2037. Minimum Number of Moves to Seat Everyone
There are n availabe seats and n students standing in a room. You are given an array seats of length n,
where seats[i] is the position of the ith seat. You are also given the array students of length n,
where students[j] is the position of the jth student.
You may perform the following move any number of times:
Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position
x to x + 1 or x - 1)
Return the minimum number of moves required to move each student to a seat such that no two students
are in the same seat.

```def minMovesToSeat(seats: List[int], students: List[int]) -> int:
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


### 1122. Relative Sort Array
Given two arrays arr1 and arr2, the elements of arr2 are distinct,
and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

`def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
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
`
