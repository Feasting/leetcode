class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        ret = 0
        min = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] < min:      
                min = prices[i]
                
            else:
                ret = max(ret, prices[i] - min)
        return ret
        
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
