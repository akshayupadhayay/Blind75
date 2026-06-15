class Solution:
    def buySellStocks(self, prices: list[int]) -> int:
        left = 0
        right = 1
        maxP = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
            else:
                left = right
            right += 1

        return maxP


sol = Solution()
lst_1 = [7, 1, 5, 3, 6, 4]
print(sol.buySellStocks(lst_1))

lst_2 = [7, 6, 4, 3, 1]
print(sol.buySellStocks(lst_2))
