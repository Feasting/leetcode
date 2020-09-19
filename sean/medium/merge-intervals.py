# 9-18-2020
# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()        
        for x, y in intervals:
            if not result or result[-1][1] < x:
                result.append([x,y])
            else:
                result[-1][1] = max(result[-1][1], y)
        return result
