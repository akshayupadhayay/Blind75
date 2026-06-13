class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        preMap = {}  # value -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in preMap:
                return [preMap[diff], i]
            preMap[n] = i
        return []


sol = Solution()
lst = [1, 2, 3, 4, 5]
print(sol.twoSum(lst, 4))
