class Solution:
    def reverseBits(self, n: int) -> int:
        bitStr = str(bin(n))[::-1][:-2]
        for i in range(len(bitStr), 32):
            bitStr += '0'
        return int(bitStr, 2)
        
# https://leetcode.com/problems/reverse-bits/
