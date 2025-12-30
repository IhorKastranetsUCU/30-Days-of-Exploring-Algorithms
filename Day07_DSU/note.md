# Day 7

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


