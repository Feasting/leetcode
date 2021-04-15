#Single Number
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dict1 = {}
        
        # Solution 1: dictionary approach where I could occurence of each number
        
        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
                
        for i in nums:
            if dict1[i] == 1:
                return i