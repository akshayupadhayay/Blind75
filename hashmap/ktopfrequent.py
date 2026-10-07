class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for n in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return []


sol = Solution()
print(sol.topKFrequent([1, 1, 2, 2, 2, 3], 2))
