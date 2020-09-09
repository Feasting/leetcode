class Solution:
    def climbStairs(self, n: int) -> int:
        ret = [1,1]
        for i in range(2, n+1):
            ret.append(ret[i - 2] + ret[i-1])
        return ret[n]
        
# https://leetcode.com/problems/climbing-stairs/
