# Day 3
___
This is the third day of our challenge, and I already feel tired.  
Today I didn't do too much, but the difficulty of LeetCode problems really frustrated me.  
I had planned to do much more than I actually managed.  

In my plans were:
1. [ ] Build the pin-code program with `argparse`
2. [x] Retake **pandas** course on `haggle`
3. [ ] Start a course on `haggle` about **data visualization**
4. [ ] Research how Christmas is celebrated in Ukraine
5. [ ] Read a chapter of the `Grokking Algorithms` book
6. [ ] Learn `linked lists`
7. [x] Do LeetCode problems

All that I actually did was retake half of the `pandas` course 
and solve several problems on LeetCode.  

I started to understand the basics of `pandas` and I hope I will do that research 
in the near future. I promised my teacher, Anastasia, that I would, so I suppose 
I have to do it. In addition, I feel that my programming skills are developing.  

To continue this challenge, I want to create a reward system for myself that will motivate me to study.  
I was thinking of a system where for every day of my challenge I would save **$100** for my summer travel.  
But to be honest, I can't complete the travel without any risks with less than **$3000**, so I'm thinking about 
how to relate this challenge to the decision of buying a PowerMeter for my bike. I will think about it.

## LeetCode problems

### 219. Contains Duplicate II
Given an integer array nums and an integer k, return true if there are two distinct
indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

```
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    window = set()
    for i, num in enumerate(nums):
        if num in window:
            return True
        window.add(num)
        if len(window) > k:
            window.remove(nums[i - k])
    return False
```

### 1652. Defuse the Bomb

You have a bomb to defuse, and your time is running out! Your informer will provide you with
a circular array code of length of n and a key k.
To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.
If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0]
is code[n-1].
Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!
```
def decrypt(code: list[int], k: int) -> list[int]:
    new_code = []
    if k > 0:
        initial_sum = 0
        for j in range(1, k + 1):
            initial_sum += code[j % len(code)]
        new_code.append(initial_sum)

        for i in range(1, len(code)):
            initial_sum = initial_sum - code[i] + code[(i + k) % len(code)]
            new_code.append(initial_sum)

    elif k < 0:
        k = -k
        initial_sum = 0
        for j in range(1, k + 1):
            initial_sum += code[-j]
        new_code.append(initial_sum)

        for i in range(1, len(code)):
            initial_sum = initial_sum - code[i - k - 1] + code[i - 1]
            new_code.append(initial_sum)

    else:
        new_code = [0] * len(code)
    return new_code
```

### 1876. Substrings of Size Three with Distinct Characters
A string is good if there are no repeated characters.
Given a string s​​​​​, return the number of good substrings
of length three in s​​​​​​.
Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
A substring is a contiguous sequence of characters in a string.
```
def countGoodSubstrings(s: str) -> int:
    l, r, res = 0, 3, 0
    while r <= len(s):
        if len(set(s[l:r])) == 3:
            res += 1
        l+=1
        r+=1
    return res
```

### 1984. Minimum Difference Between Highest and Lowest of K Scores
You are given a 0-indexed integer array nums, where nums[i] represents the
score of the ith student. You are also given an integer k.
Pick the scores of any k students from the array so that the difference
between the highest and the lowest of the k scores is minimized.
Return the minimum possible difference.

```
def minimumDifference(nums: list[int], k: int) -> int:
    nums.sort()
    l, r, min_dif = 0, k-1, nums[-1]
    while r < len(nums):
        cur_dif = nums[r] - nums[l]
        min_dif = min(cur_dif, min_dif)
        l+=1
        r+=1
    return min_dif
```

### 187. Repeated DNA Sequences
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.
Given a string s that represents a DNA sequence, return all the 10-letter-long sequences
(substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

```
def findRepeatedDnaSequences(s: str) -> list[str]:
    parts = set()
    l, r = 0, 10
    result = []
    while r <= len(s):
        if s[l:r] in parts and s[l:r] not in result:
            result.append(s[l:r])
        parts.add(s[l:r])
        l += 1
        r += 1
    return result
```


### 904. Fruit Into Baskets
You are visiting a farm that has a single row of fruit trees arranged from left to right.
The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
You only have two baskets, and each basket can only hold a single type of fruit.
There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree
(including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

```
def totalFruit(fruits: list[int]) -> int:
    l = r = maximum = 0
    fruit_types = set()

    while r < len(fruits):
        fruit_types.add(fruits[r])
        if len(fruit_types) > 2:
            last_fruit_type = fruits[r - 1]
            l = r - 1
            while fruits[l] == last_fruit_type:
                l -= 1
            l += 1
            fruit_types = {fruits[r], last_fruit_type}
        maximum = max(maximum, r - l + 1)
        r += 1
    return maximum
```