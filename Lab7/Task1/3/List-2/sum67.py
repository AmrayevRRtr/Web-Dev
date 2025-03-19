def sum67(nums):
    total = 0
    isSix = False
    i = 0

    while i < len(nums):
        if nums[i] == 6:
            isSix = True
        elif nums[i] == 7 and isSix:
            isSix = False
        elif not isSix:
            total += nums[i]
        i += 1

    return total