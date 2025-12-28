def maximumGap(nums: list[int]) -> int:
    min_val , max_val = min(nums) , max(nums)

    if min_val == max_val:
        return 0

    bucket_size = max(1, (max_val - min_val) // (len(nums) - 1))

    bucket_num = (max_val - min_val) // bucket_size + 1

    buck_min = [-1] * bucket_num
    buck_max = [-1] * bucket_num



    for num in nums:
        index = (num - min_val) // bucket_size

        if buck_min[index] == -1:
            buck_min[index] = num
            buck_max[index] = num
        else:
            buck_min[index] = min(buck_min[index] , num)
            buck_max[index] = max(buck_max[index] , num)

    max_g = 0
    prev_g = buck_max[0]


    for i in range( 1, bucket_num ):

        if buck_min[i] == -1:
            continue

        curr_gap =  buck_min[i] - prev_g
        max_g = max(max_g , curr_gap)

        prev_g = buck_max[i]

    return max_g


if __name__ == "__main__":
    nums = [1,10000000]
    print(maximumGap(nums))
