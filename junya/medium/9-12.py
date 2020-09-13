class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ret = [0]
        for i in range(1, amount + 1):
            potNum = []
            for coin in coins:
                prev = i - coin
                if prev >= 0 and ret[prev] >= 0:
                    potNum.append(ret[prev] + 1)
            if potNum:
                ret.append(min(potNum))
            else:
                ret.append(-1)
        return ret[amount]
        
# https://leetcode.com/problems/coin-change/
