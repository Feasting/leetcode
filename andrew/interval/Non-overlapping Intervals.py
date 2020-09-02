"""

https://leetcode.com/problems/non-overlapping-intervals/

435. Non-overlapping Intervals

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    
        #Loop array creating new array, if overlap add one
        
        count = 0
        
        newList = []
        
        #sort by end times
        intervals.sort(key = lambda x : x[1])
        
        for i in intervals:
            if newList == []:
                newList.append(i)
            else:
                if newList[-1][1] > i[0]:
                    count += 1
                elif newList[-1][1] <= i[0]:
                    newList.append( i )
        
        return count