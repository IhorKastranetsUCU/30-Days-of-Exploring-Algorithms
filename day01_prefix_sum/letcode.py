from turtledemo.penrose import start


def missingInteger(nums: list[int]) -> int:
    biggest_sequential_sum = nums[0]
    i = 1
    while nums[i] - nums[i-1] == 1:
        biggest_sequential_sum += nums[i]
        i += 1
    biggest_num = max(nums)
    return biggest_sequential_sum if biggest_sequential_sum > biggest_num else biggest_num + 1



def minSubArrayLen(target: int, nums: list[int]) -> int:
    prefix_sum = [nums[0]]
    for i in range(1, len(nums)):
        prefix_sum.append(prefix_sum[-1] + nums[i])

    print(prefix_sum)
    for i in range(1, len(prefix_sum) + 1):
        for j in range(len(prefix_sum) - i):
            if i == 1 and j == 0:
                print(prefix_sum[j + i] - prefix_sum[j])
            if prefix_sum[j + i] - prefix_sum[j] >= target:
                return i
    return len(nums) if sum(nums) >= target else 0


# 209 Minimum Size Subarray Sum
def minSubArrayLen(target: int, nums: list[int]) -> int:
    n = len(nums)
    prefix_sum = [nums[0]]
    lenght = n + 1

    for i in range(1, len(nums)):
        prefix_sum.append(prefix_sum[-1] + nums[i])

    for i in range(n):
        end = n - 1
        start = i
        while start <= end:
            mid = (end + start) // 2
            subsum = prefix_sum[mid] - prefix_sum[i] + nums[i]
            if subsum >= target:
                lenght = min(mid - i + 1, lenght)
                end = mid - 1
            else:
                start = mid + 1
    return 0 if lenght > n else lenght

# 724 Find Pivot Index

def pivotIndex(nums: list[int]) -> int:
    prefix_sum = []
    temp = 0
    for i in nums:
        temp += i
        prefix_sum.append(temp)
    print(prefix_sum)
    if prefix_sum[-1] - prefix_sum[0] == 0:
        return 0
    for i in range(1, len(nums)):
        right_sum = prefix_sum[-1] - prefix_sum[i]
        left_sum = prefix_sum[i-1]
        print(left_sum, right_sum)
        if right_sum == left_sum:
            return i
    return -1

# 1422 Maximum Score After Splitting a Stringe
def maxScore(s: str) -> int:
    ones_right = s.count("1")
    zeros_left = 0
    max_sum = 0
    for i in range(len(s) - 1):
        if s[i] == "0":
            zeros_left += 1
        else:
            ones_right -= 1
        max_sum = max(max_sum, zeros_left + ones_right)
    return max_sum