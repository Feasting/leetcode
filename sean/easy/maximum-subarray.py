# 9-3-2020
# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = s = nums[0]
        for num in nums[1:]:
            s = max(num, s + num)
            largest = max(s, largest)
        
        return largest
