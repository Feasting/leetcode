"""

https://leetcode.com/problems/product-of-array-except-self/

238. Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #Approach
        #Each output value is the product of 
        #all the left values and all the right values
        
        #Calculate left values
        
        #Output Arr
        output = [1] * len(nums)
        
        #Calculate accumulation of left array
        L = 1
        for i in range(1, len(nums)):
            output[i] = nums[i-1] * L 
            L *= nums[i - 1]
        
        #Calc Right values and multiply to the current left values
        # to get the answer
        R = 1
        for i in reversed(range(0, len(nums))):
            output[i] *= R
            R *= nums[i]
        
        return output