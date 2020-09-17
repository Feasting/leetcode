# 9-16-2020
# https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        size = len(nums)
        count = 0
        for i in range(size-1):
            for j in range(i+1, size):
                if nums[i] == nums[j]:
                    count += 1
        return count
