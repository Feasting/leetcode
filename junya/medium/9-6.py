class Solution:
    def countBits(self, num: int) -> List[int]:
        retList = []
        for i in range(0, num + 1):
            count = 0
            biStr = str(bin(i))
            for bit in biStr:
                if bit is '1':
                    count += 1
            retList.append(count)
        return retList
        
# https://leetcode.com/problems/counting-bits/
