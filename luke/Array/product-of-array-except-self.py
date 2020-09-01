import sys

class Solution:
    def productExceptSelf(self, nums):
        prod = 1
        length = len(nums)
        output = [1] * length
        for i in range(1, length):
            prod *= nums[i-1]
            output[i] *= prod
        
        prod = 1
        for i in reversed(range(length-1)):
            prod *= nums[i+1]
            output[i] *= prod
            
        return output