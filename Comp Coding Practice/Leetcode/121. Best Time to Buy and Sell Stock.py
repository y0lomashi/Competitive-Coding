# Leetcode 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Find the maximum profit from buying and selling a stock

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                maxP = max(maxP, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxP


# ! for testing
prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
