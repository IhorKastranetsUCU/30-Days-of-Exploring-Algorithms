# 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.
from scipy.optimize import newton


def isPalindrome(x: int) -> bool:
    """
    The function checks is the number palendrom or not and returns the bool value
    :param x: given number
    :return: bool
    >>> isPalindrome(123)
    False
    >>> isPalindrome(1234321)
    True
    >>> isPalindrome(666)
    True
    >>> isPalindrome(5555)
    True
    """
    x = str(x)
    l, r = 0, len(x) - 1
    while l < r:
        if x[l] != x[r]:
            return False
        l += 1
        r -= 1
    return True



# 28. Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first occurrence of needle
# in haystack, or -1 if needle is not part of haystack.

def strStr(haystack: str, needle: str) -> int:
    """
    The functions returns the index of first occurrence of needle in haystack
    :param haystack: string where searching will be going
    :param needle: string that need to be found
    :return int number of first occur or -1 if the needle wasn't found
    >>> haystack = "sadbutsad"
    >>> needle = "sad"
    >>> strStr(haystack, needle)
    0
    >>> haystack = "leetcode"
    >>> needle = "leeto"
    >>> strStr(haystack, needle)
    -1
    >>> haystack = "gomalungma"
    >>> needle = "lun"
    >>> strStr(haystack, needle)
    4
    """
    if needle == "":
        return 0
    if len(needle) > len(haystack):
        return -1
    i = 0
    j = 0
    start = 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            j += 1
            if j == len(needle):
                return i - j + 1
        else:
            start += 1
            i = start - 1
            j = 0
        i += 1
    return -1


# 88. Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements
# that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    The function modify the nums1 array by merging it with the nums2 array in sorted way
    It takes the number m the exact point where array nums1 finish and n where nums2 finish
    :param nums1: the main array that need to be modified
    :param m: the integer number to finish nums1 array
    :param nums2: the array which takes the elements
    :param n: the integer number to finish nums2 array
    :return: None

    >>> nums1 = [1,2,3,0,0,0]
    >>> merge(nums1, 3, [2,5,6], 3)
    >>> nums1
    [1, 2, 2, 3, 5, 6]

    >>> nums1 = [1]
    >>> merge(nums1, 1, [], 0)
    >>> nums1
    [1]

    >>> nums1 = [0]
    >>> merge(nums1, 0, [1], 1)
    >>> nums1
    [1]

    >>> nums1 = [2,0]
    >>> merge(nums1, 1, [1], 1)
    >>> nums1
    [1, 2]
    """
    i = j = 0
    while j < n:
        if i >= m + j or nums2[j] <= nums1[i]:
            nums1.insert(i, nums2[j])
            j += 1
            nums1.pop()
        i += 1


# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase
# letters and removing all non-alphanumeric characters, it reads the same forward
# and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.


def isPalindrome(s: str) -> bool:
    """
    The Function returns True if the string is a palindrom after removing all ASCII characters
    except the letters and digists
    :param s: str, the given string
    :return: bool, True if it is palindrom, False otherwise
    >>> isPalindrome("Hello my name is 'sieman ymo lleh'")
    True
    >>> isPalindrome("%$#")
    True
    >>> isPalindrome(("%He@@"))
    False
    """
    s = "".join([i.lower() for i in s if i.isalnum()])
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


# 202. Happy Number
# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.

def isHappy(n: int) -> bool:
    """
    Return True if the sum recursive sum of the digits in square gives 1 and not going to endless loop
    :param n: int, given number
    :return: bool, True if the number is happy, False otherwise
    >>> isHappy(1)
    True
    >>> isHappy(42)
    False
    >>> isHappy(6)
    False
    >>> isHappy(69)
    False
    >>> isHappy(9)
    False
    """

    def next_num(x):
        return sum([int(i) ** 2 for i in str(x)])
    slow = n
    fast = next_num(n)
    while fast != 1 and slow != fast:
        slow = next_num(slow)
        fast = next_num(next_num(fast))
    return fast == 1



#11. Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that
# the two endpoints of the ith line are (i, 0) and (i, height[i]).

def maxArea(height: list[int]) -> int:
    max_capacity = 0
    l, r = 0, len(height) - 1
    while l < r:
        max_capacity = max((r-l) * min(height[l], height[r]), max_capacity)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_capacity


# 42. Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.

def trap(height: list[int]) -> int:
    n = len(height)
    if n == 0 or min(height) == max(height):
        return 0

    lmax = [height[0]] * n
    rmax = [height[n - 1]] * n
    l = 0
    r = len(height) - 1
    for i in range(1, n):
        lmax[i] = max(lmax[i - 1], height[i])
        rmax[n - 1 - i] = max(rmax[n - i], height[n - 1 - i])
    total = 0
    for i in range(n):
        total += min(lmax[i], rmax[i]) - height[i]
    return total