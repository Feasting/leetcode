import sys

class Solution:
    def maxProfit(self, prices) -> int:
        min = float("inf")
        maxProfit = 0
        for num in prices:
            if num < min:
                min = num
            profit = num - min
            if profit > maxProfit:
                maxProfit = profit

            
        return maxProfit