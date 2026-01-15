# Day 23

This was the twenty third day of the challenge.
Thursday , I have finished all exams.

---

## Line Sweep algorithm
Line sweep (idk but always called it scanning line) ,
Idea , to sweep line from left to right and call events which change something.


## LeetCode

I've completed daily task **2943. Maximize Area of Square Hole in Grid**.

Regarding today's algorythm , I have tested out on **1094. Car Pooling**




That's all for today)

----

## LetCode problems

#### My implementation of Scan line for Car Pooling
```python
from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        event_arr = []
        for num , par , to in trips:
            event_arr.append( (par, 1 , num)  )
            event_arr.append( (to , -1 , num) )

        curr_cap = capacity

        event_arr = sorted(event_arr , key = lambda x : (x[0] , x[1] , x[2]) )
        print(event_arr)
        for x , type , num in event_arr:
            if type == 1:
                curr_cap -= num
            else:
                curr_cap += num

            if curr_cap < 0:
                return False

        return True

if __name__ == "__main__":
    print(Solution.carPooling(Solution , [[2,1,5],[3,3,7]] , 4))
```
____


#### 2943. Maximize Area of Square Hole in Grid
```python

from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        start = hBars[0]
        maxlen = 1
        length = 1
        for  i, el in enumerate(hBars):
            if i == 0: continue
            if el == start + 1:
                length += 1
                maxlen = max(maxlen , length)
            else:
                length = 1

            start = el

        s1 = maxlen + 1
        #print(s1)

        vBars.sort()
        start = vBars[0]
        maxlen = 1
        length = 1
        for  i, el in enumerate(vBars):
            if i == 0: continue
            if el == start + 1:
                length += 1
                maxlen = max(maxlen , length)
            else:
                length = 1

            start = el

        s2 = maxlen+1
        #print(s2)

        return min(s1,s2) * min(s1,s2)
```
____
