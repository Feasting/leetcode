"""
https://leetcode.com/problems/two-sum/
Two Sum (easy)

Given an array of integers nums and and integer target, return the indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1]
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #Save old values in dict with index saved
        #Loop and see if curr value + old value = target
        
        
        oldValues = {}
        
        for i in range(0, len(nums)):
            
            #Check if two values in arr add up to target
            if target - nums[i] in oldValues:
                return [ oldValues[ target - nums[i] ], i ]
            
            #Save old values
            if nums[i] not in oldValues:
                oldValues[ nums[i] ] = i