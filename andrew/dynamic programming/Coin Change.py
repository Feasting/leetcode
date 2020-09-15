"""

https://leetcode.com/problems/coin-change/

322. Coin Change (Medium)

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #Hold best number of coins to reach each value until amount
        dp = [float('inf')] * (amount + 1)
        
        #0 coins needed to achieve 0 coin amount
        dp[0] = 0
        
        #Build up to the amount using minimum number of coins
        for coin in coins:
            for i in range(coin, amount + 1):
                #Use either current num
                currNumCoin = dp[i]
                #Use an old value + current coin
                useNewNumCoin = dp[i - coin] + 1
                
                dp[i] = min(currNumCoin, useNewNumCoin)
        
        
        if dp[amount] == float('inf'):
            #Cannot reach amount with current coin amount
            return -1
        else:
            #Can reach current coin amount
            return dp[amount]