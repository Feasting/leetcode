# 9-16-2020
# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        i = 0
        size = len(startTime)
        count = 0
        for i in range(size):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                count += 1
        return count
