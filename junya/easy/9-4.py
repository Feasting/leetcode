class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        num = bin(n)
        for bit in num:
            if bit is '1':
                count += 1
        return count
        
# https://leetcode.com/problems/number-of-1-bits/
