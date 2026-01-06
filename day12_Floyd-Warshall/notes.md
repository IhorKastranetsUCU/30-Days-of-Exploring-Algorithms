# Day 12
___
- [Maksym’s Notes](#Maksym)
- [Ihor’s Notes](#Ihor)
___

# Maksym

This was the twelve day of the challenge.
Sunday.

---

## Floyd-Warshall

Today's topic was widely knew **Floyd-Warshall** algorithm.

### My Thoughts
Cool algorithm


### Algorithm
**Floyd-Warshall** algorithm. Useful when we want to find distances between all pair of vertices.
Idea of algorithm is similiar to transitivity property in relations.
For all possible triples of vertices we check is it possible to better result
for 2nd and 3rd vertice using 1st as connector.
After this check we as result get matrix with minimum distance for all pairs of veritces.


**Efficency**
1. Time Complexity : **O(V^3)** , because we check all possible triples(order matter).
2. Space Complexity : **O(V^2)** , **O(V^2)** size of a min distance matrix

That's all! ))

## LeetCode



I've completed daily task **1390. Four Divisors**.
Revised Sieve of Eratosphen and how divisors are found,
but as I  later understood , solved task not in the most optimal way


Regarding today's algorythm , I solved:
1.  **2976. Minimum Cost to Convert String I**
2.  **1462. Course Schedule IV**

And checked implementation on **1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance**

That's all for today)

----

## LetCode problems

#### My implementation of Bellman-Ford
```python

def Floyd_Warshall(graph: list[list], n: int):
    INF = float('inf')

    for k in range(n):
        for i in range(n):
            if graph[i][k] == INF:
                continue

            dist_ik = graph[i][k]

            for j in range(n):
                new_dist = dist_ik + graph[k][j]
                if graph[i][j] > new_dist:
                    graph[i][j] = new_dist

    return graph

def matrix_convert(edges: list, n: int):
    INF = float('inf')
    graph = [[INF] * n for _ in range(n)]

    for i in range(n):
        graph[i][i] = 0

    for u, v_node, w in edges:
        graph[u][v_node] = w

    return graph

```

#### 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
```python

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = Floyd_Warshall(matrix_convert(edges, n), n)

        min_reachable_count = float('inf')
        best_city = -1

        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and graph[i][j] <= distanceThreshold:
                    count += 1
            if count <= min_reachable_count:
                min_reachable_count = count
                best_city = i

        return best_city
```
____

#### 2976. Minimum Cost to Convert String I
```python
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        def Floyd_Warshall(graph: list[list], n: int):
            INF = float('inf')

            for k in range(n):
                for i in range(n):
                    if graph[i][k] == INF:
                        continue

                    dist_ik = graph[i][k]

                    for j in range(n):
                        new_dist = dist_ik + graph[k][j]
                        if graph[i][j] > new_dist:
                            graph[i][j] = new_dist

            return graph

        def matrix_convert(edges: list, n: int):
            INF = float('inf')
            graph = [[INF] * n for _ in range(n)]

            for i in range(n):
                graph[i][i] = 0

            for u, v_node, w in edges:
                if w < graph[u][v_node]:
                    graph[u][v_node] = w

            return graph

        n = 26
        original_idx = [ord(c) - ord('a') for c in original]
        changed_idx = [ord(c) - ord('a') for c in changed]

        edges = []
        for i in range(len(cost)):
            edges.append((original_idx[i], changed_idx[i], cost[i]))

        graph = Floyd_Warshall(matrix_convert(edges, n), n)

        res = 0
        for i in range(len(source)):
            u = ord(source[i]) - ord('a')
            v = ord(target[i]) - ord('a')

            current_cost = graph[u][v]

            if current_cost == float('inf'):
                return -1

            res += current_cost

        return res
```
____

#### 1462. Course Schedule IV
```python
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def Floyd_Warshall(graph: list[list], n: int):
            INF = float('inf')

            for k in range(n):
                for i in range(n):
                    if graph[i][k] == INF:
                        continue

                    dist_ik = graph[i][k]

                    for j in range(n):
                        new_dist = dist_ik + graph[k][j]
                        if graph[i][j] > new_dist:
                            graph[i][j] = new_dist

            return graph

        def matrix_convert(edges: list, n: int):

            INF = float('inf')
            graph = [[INF] * n for _ in range(n)]

            for i in range(n):
                graph[i][i] = 0

            for u, v_node in edges:
                graph[u][v_node] = 1

            return graph

        graph = Floyd_Warshall(matrix_convert(prerequisites, numCourses), numCourses)
        res = []
        for u , v in queries:
            ans = True if graph[u][v] != float('inf') else False
            res.append(ans)

        return res

```
____

#### 1390. Four Divisors
```python

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        end = max(nums)
        eratosfen = [(1 , 1)] * int(end+10)


        for i in range(2 ,end+1):
            for j in range(i,end+1, i):
                eratosfen[j] = (eratosfen[j][0]+1 ,eratosfen[j][1]+i)

        #print(eratosfen)
        res = 0
        for el in nums:
            if eratosfen[el][0] == 4:
                res+=eratosfen[el][1]

        return res

```
____


# Ihor


## Pandas
I continue to learn pandas and to complete database problems on **LeetCode**.
Today, I worked on solving problems using the groupby method and the different functions it provides.
In total, I solved 7 problems in pandas today. In 2 days, I am going to start working on medium-difficulty problems.

## LeetCode

I started with my daily problem, as always. It wasn’t difficult, so I managed to solve it myself without any hints.

> ### 1390. Four Divisors
>Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

```Py
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = [1, {1, num}]
            else:
                hashmap[num][0] += 1

        for num, values in hashmap.items():
            for i in range(2, int(num**(1/2) + 1)):
                if num % i == 0:
                    hashmap[num][1].add(i)
                    hashmap[num][1].add(num//i)
                if len(hashmap[num][1]) > 4:
                    break
        return sum(sum(hashmap[num][1]) * hashmap[num][0] for num in hashmap if len(hashmap[num][1]) == 4 )
```

Then, I started solving a bunch of `pandas` problems.
Some of them were quite interesting.


>### 586. Customer Placing the Largest Number of Orders
> Write a solution to find the customer_number for the customer who has placed the largest number of orders.<br>
>The test cases are generated so that exactly one customer will have placed more orders than any other customer.<br>
>The result format is in the following example.

```py
df = orders.groupby("customer_number").size().reset_index(name='count')
df[df["count"].max() == df["count"]][["customer_number"]]
```
___
> ### 607. Sales Person
> Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name "RED".
```py
all_sales = company.merge(orders, on="com_id")
red_sales = all_sales[all_sales.name == "RED"]["sales_id"]
sales_person[~sales_person["sales_id"].isin(red_sales)]['name']
```
___

## Floyd - Warshall Algorithm

So, this is an algorithm that doesn’t use any specific data structures, and I understood it very well.
I was struggling with understanding how to detect a negative cycle, but now I feel confident.