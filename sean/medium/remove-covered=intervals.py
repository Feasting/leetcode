# 9-14-2020
# https://leetcode.com/problems/remove-covered-intervals/

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        p = intervals[0]
        count = 1
        for interval in intervals:
            if interval[0] is p[0]:
                p = interval
            elif interval[1] > p[1]:
                p = interval
                count += 1
        return count
