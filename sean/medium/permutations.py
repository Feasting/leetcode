# 9-9-2020
# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) <= 1:
            return [nums]
    
        results = []
        for i in range(len(nums)):
            comb = self.permute(nums[:i] + nums[i+1:])
            for p in comb:
                results.append([nums[i]] + p)
        return results
