# Day 2

This was second day of challange. note for first day was skipped because i was writing my code in my village , cause it was Christmass Eve.
As it is. The day of Christmas was great and challange wasn't burden , but rather part , which gave feel of knoweledge growth besides spiritual and connection growth. 

---

## Two pointers

Today’s topic was interesting algorithmic idea — **Two pointers**.
Idea is quite simple , use pointers to hold nessecary info to solve task.
It allows to use **O(1)** time and space to access pointers and flattern some task to **O(N)** from strong **O(N^2)**
I was familiar with two pointers , but only in context of merging arrays in Merge sort , tht's why discovering 
it so wide use was quite impressive for me.


---

## LeetCode

I completed daily task on Leetcode and several specificaly for Two pointers approach.
Problems which impressed me most where **11.Container with most water** and **42.Traping rain water**
From first view not simple problems , and solution looks like **O(N^2)** minimum , but as discoverd further was great ,
because solved not with naive approach but with bold idea approach.
They show how two pointers can be powerful.


## LetCode problems

#### 11. Container With Most Water
```
def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        area = 0
        while left != right:
            area = max(area , abs(right-left)*(min(height[left] , height[right])) )
            if height[left] >= height[right]:
                right-=1
            else:
                left+=1
        return area
```
___
#### 42. Trapping Rain Water
```
def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        
        left_max, right_max = 0, 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left] 
                else:
                    water += left_max - height[left] 
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
                
        return water
```
