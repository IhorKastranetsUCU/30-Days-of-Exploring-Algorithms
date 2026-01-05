# Day 12
___

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