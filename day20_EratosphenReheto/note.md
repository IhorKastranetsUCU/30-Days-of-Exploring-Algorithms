# Day 20

This was the twentieth day of the challenge.
Monday , tommorow will be interesting day

---

## Eratosphen Sieve algorithm
We slighty moved to Number Theory , today we have looked on Eratosphen Sieve


## LeetCode

I've completed daily task **1266. Minimum Time Visiting All Points**.

Regarding today's algorythm , I have tested different aproaches out on **204. Count Primes**
1 ) Regular for me
2 ) Logicaly the same , however implemented differently , but best for python performance. (This python...)
3 ) Slighltly modified idea , we store lowest prime factor and do cross out of multiple of prime only once.
P.S 3 Aproach is algorithmically *O(N)* , and 3 is *O(NloglogN)* , but due to python implementation specifics , performed badly on tests.

P.S.S Give me guide , how to write fast code on python , so I wouldn't wonder that is faster due to python *specifics*


That's all for today)

----

## LetCode problems

#### My implementation of Eratosthenes Sieve Idea
```python

class Eratosphen:
    def __init__(self , n):
        self.array = [1] * n
        self.n = n
        self.is_prime = [1] * self.n
        self.is_prime[0] = self.is_prime[1] = 0
        self.lp = [0] * (n + 1)
        self.primes = []

    def calc_number_of_factor(self):
        """Calculate number of factors and return which are prime"""
        primes = []
        for i in range(2,int( (self.n)**(0.5) )+1 ):
            for j in range(i , self.n , i):
                self.array[j] += 1
                if j == i and self.array[j] == 2:
                    primes.append(j)
        return primes

    def find_primes(self):
        limit = int(self.n**0.5) + 1

        for i in range(2, limit):
            if self.is_prime[i]:
                self.is_prime[i*i : self.n : i] = [0] * len(self.is_prime[i*i : self.n : i])

        return [num for num, prime in enumerate(self.is_prime) if prime]

    def euler_search(self):

        for i in range(2, self.n + 1):
            if self.lp[i] == 0:
                self.lp[i] = i
                self.primes.append(i)

            for p in self.primes:
                x = i * p

                # Якщо вийшли за межі діапазону - зупиняємось
                if x > self.n:
                    break

                # Позначаємо найменший дільник для складеного числа x
                self.lp[x] = p

                # Якщо i ділиться на p без остачі, то p є найменшим дільником i.
                # Це означає, що для наступних чисел (i * наступне_p)
                # найменшим дільником все одно буде p, а не "наступне_p".
                # Тому ми перериваємо цикл, щоб уникнути повторного викреслення.
                if i % p == 0:
                    break

        return self.primes
```
____

#### 85. Maximal Rectangle
```python

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        cost = 0
        for i in range(len(points)-1):
            diff_x , diff_y = abs(points[i+1][0] - points[i][0]) , abs(points[i+1][1] - points[i][1])
            cost +=  max(diff_x , diff_y)


        return cost
```
____
