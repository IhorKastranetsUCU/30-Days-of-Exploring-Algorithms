# Day 22

This was the twenty secind day of the challenge.
Wednesday , tommorow will be more interesting day

---

## Segmented Tree structure
Segmented Tree is great structure which allows to handle queries (off/on line)

## LeetCode

I've completed daily task **3453. Separate Squares II**.

Regarding today's algorythm , I have tested out on **307. Range Sum Query - Mutable**

On 307 i have extended logic and add lazy propagation for add num on segment and sum on segment


That's all for today)

----

## LetCode problems

#### My implementation of Segmented Tree
```python

def build_tree(v : int , l : int , r: int , tree : list , arr : list  , mod : list):
    if l == r:
        mod[v] = 0
        tree[v] = arr[l]
        return

    m = (r-l)//2 + l
    build_tree(2*v + 1 , l , m , tree , arr , mod)
    build_tree(2*v + 2 , m + 1 , r , tree , arr  , mod)

    tree[v] = tree[2*v+1] + tree[2*v+2]

def search(v : int, l : int , r : int , LS : int , RS : int , tree : list , mod : list):
    if (LS > r or RS < l):
        return 0

    if ( l >= LS and r <= RS):
        return tree[v]

    push(v , l , r ,tree , mod)
    m = (r-l)//2 + l

    return search(2*v+1 , l , m , LS , RS , tree , mod ) + search(2*v+2 , m+1 , r , LS , RS , tree , mod)

def push(v : int  , LS : int  , RS : int , tree : list , mod : list):
    if mod[v] == 0 or LS == RS :
        return

    m = (LS+RS)//2

    mod[2*v+1] += mod[v]
    mod[2*v+2] += mod[v]


    tree[2*v+1] = tree[2*v+1]  + mod[v] * (m - LS + 1)
    tree[2*v+2] = tree[2*v+2]  + mod[v] * (RS - m)

    #tree[v] = max(tree[2*v+1] , tree[2*v+2])

    mod[v] = 0



def add_interval(v : int, l : int , r : int , LS : int , RS : int , val : int, tree : list , mod : list):
    if (LS > r or RS < l):
        return

    if (l >= LS and r <= RS):
        tree[v] += val * (r - l + 1)
        mod[v] += val
        return

    push(v , l , r ,tree , mod)

    m = (r-l)//2 + l
    add_interval(2*v+1 , l , m , LS , RS , val , tree , mod)

    add_interval(2*v+2 , m + 1 , r , LS , RS , val , tree, mod)

    tree[v] = tree[2*v+1] + tree[2*v+2]
```
____


#### 3453. Separate Squares II
```python

from typing import List

def update(v: int, tl: int, tr: int, l: int, r: int, val: int, tree: list, count: list, X: list):
    if l >= r:
        return

    if l == tl and r == tr:
        count[v] += val
    else:
        tm = (tl + tr) // 2
        update(2 * v + 1, tl, tm, l, min(r, tm), val, tree, count, X)
        update(2 * v + 2, tm, tr, max(l, tm), r, val, tree, count, X)

    if count[v] > 0:
        tree[v] = X[tr] - X[tl]
    else:
        if tl + 1 == tr:
            tree[v] = 0.0
        else:
            tree[v] = tree[2 * v + 1] + tree[2 * v + 2]


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        #compress coords
        xs = set()
        for x, y, l in squares:
            xs.add(x)
            xs.add(x + l)
        sorted_x = sorted(list(xs))
        x_map = {val: i for i, val in enumerate(sorted_x)}
        n = len(sorted_x)

        if n < 2: return 0.0

        #creating set of events
        events = []
        for x, y, l in squares:
            events.append((y, 1, x_map[x], x_map[x + l]))
            events.append((y + l, -1, x_map[x], x_map[x + l]))

        events.sort(key=lambda e: e[0])
        #declaring tree
        tree = [0.0] * (4 * n)
        count = [0] * (4 * n)

        total_area = 0.0
        history = []
        prev_y = events[0][0]
        #scan line (on leetcode - line sweep)
        for y, type, x1, x2 in events:
            dy = y - prev_y

            if dy > 0:
                width = tree[0]
                slice_area = width * dy
                total_area += slice_area
                history.append((prev_y, y, width))


            update(0, 0, n - 1, x1, x2, type, tree, count, sorted_x)
            prev_y = y

        target = total_area / 2.0
        current_area = 0.0


        #calc min
        for y1, y2, width in history:
            slice_area = width * (y2 - y1)
            if current_area + slice_area >= target:
                needed = target - current_area
                if width == 0: return float(y1)
                return y1 + needed / width
            current_area += slice_area

        return float(prev_y)
```
____
