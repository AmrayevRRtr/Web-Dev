def max_end3(nums):
    max = nums[0]

    if (nums[0] < nums[-1]):
        max = nums[-1]

    return [max] * 3
