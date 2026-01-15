# Day 21

This was the twenty fisrt day of the challenge.
Tuesdat , tommorow will be more interesting day

---

## Binary Exponentiation algorithm
We moved to Number Theory , today we have looked on binary exponentiation


## LeetCode

I've completed daily task **3453. Separate Squares I**.

Regarding today's algorythm , I have tested out on **50. Pow(x, n)**



That's all for today)

----

## LetCode problems

#### My implementation of Binary Exponentiation
```python
def binary_exponentiation(base: int, exponent: int) -> int:
    if exponent == 0:
        return 1

    result = 1

    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base

        exponent //= 2

    return result
```
____

#### 50. Pow(x , n)
```python

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        current_product = x

        while n > 0:
            if n % 2 == 1:
                result *= current_product

            current_product *= current_product

            n //= 2

        return result
```
____

#### 3453. Separate Squares I
```python

def comp( line : int , arr : list):
    upper = 0
    lower = 0
    for x , y , l in arr:
        if y > line:
            upper += l*l
        elif y + l < line :
            lower += l*l
        else:
            upper += (l + y - line) * l
            lower += (line - y) * l
    return 1 if upper > lower else -1


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        l = 0
        r = 1e9
        for i in range(50):
            m = (r-l)/2 + l
            if comp(m , squares) == 1 :
                l = m
            else:
                r = m

        return r
```
____
