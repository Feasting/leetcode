# 9-6-2020
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i, num in enumerate(nums):
            if num in complement:
                return [i, complement[num]]
            else:
                complement[target - num] = i
        raise Exception('No valid answers')
