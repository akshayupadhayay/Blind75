def remDupFromSortedArray(nums: list) -> list:
    left = 1

    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            nums[left] = nums[i]
            left += 1

    return nums[0:left]


print(remDupFromSortedArray([0, 1, 1, 2, 3, 3, 3, 4, 4]))  # [0, 1, 2, 3, 4]
