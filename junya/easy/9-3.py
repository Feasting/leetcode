class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        currMax = nums[0]
        for num in nums:
            curr += num
            currMax = max([currMax, curr])
            if curr < 0:
                curr = 0
        return currMax
        
# https://leetcode.com/problems/maximum-subarray/
