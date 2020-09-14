class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort()
        ret = [intervals[0]]
        intervals.pop(0)
        
        for inter in intervals:
            if ret[-1][1] >= inter[0]:
                ret[-1][1] = max(ret[-1][1], inter[1])
            else:
                ret.append(inter)
        return ret
        
# https://leetcode.com/problems/merge-intervals/
