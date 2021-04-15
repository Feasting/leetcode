#Remove Duplicates from Sorted Array
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        
        #Have ptr1 keep track of current index
        #Have ptr2 find the next number and swap 
        ptr1 = 0
        ptr2 = 0
        
        def swap(ptr1, ptr2, nums):
            temp = nums[ptr1]
            nums[ptr1] = nums[ptr2]
            nums[ptr2] = temp
        
        previous = nums[ptr2]
        while ptr2 != len(nums):
            
            if previous != nums[ptr2]:
                ptr1 += 1
                previous = nums[ptr2]
                swap(ptr1, ptr2, nums)
            
            ptr2 += 1
        
        return ptr1 + 1
        