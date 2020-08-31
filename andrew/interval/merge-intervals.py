"""

https://leetcode.com/problems/merge-intervals/

56. Merge Intervals (Medium)

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

 

Constraints:

intervals[i][0] <= intervals[i][1]

"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        #Loop list and append to new list, check if overlap with last value in new list
        #if so pop from newlist and combine it and add it back to the list
        
        #Complexity: O(nlogn) because of sort above
        
        newList = [ ]
        
        for i in intervals:
            if newList == []:
                newList.append(i)
            else:
                if newList[-1][1] >= i[0] and newList[-1][1] < i[1]:
                    oldIn = newList.pop()
                    newList.append( [ oldIn[0], i[1] ] )
                elif newList[-1][1] < i[1]:
                    newList.append( i )
        
        return newList