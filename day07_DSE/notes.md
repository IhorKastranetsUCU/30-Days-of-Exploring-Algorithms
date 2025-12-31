# Day 7

___
- [Ihor’s Notes](#Ihor)
- [Maksym’s Notes](#Maksym)
___

# Ihor

This is the seventh day of the challenge, and today I learned my first data structure called
**Disjoint Set Union (DSU)**. It is a simple representation of a tree, where each node is connected
to its parent.

I also learned the basics of **Object-Oriented Programming (OOP)** in Python and built my first
class. I didn’t implement it completely by myself because it is still very difficult for me to
design new functions, and it takes a lot of time.

Since today I had a walk with my friend Zora, I didn’t have much free time. However, I still spent
around **4 hours** trying to understand the fundamentals of this data structure and its pseudocode.
At the beginning, I had no idea what it does or how to implement it.

So, I called Maksym again and asked him for help. We used the code from
["Hello Byte"](https://www.youtube.com/watch?v=92UpvDXc8fs) as a reference, and I explained the whole
idea of the data structure to Maksym. Then we created several objects from the implemented classes,
and at that moment, everything finally clicked. 
- **[First version](DSU.py#L3-L16)** – `union` time Complexity $O(n)$
- **[Second version](DSU.py#L20-L38)** – `union` time Complexity $O(\log n)$
- **[Third version](DSU.py#L44-L71)** – `union` time Complexity $O(a(n))$ - where $a$ is some constant

I also [modified](DSU.py#L66-L72) the `union` function in final version to ensure the correct order of swapping.

```
if self.parent[x] > self.parent[y]:
    self.parent[y] = x
    self.rank[x] += 1
else:
    self.parent[x] = y
    self.rank[y] += 1
```

___
# Maksym

This was the seventh day of the challenge.
The day passed quickly. I played games with my close friends. Everything went well.

---

## Disjoint Set

Today's topic was **Disjoint Set (DSU)**.

### My Thoughts
I was already familiar with the concept of Disjoint Sets and even practiced it during this year's Advent of Code tasks.
We all know that repetition and practice make perfect. That’s all for today's thoughts.

### Algorithm
The core idea of a Disjoint Set is that, with the information that two sets cannot overlap, we can efficiently store and check whether two objects are in the same group, and if needed, merge two groups into one.
Additionally, we can store the rank of the tree for a group and its size, which can be useful in certain tasks.

**How it works:**
Every node in the set starts as its own parent. When we want to merge two groups, we follow these steps:
1.  Check if they are not already in the same group.
2.  If they are not in the same group, check which one is larger.
3.  Set the larger group as the parent of the smaller one, because it is faster to update the smaller structure.
4.  Done.

When we need to check if two objects belong to the same group, we start a traversal up to the parent node to get its "signature." If the parent nodes are the same, then the objects are in the same group.

**Efficiency:**
* To build the Disjoint Set takes **$O(N)$**, just to create the array for our objects.
* To find or merge takes only **$O(\alpha(N))$** time, due to the way we connect nodes (using path compression).

---

## LeetCode

I've completed daily problem **840. Magic Squares In Grid** , it was just implementation task of bruteforcing all possible 3x3 grids.

Ihor found set of DSU problems. I've completed problems from there, 2 mid level.

1.   **990. Satisfiability of Equality Equations**

2.   **128. Longest Consecutive Sequence**

[Link to problem set](https://leetcode.com/problem-list/5lhmb4mj)


----

## LetCode problems

#### 840. Magic Squares In Grid
```
def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def is_magic(r, c):
        if grid[r+1][c+1] != 5:
            return False

        block = []
        for i in range(3):
            block.extend(grid[r+i][c:c+3])

        if sorted(block) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False

        if (grid[r][c] + grid[r][c+1] + grid[r][c+2] != 15 or
            grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] != 15 or
            grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] != 15):
            return False

        if (grid[r][c] + grid[r+1][c] + grid[r+2][c] != 15 or
            grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != 15 or
            grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != 15):
            return False

        if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or
            grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15):
            return False

        return True

    for r in range(rows - 2):
        for c in range(cols - 2):
            if is_magic(r, c):
                count += 1

    return count
```
___

#### My implementation of Disjoint set as Class
```
class DisjointSet:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            if self.rank[root_a] < self.rank[root_b]:
                self.parents[root_a] = root_b
                self.size[root_b] += self.size[root_a]
            elif self.rank[root_a] > self.rank[root_b]:
                self.parents[root_b] = root_a
                self.size[root_a] += self.size[root_b]
            else:
                self.parents[root_b] = root_a
                self.rank[root_a] += 1
                self.size[root_a] += self.size[root_b]
            return True
        return False

```

#### 128. Longest Consecutive Sequence
```
def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique_nums = list(set(nums))

        dsu = DisjointSet(len(unique_nums))

        val_to_index = {num: i for i, num in enumerate(unique_nums)}

        for num in unique_nums:
            if (num - 1) in val_to_index:
                curr_idx = val_to_index[num]
                prev_idx = val_to_index[num - 1]
                dsu.union(curr_idx, prev_idx)

        return max(dsu.size)
```
___


#### 990. Satisfiability of Equality Equations
```
def equationsPossible(self , equations: List[str]) -> bool:
    dsu = DisjointSet(27)

    for equ in equations:
        if equ[1] == "=":
            dsu.union( ord(equ[0])-ord("a") ,ord(equ[-1])-ord("a") )

    for equ in equations:
        if equ[1] == "!":
            if dsu.find ( ord(equ[0])-ord("a") )  == dsu.find( ord(equ[-1])-ord("a") ):
                return False
    return True

```
___
