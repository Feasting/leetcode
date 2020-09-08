"""

https://leetcode.com/problems/maximum-product-subarray/

152. Maximum Product Subarray (Medium)

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums:
            return -1
        
        #Variables to keep track of biggest and smallest value
        #Smallest value will be generally be negative, and currMax will be largest
        #Min can turn into largest with multiplication of negative number
        currMax = nums[0]
        currMin = nums[0]
        maxProduct = nums[0]
        
        
        for i in range(1,len(nums)):
            tempMax = currMax
            #Current biggest positive number
            currMax = max(max(currMax * nums[i], currMin * nums[i]), nums[i])
            #Current smallest negative number
            currMin = min(min(tempMax * nums[i], currMin * nums[i]), nums[i])
            #Update max product
            if currMax > maxProduct:
                maxProduct = currMax
        
        return maxProduct