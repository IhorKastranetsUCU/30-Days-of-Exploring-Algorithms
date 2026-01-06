# Day 13


## Overall
___
Yesterday I asked Yuliana to help figure out how to merge branches on `git` because
I still do it manually and we decided to do it early on the morning but undortunately
I slept over and she left. So, today I am going to do 2 commits from `main` branch.

I was thinking about gratification and realised that I haven't given myself any reward.
So I realised that I need to handle my daily routine and with doing some things I will
add some money to my travel this summer. Some daily habits that I'm going provide soon

* Day without smoking
* Push-ups
* 10k steps per day

I have been thinking about tracking this habits, and I haven't decided yet. But thinking
about how expensive my travel actually is, I understande that I need to start accumulate money 
rewards as quick as possible. 

___

## Pandas

I still solve pandas problems mostly and today I learned functions `to_frame`, `map`, `apply`,
`size` and for most of the problems I don't spend much time. Nevertheless I don't quite understand
how to use `loc`, `iloc`, `agg` which are quitly often used by other people on their solutions.
In addition I stuck on the 1084. Sales Analysis III problem on LeetCode. 

___

## LeetCode

I started with daily problem and after explanation of the problem spent 3 minutes for implementation
and 2 minutes to fix edge cases.
> ### 1975. Maximum Matrix Sum
> Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.
```Py
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        counter = 0
        min_negativ = float("inf")
        sum_of_elemetns = 0

        for i in matrix:
            for j in i:
                sum_of_elemetns += abs(j)
                if j <= 0:
                    counter += 1
                min_negativ = min(min_negativ, abs(j))

        return sum_of_elemetns if counter % 2 == 0 else sum_of_elemetns - 2 * min_negativ
```
Then I did several DB problems on pandas, and currently I have no idea how to solve this problem 
>Write a solution to report the products that were only sold in the first quarter of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.<br>

So, I will get back tomorrow and do another try.

___
## Script for setting up the working area

Nastya recommended that I create a shell script which automatically generates all the required files
for our project structure. It sounds like a very good idea and also a good way to revise how to create
files using Python or to learn shell scripting.