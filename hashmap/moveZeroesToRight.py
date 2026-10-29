def moveZeroesToRight(nums: list[int]) -> list[int]:
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums


print(moveZeroesToRight([0, 1, 0, 3, 12, 0]))  # Output: [1, 3, 12, 0, 0]
