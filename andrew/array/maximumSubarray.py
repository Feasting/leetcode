'''
https://leetcode.com/problems/maximum-subarray/

53. Maximum Subarray (easy)

Given an integer array nums, find the contiguous subarray (containing at least one number)
 which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
 which is more subtle.

'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #Sliding window problem
        #O(n) solution
        #Traverse the array adding up the sum
            #when the sum is negative then set back to 0 since that the added value makes it neg
            #which is worse than 0 (tracking new sum)
            
        if len(nums) == 1:
            return nums[0]
        
        largestSum = nums[0]
        
        currentSum = 0
        
        for i in nums:
            currentSum += i
            
            #Set new biggest Sum
            if currentSum > largestSum:
                largestSum = currentSum
            
            #Reset Current Sum
            if currentSum < 0:
                currentSum = 0
                
        return largestSum