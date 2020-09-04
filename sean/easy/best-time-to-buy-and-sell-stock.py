# 9-3-2020
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        
        size = len(prices)
        max_profit = 0
        min_value = prices[0]
        for i in prices:
            if i - min_value > max_profit:
                max_profit = i - min_value
            if i < min_value:
                min_value = i
        return max_profit
