class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        totNums = sum(nums)
        n = len(nums)
        tot = n * (n + 1) // 2
        ret = tot - totNums
        if ret is 0:
            if min(nums) is 0:
                return n + 1
            return 0
        return ret
        
# https://leetcode.com/problems/missing-number/
