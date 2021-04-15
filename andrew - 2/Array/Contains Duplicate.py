#Contains Duplicate
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        set1 = set()
        
        for i in nums:
            if i in set1:
                return True
            else:
                set1.add(i)
        
        return False