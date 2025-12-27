# Day 3

This was the third day of the challenge. The mood was great, especially after a nap after lunch. 
The day was productive. I've finally finished my term Physics homework and was able to drop that burden.

---

## Sliding Window
----

Today's topic was - Sliding Window. 
This idea can be imagined as a caterpillar crawling along an array, widening and shortening when needed. 
The main pro is that it often allows cutting time complexity to O(N) and space complexity to O(1).
From my point of view, it is just a separate example of the two-pointer approach, but LeetCode suggests it in a different topic, which is why it is here.

---

## LeetCode

----

I completed the daily task on LeetCode and one specifically for the Sliding Window approach. 
The daily problem was 2483. Minimum Penalty for a Shop; it was not hard, and the main idea was the prefix sum approach, particularly to count the number of "Y"s in the string. 
That was not hard. The task of the day was 904. Fruit Into Baskets. The Sliding Window approach was great here. 
The idea was to move ahead at every step, but when we met a third unique type, we should stop and shrink our tail until the moment there is only one element type in our caterpillar,
so we would be able to encounter the new type.

----

## LetCode problems

#### 904. Fruit Into Baskets
```
def totalFruit(self, fruits: List[int]) -> int:        
        pleft = 0
        pright = 0
        dict_fruit = {}
        max_outcome = -1
        while pright < len(fruits):
            if fruits[pright] not in dict_fruit:
                dict_fruit.setdefault(fruits[pright],0)
            dict_fruit[fruits[pright]] += 1
            while len(dict_fruit)>2:
                dict_fruit[ fruits[ pleft] ]  -= 1
                if dict_fruit[ fruits[ pleft] ]  == 0:
                    dict_fruit.pop( fruits[ pleft] )
                pleft += 1
            max_outcome = max(max_outcome ,  pright - pleft + 1 )
            pright+=1
        return max_outcome
```
___
#### 2483. Minimum Penalty for a Shop
```
def bestClosingTime(customers: str) -> int:
    customers = "N"+customers
    y_arr = []
    counter = 0
    for i in customers:
        if i == "Y":
            counter+=1
        y_arr.append(counter)

    min_pen = 1e8
    min_ind = 0
    for i , num in enumerate(y_arr):
        pen = (i - y_arr[i]) + (y_arr[-1] - y_arr[i])
        if pen < min_pen:
            min_pen = pen
            min_ind = i

    return min_ind
```
----
#### 1876. Substrings of Size Three with Distinct Characters
```
def countGoodSubstrings(s: str) -> int:
    count = 0
    for i in range(len(s) - 2):
        if len(set(s[i:i+3])) == 3:
            count += 1
    return count
```
