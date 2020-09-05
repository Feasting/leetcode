# 9-4-2020
# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            result += n & 1
            n >>= 1
        return result
