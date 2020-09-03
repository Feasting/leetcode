# 9-1-2020
# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [1] * size
        leftTotal = 1
        for i in range(size):
            result[i] *= leftTotal
            leftTotal *= nums[i]
        rightTotal = 1
        for i in reversed(range(size)):
            result[i] *= rightTotal
            rightTotal *= nums[i]
        return result
